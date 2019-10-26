"""
Overview
========

This plugin does autocompletion using ycmd.

Install
=======


Key-Commands
============

Namespace: ycmd

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible words for
completion.

Commands
========

Command: lycm(path=None)
Description: Create a .ycm_extra_conf.py in the specified folder path. When
path is not specified it creates in the user home dir.

"""

from vyapp.completion import CompletionWindow, Option
from os.path import expanduser, join, exists, dirname
from base64 import b64encode, b64decode
from vyapp.widgets import LinePicker
from tempfile import NamedTemporaryFile
from subprocess import Popen, PIPE
from shutil import copyfile
from vyapp.plugins import ENV
from vyapp.app import root
from vyapp.base import printd
from vyapp.areavi import AreaVi
import atexit
import requests
import random
import hashlib
import hmac
import json
import os

HMAC_LENGTH  = 32

# Vim filetypes mapping.
FILETYPES = {
'.c': 'c',
'.py': 'python',
'.go': 'golang',
'.c++':'cpp',
'.js':'javascript',
'.java': 'java'
}


class YcmdServer:
    def __init__(self, path, port, settings_file, idle_suicide=300):
        """
        """

        self.settings_file = settings_file
        self.settings      = None
        self.path          = path
        self.port          = port
        self.url           = 'http://127.0.0.1:%s' % port 
        self.idle_suicide  = idle_suicide
        self.hmac_secret   = os.urandom(HMAC_LENGTH)

        with open(self.settings_file) as fd:
          self.settings = json.loads(fd.read())

        hmac_secret = b64encode(self.hmac_secret).decode('utf8 ')
        self.settings[ 'hmac_secret' ] = hmac_secret

        with NamedTemporaryFile(mode = 'w+', delete = False) as tmpfile:
            json.dump(self.settings, tmpfile)

        # It is necessary to use stdout=PIPE, stderr=PIPE otherwise
        # we get ycmd outputing stuff even in non verbose mode.
        self.cmd = ['python', '-m', 'ycmd', 
        '--port', str(self.port), '--options_file', tmpfile.name, 
        '--idle_suicide_seconds', str(self.idle_suicide)]

        self.daemon = Popen(self.cmd,  cwd=self.path)
        atexit.register(self.daemon.terminate)

    def load_conf(self, path):
        """
        """

        data = {
       'filepath': path,
        }

        url = '%s/load_extra_conf_file' % self.url
        hmac_secret = self.hmac_req('POST', 
        '/load_extra_conf_file', data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.post(url, json=data, headers=headers)

        printd('Ycmd - Loading extra conf...', path)
        printd('Ycmd - Load conf response:', req.json())

    def is_alive(self):
        """
        """
        hmac_secret = self.hmac_req('GET', 
        '/healthy', '', self.hmac_secret)

        url = '%s/healthy' % self.url
        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.get(url, headers=headers)
        printd('Ycmd - /healthy response status..\n', req.status_code)
        printd('Ycmd - /healthy response JSON', req.json())

    def ready(self, line, col, path, data):
        """
        Send file ready.
        """

        req = self.e_send('FileReadyToParse', line, col, path, data)
        printd('Ycmd - /FileReadyToParse status', req.status_code)
        printd('Ycmd - FileReadyToParse Event Response JSON:\n', req.json())
        return req

    def debug_info(self, line, col, path, data):
        data = {
       'line_num': line,
       'column_num': col,
       'filepath': path,
       'file_data': data
        }

        url = '%s/debug_info' % self.url
        hmac_secret = self.hmac_req('POST', '/debug_info', 
        data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.post(url, json=data, headers=headers, timeout=2)
        printd('Ycmd - debug_info Event Response JSON:\n', req.json())
        return req

    def e_send(self, name,  line, col, path, data):
        """
        Send event notification.
        """

        data = {
       'line_num': line,
       'column_num': col,
       'filepath': path,
       'file_data': data,
       'event_name': name,
        }

        url = '%s/event_notification' % self.url
        hmac_secret = self.hmac_req('POST', '/event_notification', 
        data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.post(url, json=data, headers=headers, timeout=1)
        return req

    def buffer_unload(self, line, col, path, data):
        """
        When an AreaVi instance is destroyed it is sent.
        It is useful to lower resource consume.
        """

        req = self.e_send('BufferUnload', line, col, path, data)
        printd('Ycmd - BufferUnload status', req.status_code)
        printd('Ycmd - BufferUnload Event Response JSON:\n', req.json())
        return req


    def post(self, *args, **kwargs):
        """
        Abstract the workings of HTTP POST method to validate
        HMAC in responses.
        """

        req = requests.post(*args, **kwargs)
        is_valid = self.is_vhmac(req.text, 
        req.headers['X-YCM-HMAC'], self.hmac_secret)

        if not is_valid:
            raise RuntimeError('Invalid HMAC response')
        return req

    def get(self, *args, **kwargs):
        """
        Abstract the workings of HTTP GET method to validate
        HMAC in responses.
        """

        req = requests.get(*args, **kwargs)
        is_valid = self.is_vhmac(req.text, 
        req.headers['X-YCM-HMAC'], self.hmac_secret)

        if not is_valid:
            raise RuntimeError('Invalid HMAC response')
        return req

    def completions(self, line, col, path, data, 
        dir, target=None, cmdargs=None):

        data = {
       'line_num': line,
       'column_num': col,
       'filepath': path,
       'file_data': data
        }

        url = '%s/completions' % self.url

        hmac_secret = self.hmac_req('POST', '/completions', 
        data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.post(url, json=data, headers=headers, timeout=2)
        printd('Request data:', req.json())
        return self.build_docs(req.json())

    def build_docs(self, data):
        return [Option(ind.get('insertion_text', ''), 
            self.fmt_option(ind)) for ind in data['completions']]

    def fmt_option(self, option):
        kind     = option.get('kind', '')
        details  = option.get('detailed_info', '')
        data     = option.get('extra_data', {})
        location = data.get('location', {})
        path     = location.get('filepath', '')
        line     = location.get('line_num', '')

        return '\n\n'.join(('Kind: %s' % kind, 
        'Details: %s' % details, 'Path: %s\nLine:%s' % (path, line)))

            
    def hmac_req(self, method, path, body, hmac_secret):
        """
        Calculate hmac for request. The algorithm is based on what is seen in
        https://github.com/ycm-core/ycmd/blob/master/examples/example_client.py
        at CreateHmacForRequest function.
        """

        method = bytes(method, encoding = 'utf8' )
        path   = bytes(path, encoding = 'utf8' )

        # In case of HTTP GET it can't use json.dumps because it returns
        # "''" that makes the hmac be calculated wrongly.
        body = json.dumps(body, ensure_ascii = False) if body else ''
        body = bytes(body, encoding = 'utf8' )

        method = bytes(hmac.new(hmac_secret, 
        method, digestmod = hashlib.sha256).digest())

        path = bytes(hmac.new(hmac_secret, 
        path, digestmod = hashlib.sha256).digest())

        body = bytes(hmac.new(hmac_secret, 
        body, digestmod = hashlib.sha256).digest())

        joined = bytes().join((method, path, body))

        data = bytes(hmac.new(hmac_secret, joined, 
        digestmod = hashlib.sha256).digest())

        return str(b64encode(data), encoding='utf8 ')

    def is_vhmac(self, body, hmac_header, hmac_secret):
        """
        Check the response hmac.
        """

        body = body.encode('utf8')
        a = b64decode(hmac_header)
        b = bytes(hmac.new(hmac_secret,
        msg = body, digestmod = hashlib.sha256).digest())

        if len(a) != len(b):
            return False
       
        result = 0
        for x, y in zip(a, b):
            result |= x ^ y
        return result == 0
       
class YcmdWindow(CompletionWindow):
    """
    """

    def __init__(self, area, server, *args, **kwargs):
        source    = area.get('1.0', 'end')
        line, col = area.indcur()
    
        data = {area.filename: 
        {'filetypes': [FILETYPES[area.extension]], 'contents': source}}

        completions = server.completions(line, col + 1, 
        area.filename, data, dirname(area.filename))

        CompletionWindow.__init__(self, area, completions, *args, **kwargs)

class YcmdCompletion:
    server = None
    def __init__(self, area):
        self.area       = area
        self.err_picker = LinePicker()
        completions     = lambda event: YcmdWindow(event.widget, self.server)
        wrapper         = lambda event: area.after(1000, self.on_ready)

        # Used to keep the server alive.
        def keep():
            self.server.is_alive()
            area.after(250000, keep)
        area.after(250000, keep)

        # area.master.bind('<Destroy>', self.on_unload)
        area.install('ycmd', ('INSERT', '<Control-Key-period>', completions),
        (-1, '<<LoadData>>', wrapper), (-1, '<<SaveData>>', wrapper), 
        ('NORMAL', '<Control-greater>', lambda event: self.err_picker.display()))

    def on_unload(self, event):
        """
        """
        data = {self.area.filename:  
        {'filetypes': [FILETYPES[self.area.extension]], 
        'contents': self.area.get('1.0', 'end')}}

        req = self.server.buffer_unload(1, 1, self.area.filename, data)
        printd('Ycmd - BufferUnload status', req.status_code)
        printd('Ycmd - BufferUnload JSON response', req.json())

    def on_ready(self):
        """
        This method sends the ReadyToParseEvent to ycmd whenever a file is
        opened or saved. It is necessary to start some 
        ycmd language completers.

        When there is a global .ycm_extra_conf.py in the home dir
        then it is loaded automatically otherwise a message is
        displayed to the user to load it using lycm.
        """

        data = {self.area.filename:  
        {'filetypes': [FILETYPES[self.area.extension]], 
        'contents': self.area.get('1.0', 'end')}}

        req = self.server.ready(1, 1, self.area.filename, data)
        rsp = req.json()

        if req.status_code == 500:
            self.on_exc(rsp)
        elif req.status_code == 200 and rsp:
            self.on_diagnostics(rsp)

    def on_diagnostics(self, rsp):
        """
        """

        ranges = [(ind['location']['filepath'], 
        ind['location']['line_num'], ind['text']) 
        for ind in rsp]

        self.err_picker(ranges, display=False)
        root.status.set_msg('Ycmd found errors. Displaying diagnostics!')

    def on_exc(self, rsp):
       exc = rsp.get('exception')
       if exc and exc.get('TYPE') == 'UnknownExtraConf':
           self.is_gxconf(exc['extra_conf_file'])
   
    @classmethod
    def is_gxconf(cls, xconf):
        gxconf = expanduser('~')
        gxconf = join(gxconf, '.ycm_extra_conf.py')

        if xconf == gxconf:
            cls.server.load_conf(gxconf)
        else:
            root.status.set_msg((('Found %s!' 
                ' lycm(path) to load.') % xconf))

    @classmethod
    def setup(cls, path, xconf=expanduser('~')):
        """ 
        Create the default_settings.json file in case it doesn't exist.
        The file is located in the home dir. It also starts ycmd server.

        It also creates a global ycm_extra_conf.py file in your home dir.
        This file is used for giving completion for c-family languages and
        specifying some specific settings.

        Check ycmd docs for details.
        """
        settings_file = join(expanduser('~'), '.default_settings.json')
        if not exists(settings_file): 
            copyfile(join(dirname(__file__), 
                'default_settings.json'), settings_file)

        xconf = join(xconf, '.ycm_extra_conf.py')
        if not exists(xconf): 
            copyfile(join(dirname(__file__), 'ycm_extra_conf.py'), xconf)
    
        port        = random.randint(1000, 9999)
        cls.server  = YcmdServer(path, port,  settings_file)
        ENV['lycm'] = cls.lycm
        ENV['dycm'] = cls.dycm

    @classmethod
    def dycm(cls):
        data = {AreaVi.ACTIVE.filename:  
        {'filetypes': [FILETYPES[AreaVi.ACTIVE.extension]], 
        'contents': AreaVi.ACTIVE.get('1.0', 'end')}}

        cls.server.debug_info(1, 1, AreaVi.ACTIVE.filename, data)

    @classmethod
    def lycm(cls, path=None):
        """
        """
        home = expanduser('~')
        path = path if path else join(home, '.ycm_extra_conf.py')

        cls.server.load_conf(path)
        root.status.set_msg('Loaded %s' % path)

def init_ycm(path):
    """ 
    Generate a ycm_extra_conf.py file in the given path dir to specify
    compilation flags for a project. This is necessary to get
    semantic analysis for c-family languages.

    Check ycmd docs for more details.
    """

    conf = join(path, '.ycm_extra_conf.py')
    if exists(conf):
        root.status.set_msg('File overwritten: %s' % conf)
    copyfile(join(dirname(__file__), 'ycm_extra_conf.py'), conf)

    return conf

ENV['init_ycm'] = init_ycm
install = YcmdCompletion




