"""
Overview
========

Offers syntax checking for python with pyflakes.

Plugin dependencies: 
    vyapp.plugins.text_spots

Extern dependencies:
    pyflakes

Key-Commands
============

Namespace: snakerr

Mode: PYTHON
Event: <Key-h>
Description: Highlight all lines
with syntax errors. 

Commands
========

Command: py_errors()
Description: Run pyflakes over the current file and highlighs
all lines with errors. It is possible to jump upwards/downwards
using the same keys as defined in text_spots plugin.

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import exists, dirname, join, relpath
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.tools import get_project_root
from vyapp.plugins import ENV
from vyapp.app import root
from re import findall
import sys

class PythonChecker(object):
    PATH = 'pyflakes'

    def  __init__(self, area):
        self.area = area
        area.install('snakerr', ('PYTHON', '<Key-h>', self.check_module),
        ('PYTHON', '<Key-H>', self.check_all))

    def check_all(self, event):
        path  = get_project_root(self.area.filename)
        child = Popen([self.PATH,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        # Pyflakes omit the column attribute when there are
        # syntax errors thus the (.+?) in the beggining of the
        # regex is necessary.
        regex  = '(.+?):([0-9]+):?[0-9]*:(.+)' 
        ranges = findall(regex, output)

        sys.stdout.write('Pyflakes found global errors:\n%s\n' % output)
        self.area.chmode('NORMAL')

        if ranges:
            self.display(ranges)
        else:
            root.status.set_msg('No errors!')

    def check_module(self, event):
        path  = get_project_root(self.area.filename)
        child = Popen([self.PATH,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(%s):([0-9]+):?[0-9]*:(.+)' % relpath(self.area.filename)
        ranges = findall(regex, output)
        sys.stdout.write('Errors:\n%s\n' % output)
        self.area.chmode('NORMAL')

        if ranges:
            self.display(ranges)
        else:
            root.status.set_msg('No errors!')
        
    def display(self, ranges):
        root.status.set_msg('Pyflakes found errors!' )
        options = LinePicker()
        options(ranges)

install = PythonChecker
def py_errors():
    python_checker = PythonChecker(AreaVi.ACTIVE)
    python_checker.check()

ENV['py_errors'] = py_errors

