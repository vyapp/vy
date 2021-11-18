"""
Overview
========

This module implements javascript autocompletion using the tern javascript library.


Key-Commands
============

Namespace: ternjs

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.
"""

from vyapp.completion import CompletionWindow, Option
from os.path import expanduser, join, exists, dirname
from vyapp.plugins import Command
from subprocess import Popen, PIPE
from shutil import copyfile
import json
import requests
import sys
import atexit

filename = join(expanduser('~'), '.tern-config')
if not exists(filename): 
    copyfile(join(dirname(__file__), 'tern-config'), filename)

class JavascriptCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        # If ~/.tern-port doesn't exist then run the server.
        source      = area.get('1.0', 'end')
        line, col   = area.indexsplit()

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
        return [Option(**ind) for ind in data['completions']]

class JavascriptCompletion:
    PATH = 'tern'
    PORT = 1234

    def __init__(self, area):
        trigger = lambda event: area.hook('ternjs', 'INSERT', 
        '<Control-Key-period>', lambda event: JavascriptCompletionWindow(
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

install = JavascriptCompletion
@Command()
def acj(area):
    area.hook('javascript-completion', 'INSERT', '<Control-Key-period>', 
    lambda event: JavascriptCompletionWindow(event.widget), add=False)


