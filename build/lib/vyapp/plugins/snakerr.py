"""
Overview
========

Offers syntax checking for python with pyflakes.

Extern dependencies:
    pyflakes

Key-Commands
============

Namespace: snakerr

Mode: PYTHON
Event: <Key-h>
Description: Show previous Pyflakes reports.

Mode: PYTHON
Event: <Control-h>
Description: Run Pyflakes on the current file.
with syntax errors. 

Mode: PYTHON
Event: <Key-H>
Description:  Run Pyflakes on the whole current file project.

Commands
========

Command: py_errors()
Description: Run pyflakes over the current file and highlighs
all lines with errors. It is possible to jump upwards/downwards
using the same keys as defined in text_spots plugin.

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import relpath
from vyapp.widgets import LinePicker
from vyapp.plugins import Command
from vyapp.tools import get_project_root
from vyapp.app import root
from vyapp.stderr import printd
from re import findall
import sys

class PythonChecker:
    options = LinePicker()
    path    = 'pyflakes'

    def  __init__(self, area):
        self.area = area
        area.install('snakerr', ('PYTHON', '<Control-h>', self.check_module),
        ('PYTHON', '<Key-h>', self.display_errors),
        ('PYTHON', '<Key-H>', self.check_all))

    @classmethod
    def c_path(cls, path):
        printd('Snakerr - Setting Pyflakes path = ', cls.path)
        cls.path = path

    def display_errors(self, event=None):
        root.status.set_msg('Pyflakes previous errors!')
        self.options.display()
        self.area.chmode('NORMAL')

    def check_all(self, event=None):
        path  = get_project_root(self.area.filename)
        child = Popen([self.path,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        # Pyflakes omit the column attribute when there are
        # syntax errors thus the (.+?) in the beggining of the
        # regex is necessary.
        regex  = '(.+?):([0-9]+):?[0-9]*:(.+)' 
        ranges = findall(regex, output)

        sys.stdout.write('Pyflakes found global errors:\n%s\n' % output)
        self.area.chmode('NORMAL')
        root.status.set_msg('Pyflakes errors: %s' % len(ranges))

        if ranges:
            self.options(ranges)

    def check_module(self, event=None):
        path  = get_project_root(self.area.filename)
        child = Popen([self.path,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(%s):([0-9]+):?[0-9]*:(.+)' % relpath(self.area.filename)
        ranges = findall(regex, output)
        sys.stdout.write('Errors:\n%s\n' % output)
        self.area.chmode('NORMAL')
        root.status.set_msg('Pyflakes errors: %s' % len(ranges))

        if ranges:
            self.options(ranges)
        
@Command()
def py_errors(area):
    python_checker = PythonChecker(area)
    python_checker.check_all()

install = PythonChecker

