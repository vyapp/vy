from vyapp.complete import CompleteWindow
from subprocess import Popen
import json
import requests
import sys
import os
import atexit

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
        with open(os.path.join(os.getcwd(), '.tern-port'), 'r') as fd:
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

