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

from vyapp.complete import CompleteWindow, Option
from subprocess import Popen
import json
import requests
import sys
import atexit
from os.path import expanduser, join, exists, dirname
from os import getcwd
from shutil import copyfile
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

filename = join(expanduser('~'), '.tern-config')
if not exists(filename): copyfile(join(dirname(__file__), 'tern-config'), filename)

class Tern(object):
    def __init__(self, path):
        self.path  = path
        self.child = Popen([path, '--persistent'])
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
                                'docs': 'true',
                                'types': 'true', 
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
        return map(lambda ind: Option(**ind), data['completions'])

class JavascriptCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, tern, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()
        completions = tern.completions(source, line - 1, col, area.filename)

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)
        self.bind('<F1>', lambda event: sys.stdout.write('/*%s*/\n%s\n' % ('*' * 80, self.box.elem_desc())))

class JavascriptCompletion(object):
    def __init__(self, area, tern):
        self.tern = tern
        trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                  lambda event: JavascriptCompleteWindow(self.tern, event.widget), add=False)
        remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')
        area.install((-1, '<<Load-application/x-javascript>>', trigger),
                     (-1, '<<Load-text/html>>', trigger), 
                     (-1, '<<Save-application/x-javascript>>', trigger), 
                     (-1, '<<Save-text/html>>', trigger), 
                     (-1, '<<LoadData>>', remove_trigger), (-1, '<<SaveData>>', remove_trigger))

def javascript_tools(tern):
    active_completion = lambda :AreaVi.ACTIVE.hook('INSERT', '<Control-Key-period>', 
                  lambda event: JavascriptCompleteWindow(tern, event.widget), add=False)
    ENV['active_javascript_completion'] = active_completion

install = JavascriptCompletion








