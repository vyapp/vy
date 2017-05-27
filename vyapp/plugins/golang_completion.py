"""
Overview
========

This module implements golang autocompletion using the gocode
daemon.

Github: https://github.com/nsf/gocode

Key-Commands
============

Namespace: golang-completion

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible golang words for
completion.
"""

from vyapp.completion import CompletionWindow, Option
from subprocess import Popen, PIPE
import json
import sys

class GolangCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area,  *args, **kwargs):
        self.area = area
        tmp0      = area.get('1.0', 'insert')
        tmp1      = area.get('insert', 'end')
        source    = tmp0 + tmp1
        offset    = len(tmp0) 

        completions = self.completions(source, offset, area.filename)
        CompletionWindow.__init__(self, area, completions, *args, **kwargs)

        self.bind('<F1>', lambda event: sys.stdout.write('%s\n%s\n' % (
        '#' * 80, self.box.selection_docs())))

    def completions(self, data, offset, filename):
        daemon = Popen('%s -f=json autocomplete %s %s' % (GolangCompletion.PATH,
        self.area.filename, offset), shell=1, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = daemon.communicate(data)

        return self.build(stdout)

    def build(self, data):
        data = json.loads(data)
        return map(lambda ind: Option(ind['name'], 'Type:%s' % ind['type'], 
        'Class:%s' % ind['class']), data[1])

class GolangCompletion(object):
    PATH = 'gocode'

    def __init__(self, area):
        trigger = lambda event: area.hook('golang-completion', 'INSERT', '<Control-Key-period>', 
                  lambda event: GolangCompletionWindow(event.widget), add=False)

        remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')
        area.install('golang-completion', (-1, '<<Load/*.go>>', trigger),
        (-1, '<<Save/*.go>>', trigger),  (-1, '<<LoadData>>', remove_trigger), 
        (-1, '<<SaveData>>', remove_trigger))

install = GolangCompletion








