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
from tkinter import Toplevel, Listbox, BOTH, END, TOP, SINGLE
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.app import root
from vyapp.ask import Ask
from re import findall
import sys

# def get_project_root(path):
    # # In case it receives '/file'
    # # and there is '/__init__.py' file.
    # if path == dirname(path):
        # return path
# 
    # while True:
        # tmp = dirname(path)
        # if not exists(join(tmp, '.git')):
            # return path
        # path = tmp

class OptionWindow(Toplevel):
    def  __init__(self, area, options):
        Toplevel.__init__(self, master=root)
        self.title('Matches')

        self.listbox = Listbox(master=self, selectmode=SINGLE)

        for filename, line, msg in options:
            self.listbox.insert(END, '%s - %s %s' % (filename, line, msg))

        self.listbox.pack(expand=True, fill=BOTH, side=TOP)
        self.listbox.focus_set()
        self.listbox.config(width=50)
        self.transient(root)
        self.grab_set()
        self.wait_window(self)

class Fstmt(object):
    def  __init__(self, area):
        area.install('fstmt', 
        ('NORMAL', '<Key-backslash>', lambda event: self.picker()),
        ('NORMAL', '<Key-B>', lambda event: self.set_search_path()))
        self.area = area
        # self.search_path = '/home/tau/projects/vy-code'

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

        if ranges:
            OptionWindow(self.area, ranges)

install = Fstmt





