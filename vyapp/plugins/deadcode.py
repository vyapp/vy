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
Description: Highlight all lines which were reported 
by vulture on the current file.

Mode: PYTHON
Event: <Key-O>
Description: Highlight all lines which were reported 
by vulture on all files.

Commands
========

Command: py_analysis()
Description: Run vulture over the current file and highlighs
all incoherent code. It is possible to jump upwards/downwards
using the same keys as defined in text_spots plugin.

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import relpath
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
        area.install('deadcode', ('PYTHON', '<Key-o>', self.check_module),
        ('PYTHON', '<Key-O>', self.check_all))
    
    def check_all(self, event):
        output = self.run_cmd(self.area.filename)
        regex  = '(.+):([0-9]+):?[0-9]*:(.+)' 
        ranges = findall(regex, output)
        sys.stdout.write('Global errors:\n%s\n' % output)
        self.area.chmode('NORMAL')

        if ranges:
            self.display(ranges)
        else:
            root.status.set_msg('No errors!')

    def run_cmd(self, filename):
        path  = get_project_root(filename)
        child = Popen([self.PATH,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]
        return output

    def check_module(self, event):
        output = self.run_cmd(self.area.filename)
        regex  = '(%s):([0-9]+):?[0-9]*:(.+)' % relpath(self.area.filename)
        ranges = findall(regex, output)

        sys.stdout.write('%s errors:\n%s\n' % (self.area.filename, output))
        self.area.chmode('NORMAL')

        if ranges:
            self.display(ranges)
        else:
            root.status.set_msg('No errors!')
        
    def display(self, ranges):
        root.status.set_msg('Errors were found!' )
        options = LinePicker()
        options(ranges)

install = PythonAnalysis

def py_analysis():
    python_analysis = PythonAnalysis(AreaVi.ACTIVE)
    python_analysis.check()
ENV['py_analysis'] = py_analysis

