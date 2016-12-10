"""
Overview
========

This module implements javascript autocompletion using the tern javascript library.


Key-Commands
============

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.
"""

from vyapp.completion import CompletionWindow, Option
from subprocess import Popen, PIPE
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

class JavascriptCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, path, port, area, *args, **kwargs):
        # If ~/.tern-port doesn't exist then run the server.
        self.path   = path
        self.port   = port
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()

        if not exists(join(expanduser('~'), '.tern-port')): 
            self.run_server()

        completions = self.completions(source, line - 1, col, area.filename)

        CompletionWindow.__init__(self, area, completions, *args, **kwargs)
        self.bind('<F1>', lambda event: 
        sys.stdout.write('/*%s*/\n%s\n' % ('*' * 80, 
        self.box.selection_docs())))

    def run_server(self):
        self.child = Popen([self.path, '--port', str(self.port), 
        '--persistent'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.child.stdout.readline()
        atexit.register(self.child.terminate)

    def completions(self, data, line, col, filename):
        """
        """

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
        
        addr = 'http://localhost:%s' % self.port
        req  = requests.post(addr, data=json.dumps(payload))
        return self.build(req.text)

    def build(self, data):
        data = json.loads(data)
        return map(lambda ind: Option(**ind), data['completions'])

class JavascriptCompletion(object):
    def __init__(self, area, path='tern', port=1234):
        self.path = path
        self.port = port
        trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                  lambda event: JavascriptCompletionWindow(self.path, self.port, event.widget), add=False)
        remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')
        area.install((-1, '<<Load-application/x-javascript>>', trigger),
                     (-1, '<<Load-text/html>>', trigger), 
                     (-1, '<<Save-application/x-javascript>>', trigger), 
                     (-1, '<<Save-text/html>>', trigger), 
                     (-1, '<<LoadData>>', remove_trigger), (-1, '<<SaveData>>', remove_trigger))

def javascript_tools(path='tern', port=1234):
    active_completion = lambda :AreaVi.ACTIVE.hook('INSERT', '<Control-Key-period>', 
                  lambda event: JavascriptCompletionWindow(path, port, event.widget), add=False)
    ENV['active_javascript_completion'] = active_completion

install = JavascriptCompletion


