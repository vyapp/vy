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
import shlex
import requests
import random
import hashlib
import atexit
import hmac
import json
import sys
import os

HMAC_LENGTH  = 32
IDLE_SUICIDE = 10800  # 3 hours
MAX_WAIT     = 5

# Vim filetypes mapping.
FILETYPES = {
'.c': 'cpp',
'.py': 'python',
'.go': 'golang',
'.c++':'cpp',
'.js':'javascript'
}


class YcmdServer:
    def __init__(self, path, port, settings_file):
        """
        """

        self.settings_file = settings_file
        self.settings      = None
        self.path          = path
        self.port          = port
        self.url           = 'http://127.0.0.1:%s' % port 
        self.cmd           = 'python -m ycmd --port %s --options_file  %s'
        self.hmac_secret   = os.urandom(HMAC_LENGTH)

        with open(self.settings_file) as fd:
          self.settings = json.loads(fd.read())

        hmac_secret = b64encode(self.hmac_secret).decode('utf8 ')
        self.settings[ 'hmac_secret' ] = hmac_secret

        with NamedTemporaryFile(mode = 'w+', delete = False) as tmpfile:
            json.dump(self.settings, tmpfile)

        # It is necessary to use stdout=PIPE, stderr=PIPE otherwise
        # we get ycmd outputing stuff even in non verbose mode.
        self.cmd    = self.cmd % (self.port, tmpfile.name)
        self.cmd    = shlex.split(self.cmd)
        self.daemon = Popen(self.cmd, stdout=PIPE, stderr=PIPE, cwd=self.path)

        atexit.register(self.daemon.terminate)

    def load_conf(self, path):
        """
        """

        data = {
       'filepath': path,
        }

        url = '%s/load_extra_conf_file' % self.url
        hmac_secret = self.hmac_req('POST', '/load_extra_conf_file', 
        data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.post(url, json=data, headers=headers)

        print('File to load:', path)
        print('Load conf response:', req.json())
        print('Loading extra conf...')

    def ready(self, line, col, path, data):
        """
        Send file ready.
        """

        data = {
       'line_num': line,
       'column_num': col,
       'filepath': path,
       'file_data': data,
       'event_name': 'FileReadyToParse',
        }

        url = '%s/event_notification' % self.url
        hmac_secret = self.hmac_req('POST', '/event_notification', 
        data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = self.post(url, json=data, headers=headers, timeout=1)

        print('FileReadyToParse JSON:\n', req.json())
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
        print('Request data:', req.json())
        return self.fmt_options(req.json())

    def fmt_options(self, data):
        return [Option(ind.get('insertion_text', ''),
        '\n\n'.join(('Type:\n%s' % ind.get('kind', None),
        'Extra info:\n%s' % ind.get('extra_menu_info', None),
        'Docs:\n%s' % ind.get('detailed_info', None),
        'Data:\n%s' % ind.get('extra_data', {}).get('doc_string', None)))) 
        for ind in data['completions']]
    
    def hmac_req(self, method, path, body, hmac_secret):
        """
        Calculate hmac for request. The algorithm is based on what is seen in
        https://github.com/ycm-core/ycmd/blob/master/examples/example_client.py
        at CreateHmacForRequest function.
        """

        method = bytes(method, encoding = 'utf8' )
        path   = bytes(path, encoding = 'utf8' )
        body   = json.dumps(body, ensure_ascii = False)
        body   = bytes(body, encoding = 'utf8' )

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
        self.area   = area
        completions = lambda event: YcmdWindow(event.widget, self.server)

        wrapper = lambda event: area.after(1000, self.on_ready)
        area.install('ycmd', ('INSERT', '<Control-Key-period>', completions),
        (-1, '<<LoadData>>', wrapper), (-1, '<<SaveData>>', wrapper))

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
        elif req.status_code == 200:
            self.on_diagnostics(rsp)

    def on_diagnostics(self, rsp):
        """
        """

        ranges = [(ind['location']['filepath'], 
        ind['location']['line_num'], ind['text']) 
        for ind in rsp]

        options = LinePicker()
        options(ranges)

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
        # wrapper     = lambda event: area.after(1000, self.load_gxconf)
        ENV['lycm'] = cls.lycm

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

