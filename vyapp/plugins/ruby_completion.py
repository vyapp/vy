"""
Overview
========

This module implements ruby autocompletion using the ruby library.


Key-Commands
============

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible ruby words for
completion.
"""

from vyapp.completion import CompletionWindow, Option
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
from subprocess import call
import psutil

class RubyCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, path, port, *args, **kwargs):
        self.path   = path
        self.port   = port
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()

        if not self.is_active(): self.run_server()
        completions = self.completions(source, line, col, area.filename)
        CompletionWindow.__init__(self, area, completions, *args, **kwargs)

    def is_active(self):
        filename = '/tmp/rsense.pid'
        if exists(filename):
            with open(filename, 'r') as fd:
                return psutil.pid_exists(int(fd.read()))

    def run_server(self):
        # When vy is first instantiated it runs the
        # server then leaves it running.
        call([self.path, 'start', '--port', str(self.port)])

    def completions(self, data, line, col, filename):
        payload = {
                    "command": "code_completion",
                    "project": self.get_project_path(filename),
                    "file":filename,
                    "code": data,
                    "location": {"row": line, "column":col + 1},
                  }

        payload = json.dumps(payload)
        addr = 'http://localhost:%s' % self.port
        req  = requests.post(addr, data=payload)
        return self.build(req.text)

    def build(self, data):
        data = json.loads(data)
        return map(lambda ind: Option(ind['name']), data['completions'])

    def get_project_path(self, filename):
        # It is broken. It should be fixed.
        return dirname(filename)

class RubyCompletion(object):
    def __init__(self, area, path='rsense', port=47367):
        self.path = path
        self.port = port
        trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                  lambda event: RubyCompletionWindow(event.widget, self.path, self.port), add=False)

        remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')
        area.install((-1, '<<Load-application/x-ruby>>', trigger),
                     (-1, '<<Save-application/x-ruby>>', trigger), 
                     (-1, '<<LoadData>>', remove_trigger), (-1, '<<SaveData>>', remove_trigger))

install = RubyCompletion



