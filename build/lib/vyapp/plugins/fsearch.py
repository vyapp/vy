"""
Overview
========

Run locate command and drop output on the current AreaVi instance.
The locate comand is run with lax like regex. 

The main difference from  fsniffer it consists of fsearch displaying 
also dirs and being useful with mc plugin.

Key-Commands
============

Namespace: fsearch

Mode: NORMAL
Event: <Key-W>
Description: Insert locale command output in the current AreaVi instance.


Mode: NORMAL
Event: <Control-w>
Description: Ask for a filename pattern to be located using unix locate command.

"""

from vyapp.regutils import build_regex
from subprocess import Popen, STDOUT, PIPE
from vyapp.ask import Get
from vyapp.app import root


class FSearch:
    def __init__(self, area):
        self.area   = area
        self.output = ''

        area.install('fsearch', 
        ('NORMAL', '<Key-W>', self.display),
        ('NORMAL', '<Control-w>',  lambda event: Get(events={
        '<Return>' : self.find, '<<Idle>>': self.update_pattern,
        '<Escape>': lambda wid: True})))

    def display(self, event):
        self.area.swap(self.output, '1.0', 'end')
        root.status.set_msg('Previous located files.')

    def update_pattern(self, wid):
        pattern = build_regex(wid.get(), '.*')
        root.status.set_msg('File pattern: %s' % pattern)

    def run_cmd(self, pattern):
        cmd   = ['locate', '--limit', '200']
        regex = build_regex(pattern, '.*')
        cmd.extend(['--regexp', regex])

        child = Popen(cmd, stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset)

        output = child.communicate()[0]
        return output

    def find(self, wid):
        pattern = wid.get()
        self.output = self.run_cmd(pattern)
        self.area.swap(self.output, '1.0', 'end')
        root.status.set_msg('Locate results: %s' % self.output.count('\n'))
        return True

install = FSearch
