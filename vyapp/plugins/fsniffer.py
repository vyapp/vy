"""
Overview
========

Quickly open files in vy by using locate command.

Key-Commands
============

Namespace: fsniffer

Mode: NORMAL
Event: <Control-minus>
Description: Ask for a filename pattern to be located using unix locate command.


Mode: INPUT
Event: <Return>
Description: Display possible file matches on a line picker widget. 

"""

from vyapp.regutils import build_regex
from subprocess import Popen, STDOUT, PIPE
from vyapp.widgets import LinePicker
from vyapp.ask import Get
from vyapp.app import root
from os.path import join, basename


class FSniffer(object):
    options = LinePicker()

    wide = False
    def __init__(self, area):
        self.area = area
        area.install('fsniffer', 
        ('NORMAL', '<Key-minus>', lambda e: self.options.display()), 
        ('NORMAL', '<Control-minus>', 
        lambda event: Get(events={'<Return>' : self.find,
        '<Control-w>':self.set_wide, '<<Idle>>': self.update_pattern,
        '<Escape>': lambda wid: True})))
    
    @classmethod
    def set_wide(cls, event):
        FSniffer.wide = False if FSniffer.wide else True
        root.status.set_msg('Set wide search: %s' % FSniffer.wide)

    def update_pattern(self, wid):
        pattern = ' '.join(self.make_cmd(wid.get()))
        root.status.set_msg('Unix locate cmd: %s' % pattern)

    def make_cmd(self, pattern):
        # When FSniffer.wide is False it searches in the current 
        # Areavi instance project.
        cmd   = ['locate', '--limit', '50']
        regex = build_regex(pattern, '.*')

        if self.wide:
            cmd.extend(['--regexp', regex])
        else:
            cmd.extend(['--regexp', '%s.*%s' % (
                self.area.project, regex)])
        return cmd

    def run_cmd(self, pattern):
        cmd   = self.make_cmd(pattern)
        child = Popen(cmd, stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset)

        output = child.communicate()[0]
        return output

    def find(self, wid):
        pattern = wid.get()
        output = self.run_cmd(pattern)
        if output:
            self.fmt_output(output)
        else:
            root.status.set_msg('No results:%s!' % pattern)
        return True

    def fmt_output(self, output):
        output = output.strip('\n').rstrip('\n')
        ranges = output.split('\n')
        ranges = [ind for ind in ranges
            if ranges]

        ranges = [(ind, '0', basename(ind)) for ind in ranges]

        self.options(ranges)

install = FSniffer





