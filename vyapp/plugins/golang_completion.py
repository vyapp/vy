"""
Overview
========

This module implements golang autocompletion using the gocode
daemon.

Key-Commands
============

Namespace: golang-completion

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible golang words for
completion.
"""

from vyapp.completion import CompletionWindow, Option
from os.path import expanduser, join, exists, dirname
from subprocess import call, check_output
from vyapp.areavi import AreaVi
from subprocess import Popen, PIPE
from os import getcwd
from shutil import copyfile
from vyapp.plugins import ENV
import mimetypes
import psutil
import sys
import json

class GolangCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, path, *args, **kwargs):
        self.area = area
        self.path = path
        tmp0      = area.get('1.0', 'insert')
        tmp1      = area.get('insert', 'end')
        source    = tmp0 + tmp1
        offset    = len(tmp0)
        print 'testt'

        completions = self.completions(source, offset, area.filename)
        CompletionWindow.__init__(self, area, completions, *args, **kwargs)

    def completions(self, data, offset, filename):
        daemon = Popen('%s -f=json --in=%s autocomplete %s' % (self.path,
        self.area.filename, offset), shell=1, stdin=PIPE, stdout=PIPE, stderr=PIPE)

        stdout, stderr = daemon.communicate(data)
        return self.build(stdout)

    def build(self, data):
        data = json.loads(data)
        return map(lambda ind: Option(ind['name']), data['type'], data[1])

class GolangCompletion(object):
    PATH = 'gocode'

    def __init__(self, area, path):
        self.path = path
        trigger = lambda event: area.hook('golang-completion', 'INSERT', '<Control-Key-period>', 
                  lambda event: GolangCompletionWindow(event.widget, self.path), add=False)

        remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')
        area.install('golang-completion', (-1, '<<Load-application/x-golang>>', trigger),
                     (-1, '<<Save-application/x-golang>>', trigger), 
                     (-1, '<<LoadData>>', remove_trigger), (-1, '<<SaveData>>', remove_trigger))

mimetypes.add_type('application/x-golang', '.go')
install = GolangCompletion





