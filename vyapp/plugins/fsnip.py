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
from vyapp.ask import Get
from re import findall

class Fsnip:
    options = LinePicker()
    FOLDERS = []
    PATH   = 'ag'
    fptr   = ''
    def  __init__(self, area):
        self.area = area
        area.install('fsnip', 
        ('NORMAL', '<Key-b>', lambda event: self.options.display()),
        ('NORMAL', '<Key-B>', lambda event: Get(events = {
        '<Return>':self.find, 
        '<Control-g>':self.set_file_pattern, 
        '<Escape>':  lambda wid: True})))

    def set_file_pattern(self, wid):
        self.fptr = build_regex(wid.get())
        root.status.set_msg('Set file pattern:%s' % self.fptr)
        wid.delete(0, 'end')

    def find(self, wid):
        """
        """

        root.status.set_msg('Set fsnip pattern!')
        pattern = build_regex(wid.get())
        dirs    = ' '.join(self.FOLDERS)
        child   = Popen([self.PATH, '--nocolor', '--nogroup', '-G', self.fptr,
        '--vimgrep', '--noheading', pattern, dirs], stdout=PIPE, 
        stderr=STDOUT, encoding=self.area.charset)

        output =  child.communicate()[0]
        regex  = '(.+):([0-9]+):[0-9]+:(.+)' 
        ranges = findall(regex, output)
        if ranges:
            self.options(ranges)
        else:
            root.status.set_msg('No results:%s!' % pattern)
        return True

install = Fsnip


