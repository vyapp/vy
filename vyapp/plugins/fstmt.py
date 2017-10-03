"""
Overview
========

Key-Commands
============

Namespace: fstmt

Mode: NORMAL
Event: 
Description: 

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import exists, dirname, join, relpath
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.app import root
from vyapp.ask import Ask
from re import findall
import sys

class Fstmt(object):
    def  __init__(self, area):
        area.install('fstmt', 
        ('NORMAL', '<Key-b>', lambda event: self.picker()),
        ('NORMAL', '<Key-B>', lambda event: self.set_search_path()))
        self.area = area
        self.search_path = None

    def set_search_path(self):
        ask              = Ask()
        self.search_path = ask.data
   
    def picker(self):
        pattern = self.area.join_ranges('sel')

        child   = Popen(['ack', '--nogroup', pattern, self.search_path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(.+):([0-9]+):(.+)' 
        ranges = findall(regex, output)

        # print(ranges)

        for filename, line, col, msg in ranges:
            pass

install = Fstmt




