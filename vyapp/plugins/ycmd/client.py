"""
Overview
========

This plugin does autocompletion using ycmd.


Key-Commands
============

Namespace: ycmd

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible words for
completion.

"""

from vyapp.completion import CompletionWindow, Option
from os.path import expanduser, join, exists, dirname
from base64 import b64encode, b64decode
from vyapp.plugins import ENV
from tempfile import NamedTemporaryFile
from subprocess import Popen, PIPE
from vyapp.areavi import AreaVi
from urllib.parse import urlparse
from shutil import copyfile
import requests
import random
import hashlib
import atexit
import hmac
import json
import time
import os
import time

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
    def __init__(self, path, port, settings_file, extra_file):
        self.settings_file = settings_file
        self.extra_file    = extra_file 
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

        self.daemon = Popen(self.cmd % (self.port,
        tmpfile.name), shell=1, cwd=self.path)

        atexit.register(self.daemon.terminate)

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
       # 'extra_conf_data': self.extra_file
        }

        url = '%s/event_notification' % self.url
        hmac_secret = self.hmac_req('POST', '/event_notification', 
        data, self.hmac_secret)

        headers = {
            'X-YCM-HMAC': hmac_secret,
        }

        req = requests.post(url, 
            json=data, headers=headers)

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

        req = requests.post(url, json=data, headers=headers)
        print('Request data:', req.json())
        return self.fmt_options(req.json())

    def fmt_options(self, data):
        return [Option(ind.get('insertion_text', ''),
            'Type:%s' % ind.get('kind', '')) for ind in data['completions']]
    
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
        completions = lambda event: YcmdWindow(event.widget, self.server)

        # This lambda sends the ReadyToParseEvent to ycmd whenever a file is
        # opened or saved. It is necessary to start some 
        # ycmd language completers.
        ready = lambda : self.server.ready(1, 1, area.filename, 
        {area.filename:  {'filetypes': [FILETYPES[area.extension]], 
        'contents': area.get('1.0', 'end')}})

        wrapper = lambda event: area.after(1000, ready)
        area.install('ycmd', ('INSERT', '<Control-Key-period>', completions),
        (-1, '<<LoadData>>', wrapper), (-1, '<<SaveData>>', wrapper))

    @classmethod
    def setup(cls, path):
        # Create the default_settings.json file in case it doesn't exist.
        # The file is located in the home dir.
        settings_file = join(expanduser('~'), '.default_settings.json')
        if not exists(settings_file): 
            copyfile(join(dirname(__file__), 
                'default_settings.json'), settings_file)

        # extra_file = join(expanduser('~'), '.ycm_extra_conf.py')
        # if not exists(extra_file): 
            # copyfile(join(dirname(__file__), 
                # 'ycm_extra_conf.py'), extra_file)

        port = random.randint(1000, 9999)
        cls.server = YcmdServer(path, port,  settings_file, '')

install = YcmdCompletion




