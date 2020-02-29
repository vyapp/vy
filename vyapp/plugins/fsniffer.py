"""
Overview
========

Quickly open files in vy by using locate command.

Key-Commands
============

Namespace: fsniffer

Mode: NORMAL
Event: <Alt-y>
Description: Ask for a filename pattern to be located using unix locate command.


Mode: INPUT
Event: <Alt-t>
Description: Display possible file matches on a line picker widget. 

Mode: INPUT
Event: <Control-w>
Description: Set wide search. In wide search the locate command will
search for files in the whole file system. When an AreaVi instance has 
no project path set then wide search as false will have no efect. 
When wide search is False and project path is set then it searches in the
current file project dirs.

"""

from vyapp.regutils import build_regex
from subprocess import Popen, STDOUT, PIPE
from vyapp.widgets import LinePicker
from vyapp.ask import Get
from vyapp.app import root
from os.path import basename


class FSniffer:
    options = LinePicker()
    wide    = True

    def __init__(self, area):
        self.area = area
        area.install('fsniffer', 
        ('NORMAL', '<Alt-t>', lambda e: self.options.display()), 
        ('NORMAL', '<Alt-y>', lambda event: Get(events={'<Return>' : self.find,
        '<Control-w>':self.set_wide, '<<Idle>>': self.update_pattern,
        '<Escape>': lambda wid: True})))
    
    @classmethod
    def set_wide(cls, event):
        FSniffer.wide = False if FSniffer.wide else True
        root.status.set_msg('Set wide search: %s' % FSniffer.wide)

    def update_pattern(self, wid):
        pattern = build_regex(wid.get(), '.*')
        root.status.set_msg('File pattern: %s' % pattern)

    def make_cmd(self, pattern):
        # When FSniffer.wide is False it searches in the current 
        # Areavi instance project.
        cmd   = ['locate', '--limit', '200']
        regex = build_regex(pattern, '.*')

        if self.wide or not self.area.project:
            cmd.extend(['--regexp', regex])
        else:
            cmd.extend(['--regexp', '%s.*%s' % (
                self.area.project, regex)])

        # Used to filter only files because locate doesn't support 
        # searching only for files.
        cmd = '%s | %s' % (' '.join(cmd), '''while read -r file; do
          [ -d "$file" ] || printf '%s\n' "$file"; done''')
        return cmd

    def run_cmd(self, pattern):
        cmd   = self.make_cmd(pattern)
        child = Popen(cmd, stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset, shell=True)

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






