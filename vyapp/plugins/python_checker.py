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

Namespace: python-checker

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
from vyapp.plugins import ENV
from vyapp.app import root
from re import findall
import sys

def get_project_root(path):
    """
    Return the project root or the file path.
    """

    # In case it receives '/file'
    # and there is '/__init__.py' file.
    if path == dirname(path):
        return path

    while True:
        tmp = dirname(path)
        if not exists(join(tmp, '__init__.py')):
            return path
        path = tmp

class PythonChecker(object):
    PATH = 'pyflakes'

    def  __init__(self, area):
        self.area = area

    def check(self):
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
        root.status.set_msg('Errors were found!' )
        options = LinePicker()
        options(ranges)

def install(area):
    python_checker = PythonChecker(area)
    picker = lambda event: python_checker.check()

    area.install('python-checker', 
    ('PYTHON', '<Key-h>', picker))

def py_errors():
    python_checker = PythonChecker(AreaVi.ACTIVE)
    python_checker.check()

ENV['py_errors'] = py_errors



