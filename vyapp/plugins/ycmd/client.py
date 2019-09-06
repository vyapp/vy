"""
Overview
========

This plugin does autocompletion using ycmd.


Key-Commands
============

Namespace: ycmd

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.

"""

from vyapp.completion import CompletionWindow, TextWindow
from base64 import b64encode, b64decode
from vyapp.plugins import ENV
from tempfile import NamedTemporaryFile
from subprocess import Popen, PIPE
from vyapp.areavi import AreaVi
from urllib import parse
import requests
import hashlib
import hmac
import json
import time

HMAC_HEADER  = 'X-Ycm-Hmac'
HMAC_LENGTH  = 16
IDLE_SUICIDE = 10800  # 3 hours
MAX_WAIT     = 5
YCMD_OUTPUT  = True

class YcmdServer:
    def __init__(self, path, port, settings, extra):
        self.path     = path
        self.port     = port
        self.settings = settings
        self.extra    = extra

        cmd    = 'python -m %s --options_file %s'
        daemon = Popen(cmd % (self.path, settings), shell=1, stdin=PIPE, 
        stdout=PIPE, stderr=PIPE, encoding=self.area.charset)

        stdout, stderr = daemon.communicate(data)

class YcmdWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()

        # completions = .completions()
        CompletionWindow.__init__(self, area, completions, *args, **kwargs)

class YcmdCompletion:
    server = None
    def __init__(self, area):
        completions = lambda event: YcmdWindow(event.widget)
        rmtrigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')
        trigger = lambda event: area.hook('ycmd', 'INSERT', 
        '<Control-Key-period>', completions, add=False)

   
        area.install('ycmd', (-1, '<<Load/*.py>>', trigger), 
        (-1, '<<Save/*.py>>', trigger), (-1, '<<LoadData>>', rmtrigger),
        (-1, '<<SaveData>>', remove_trigger))

    def setup(self, server):
        pass

install = Ycmd

