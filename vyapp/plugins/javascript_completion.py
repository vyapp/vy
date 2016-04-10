"""
Overview
========

This module implements javascript autocompletion using the tern javascript library.

See: http://ternjs.net

Usage
=====

This plugin places a tern-config file in the user home directory, such a file is used by tern
to load plugins like nodejs, requirejs, angularjs, as well as other options for tern library.

The ~/.tern-config file would look like:

    {
      "libs": [
        "browser",
        "jquery"
      ],
      "loadEagerly": [
        "importantfile.js"
      ],
      "plugins": {
        "requirejs": {
          "baseURL": "./",
          "paths": {}
        },
        "node": {}
      }
    }
    

In order to have completion working, press <Control-key-period> in INSERT mode.


Key-Commands
============

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.
"""

from vyapp.complete import CompleteWindow
from subprocess import Popen
import json
import requests
import sys
import atexit
from os.path import expanduser, join, exists, dirname
from os import getcwd
from shutil import copyfile

filename = join(expanduser('~'), '.tern-config')
if not exists(filename): copyfile(join(dirname(__file__), 'tern-config'), filename)

class Option(object):
    def __init__(self, name, docstring=''):
        self.name      = name
        self.docstring = docstring

class Tern(object):
    def __init__(self, path):
        self.path  = path
        self.child = Popen([path])
        atexit.register(self.child.terminate)

    def parse_port(self):
        with open(join(getcwd(), '.tern-port'), 'r') as fd:
            return int(fd.read())

    def port(self):
        port = self.parse_port()

        def shell():
            return port
        self.port = shell
        return port

    def completions(self, data, line, col, filename):
        payload = {
                    'query': { 
                                'type': 'completions', 
                                'file':filename,
                                'end': {'line': line, 'ch':col},
                             },

                    'files': [{"type": "full",
                               "name": filename,
                               "text": data}] 
                  }
        
        addr = 'http://localhost:%s' % self.port()
        req  = requests.post(addr, data=json.dumps(payload))
        return self.build(req.text)

    def build(self, data):
        data = json.loads(data)
        return map(Option, data['completions'])

class JavascriptCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, tern, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()
        completions = tern.completions(source, line - 1, col, area.filename)

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)

class JavascriptCompletion(object):
    def __init__(self, area, tern):
        self.tern = tern
        trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                  lambda event: JavascriptCompleteWindow(self.tern, event.widget), add=False)
        area.install((-1, '<<Load-application/x-javascript>>', trigger),
        (-1, '<<Save-application/x-javascript>>', trigger), (-1, '<<LoadData>>', lambda event: 
                                      area.unhook('INSERT', '<Control-Key-period>')))

install = JavascriptCompletion



