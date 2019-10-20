"""
Overview
========

Run static typer checker on code.

Extern dependencies:
    mypy

Key-Commands
============

Namespace: snakerr

Mode: PYTHON
Event: <Key-F>
Description: Highlight all lines
with syntax errors. 

Commands
========

Command: py_static()

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import exists, dirname, join, relpath
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.tools import get_project_root
from vyapp.plugins import ENV
from vyapp.app import root
from vyapp.base import printd
from re import findall
import sys

class StaticChecker(object):
    options = LinePicker()
    path    = 'mypy'

    def  __init__(self, area):
        self.area = area
        area.install('snakerr', ('PYTHON', '<Control-t>', self.check_module),
        ('PYTHON', '<Key-t>', lambda event: self.options.display()),
        ('PYTHON', '<Key-T>', self.check_all))

    @classmethod
    def c_path(cls, path):
        printd('Snakerr - Setting Mypy path = ', cls.path)
        cls.path = path

    def check_all(self, event):
        path  = get_project_root(self.area.filename)
        child = Popen([self.path,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(.+?):([0-9]+):(.+)' 
        ranges = findall(regex, output)

        sys.stdout.write('Mypy errors: \n%s\n' % output)
        self.area.chmode('NORMAL')

        root.status.set_msg('Mypy errors: %s' % len(ranges))
        if ranges:
            self.options(ranges)

    def check_module(self, event):
        path  = get_project_root(self.area.filename)
        child = Popen([self.path,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(%s):([0-9]+):(.+)' % relpath(self.area.filename)
        ranges = findall(regex, output)
        sys.stdout.write('Mypy errors: \n%s\n' % output)
        self.area.chmode('NORMAL')

        root.status.set_msg('Mypy errors: %s' % len(ranges))
        if ranges:
            self.options(ranges)


install = StaticChecker
def py_static():
    checker = StaticChecker(AreaVi.ACTIVE)
    checker.check()

ENV['py_static'] = py_static


