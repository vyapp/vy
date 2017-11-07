"""
Overview
========

Used to find snippets accross folders.

Key-Commands
============


"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.regutils import build_regex
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.app import root
from vyapp.ask import Ask
from re import findall

class Fsnip:
    options = LinePicker()
    FOLDERS = []
    PATH   = 'ag'
    def  __init__(self, area):
        self.area = area
        area.install('fsnip', 
        (-1, '<Key-b>', lambda event: self.options.display()),
        (-1, '<Key-B>', self.find))

    def find(self, event):
        """
        """

        root.status.set_msg('Set fsnip pattern!')
        ask     = Ask()
        pattern = build_regex(ask.data)
        dirs    = ' '.join(self.FOLDERS)
        child   = Popen([self.PATH, '--nocolor', '--nogroup', 
        '--vimgrep', '--noheading', pattern, dirs], stdout=PIPE, 
        stderr=STDOUT, encoding=self.area.charset)

        output =  child.communicate()[0]
        regex  = '(.+):([0-9]+):[0-9]+:(.+)' 
        ranges = findall(regex, output)
        if ranges:
            self.options(ranges)
        else:
            root.status.set_msg('No results:%s!' % pattern)

install = Fsnip

