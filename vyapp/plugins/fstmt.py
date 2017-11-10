"""
Overview
========

Find where patterns are found, this plugin uses ack to search
for word patterns. It is useful to find where functions/methods
are used over multiple files.

Key-Commands
============

Namespace: fstmt

Mode: NORMAL
Event: <Control-backslash>
Description: Get a text pattern and perform a search.

Mode: NORMAL
Event: <Key-backslash>
Description: Open the previous found pattern occurrences.

Mode: NORMAL
Event: <Key-bar>
Description: Perform a search pattern in a root directory
that can be defined manually.  If it is not defined manually then 
it searches for the project root that contains a .git or .svn or .hg folder. 
The search pattern is defined either by the word under the cursor or by 
a range of selected text. If there is any selected text then it is used for the search
otherwise it gets the word under the cursor then perform the search.

"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from re import findall, escape
from vyapp.app import root
from vyapp.ask import Ask
from os.path import join

class Fstmt(object):
    options   = LinePicker()
    PATH      = 'ack'

    def  __init__(self, area):
        self.area    = area

        area.install('fstmt', 
        ('NORMAL', '<Key-backslash>', 
        lambda event: self.options.display()),
        ('NORMAL', '<Control-bar>', 
        lambda event: self.set_pattern()),
        ('NORMAL', '<Key-bar>', 
        lambda event: self.catch_pattern()))

    def set_pattern(self):
        root.status.set_msg('Set fstmt pattern!')
        ask = Ask()
        self.picker(escape(ask.data))
        
    def catch_pattern(self):
        pattern = self.area.join_ranges('sel')
        pattern = pattern if pattern else self.area.get_word()
        pattern = escape(pattern)

        if not pattern:
            root.status.set_msg('No pattern set!')
        else:
            self.picker(pattern)

    def make_cmd(self, pattern, dir):
        return [Fstmt.PATH, '--nocolor', '-H', '--column',
        '--nogroup', pattern, dir]

    def run_cmd(self, pattern, dir):
        child = Popen(self.make_cmd(pattern, dir), stdout=PIPE, 
        stderr=STDOUT, encoding=self.area.charset)
        return child.communicate()[0]

    def picker(self, pattern):
        dir    = self.area.project
        dir    = dir if dir else AreaVi.HOME
        dir    = dir if dir else self.area.filename
        output = self.run_cmd(pattern, dir)
        regex  = '(.+):([0-9]+):[0-9]+:(.+)' 
        ranges = findall(regex, output)
        if ranges:
            self.options(ranges)
        else:
            root.status.set_msg('No pattern found!')

class FstmtSilver(Fstmt):
    PATH = 'ag'
    def make_cmd(self, pattern, dir):
        return [FstmtSilver.PATH, '--nocolor', '--nogroup', '--vimgrep', 
            '--noheading', pattern, dir]



