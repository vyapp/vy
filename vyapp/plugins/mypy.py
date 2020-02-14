"""
Overview
========

Run static typer checker on your project files. It uses mypy.

Extern dependencies:
    http://mypy-lang.org/

Key-Commands
============

Namespace: mypy

Mode: PYTHON
Event: <Key-h>
Description: Show previous Mypy reports.

Mode: PYTHON
Event: <Control-t>
Description: Run Mypy on the current file.
with syntax errors. 

Mode: PYTHON
Event: <Key-T>
Description:  Run Mypy on the whole current file project.

Commands
========

Command: py_static()

"""

from vyapp.plugins import Command
from subprocess import Popen, STDOUT, PIPE
from os.path import relpath
from vyapp.widgets import LinePicker
from vyapp.tools import get_project_root
from vyapp.app import root
from vyapp.base import printd
from re import findall
import sys

class StaticChecker:
    options = LinePicker()
    path    = 'mypy'

    def  __init__(self, area):
        self.area = area
        area.install('mypy', ('PYTHON', '<Control-t>', self.check_module),
        ('PYTHON', '<Key-t>', lambda event: self.options.display()),
        ('PYTHON', '<Key-T>', self.check_all))

    @classmethod
    def c_path(cls, path):
        printd('Snakerr - Setting Mypy path = ', cls.path)
        cls.path = path

    def check_all(self, event=None):
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

    def check_module(self, event=None):
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
@Command()
def py_static(area):
    checker = StaticChecker(area)
    checker.check_all()
