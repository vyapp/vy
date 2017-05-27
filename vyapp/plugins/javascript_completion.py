"""
Overview
========

This module implements javascript autocompletion using the tern javascript library.


Key-Commands
============

Namespace: javascript-completion

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.
"""

from vyapp.completion import CompletionWindow, Option
from os.path import expanduser, join, exists, dirname
from subprocess import Popen, PIPE
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from shutil import copyfile
from os import getcwd
import json
import requests
import sys
import atexit

filename = join(expanduser('~'), '.tern-config')
if not exists(filename): copyfile(join(dirname(__file__), 'tern-config'), filename)

class JavascriptCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        # If ~/.tern-port doesn't exist then run the server.
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
        self.child = Popen([JavascriptCompletion.PATH, 
        '--port', str(JavascriptCompletion.PORT), '--persistent'], 
        stdin=PIPE, stdout=PIPE, stderr=PIPE)

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
        
        addr = 'http://localhost:%s' % JavascriptCompletion.PORT
        req  = requests.post(addr, data=json.dumps(payload))
        return self.build(req.text)

    def build(self, data):
        data = json.loads(data)
        return map(lambda ind: Option(**ind), data['completions'])

class JavascriptCompletion(object):
    PATH = 'tern'
    PORT = 1234

    def __init__(self, area):
        trigger = lambda event: area.hook('javascript-completion', 
        'INSERT', '<Control-Key-period>', lambda event: JavascriptCompletionWindow(
        event.widget), add=False)

        remove_trigger = lambda event: area.unhook(
        'INSERT', '<Control-Key-period>')

        area.install('javascript-completion', 
        (-1, '<<Load/*.js>>', trigger),
        (-1, '<<Load/*.html>>', trigger), 
        (-1, '<<Save/*.js>>', trigger), 
        (-1, '<<Save/*.html>>', trigger), 
        (-1, '<<LoadData>>', remove_trigger), 
        (-1, '<<SaveData>>', remove_trigger))

active_completion = lambda :AreaVi.ACTIVE.hook('javascript-completion', 
'INSERT', '<Control-Key-period>', lambda event: JavascriptCompletionWindow(
event.widget), add=False)
ENV['active_javascript_completion'] = active_completion

install = JavascriptCompletion



