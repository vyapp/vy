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
Description: 

Mode: NORMAL
Event: <Key-backslash>
Description: 

Mode: NORMAL
Event: <Key-bar>
Description: 

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import exists, dirname, join
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.app import root
from vyapp.ask import Ask
from re import findall
import sys

def get_sentinel_file(path, filename):
    """
    """

    tmp = path
    while True:
        tmp = dirname(tmp)
        if exists(join(tmp, filename)):
            return tmp
        elif tmp == dirname(tmp):
            return path
        path = tmp

class Fstmt(object):
    pattern = ''
    dir     = ''
    options = LinePicker()

    def  __init__(self, area):
        self.area    = area

        area.install('fstmt', 
        ('NORMAL', '<Key-backslash>', 
        lambda event: self.find()),
        ('NORMAL', '<Control-bar>', 
        lambda event: self.set_dir()),
        ('NORMAL', '<Key-bar>', 
        lambda event: self.catch_pattern()))

    def set_dir(self):
        root.status.set_msg('Set fstmt search path!')
        ask       = Ask()
        Fstmt.dir = ask.data
   
    def catch_pattern(self):
        pattern = self.area.join_ranges('sel')
        pattern = pattern if pattern else self.area.get_word()
        Fstmt.pattern = pattern

        if not Fstmt.pattern:
            root.status.set_msg('No pattern found!')
        else:
            self.picker()

    def find(self):
        if Fstmt.pattern:
            self.options.display()
        else:
            root.status.set_msg('No pattern set!')

    def picker(self):
        dir = self.dir if Fstmt.dir else \
        get_sentinel_file(self.area.filename, '.git')

        child = Popen(['ack', '--nogroup', self.pattern, dir],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]
        regex  = '(.+):([0-9]+):(.+)' 
        ranges = findall(regex, output)
    
        if ranges:
            self.options(ranges)

install = Fstmt


