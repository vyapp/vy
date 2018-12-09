"""
Overview
========

Offers syntax checking for python with vulture.

Extern dependencies:
    vulture

Key-Commands
============

Namespace: deadcode

Mode: PYTHON
Event: <Key-o>
Description: Highlight all lines
which were reported by vulture.

Commands
========

Command: py_analysis()
Description: Run vulture over the current file and highlighs
all incoherent code. It is possible to jump upwards/downwards
using the same keys as defined in text_spots plugin.

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import exists, dirname, join, relpath
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.tools import get_project_root
from vyapp.app import root
from re import findall
import sys

class PythonAnalysis:
    PATH = 'vulture'

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
    python_analysis = PythonAnalysis(area)
    picker = lambda event: python_analysis.check()

    area.install('deadcode', 
    ('PYTHON', '<Key-o>', picker))

def py_analysis():
    python_analysis = PythonAnalysis(AreaVi.ACTIVE)
    python_analysis.check()

ENV['py_analysis'] = py_analysis


