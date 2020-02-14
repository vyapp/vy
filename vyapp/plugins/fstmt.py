"""
Overview
========

Find where patterns are found, this plugin uses silver searcher to search
for word patterns. It is useful to find where functions/methods
are used over multiple files.


Key-Commands
============

Namespace: fstmt

Mode: NORMAL
Event: <Control-z>
Description: Same as <Key-bar> but matches insensitively.

Mode: NORMAL
Event: <Key-z>
Description: Open the previous found pattern occurrences.

Mode: NORMAL
Event: <Key-Z>
Description: Get the string under the cursor and perform
a case sensitive and resursive search in the current project file directory.
It grabs the string under the cursor only if there is no selected text. 

The search is performed in the current project folder, if fstmt cant find a .git, svn
nor .hg it performs the search in the vy HOME directory.

"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from re import findall, escape
from vyapp.base import printd
from vyapp.app import root

class Fstmt:
    options = LinePicker()
    path    = 'ag'

    def  __init__(self, area):
        self.area    = area

        area.install('fstmt', 
        ('NORMAL', '<Key-z>', lambda event: self.options.display()),
        ('NORMAL', '<Control-z>', lambda event: self.picker('-i')),
        ('NORMAL', '<Key-Z>', lambda event: self.picker('-s')))

    @classmethod
    def c_path(cls, path='ag'):
        cls.path = path
        printd('Fstmt - Setting ag path = ', path)

    def catch_pattern(self):
        pattern = self.area.join_ranges('sel')
        pattern = pattern if pattern else self.area.get(
        *self.area.get_word_range())

        pattern = escape(pattern)
        return pattern

    def make_cmd(self, pattern, dir, *args):
        cmd =  [Fstmt.path, '--nocolor', '--nogroup', 
        '--vimgrep', '--noheading']
        cmd.extend(args)
        cmd.extend([pattern, dir])
        return cmd

    def run_cmd(self, pattern, *args):
        dir    = self.area.project
        dir    = dir if dir else AreaVi.HOME
        dir    = dir if dir else self.area.filename
        child  = Popen(self.make_cmd(pattern, dir, *args), stdout=PIPE, 
        stderr=STDOUT, encoding=self.area.charset)
        regex  = '(.+):([0-9]+):[0-9]+:(.+)' 
        ranges = findall(regex, child.communicate()[0])

        if ranges:
            self.options(ranges)
        else:
            root.status.set_msg('No pattern found!')

    def picker(self, *args):
        pattern = self.catch_pattern()
        if not pattern:
            root.status.set_msg('No pattern set!')
        else:
            self.run_cmd(pattern, *args)


