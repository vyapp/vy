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


Mode: PYTHON
Event: <Key-o>
Description: Show previous Vulture reports.

Event: <Control-o>
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

from vyapp.plugins import Command
from subprocess import Popen, STDOUT, PIPE
from os.path import relpath
from vyapp.widgets import LinePicker
from vyapp.tools import get_project_root
from vyapp.base import printd
from vyapp.app import root
from re import findall
import sys

class PythonAnalysis:
    options = LinePicker()
    path    = 'vulture'

    def  __init__(self, area):
        self.area = area
        area.install('deadcode', ('PYTHON', '<Control-o>', self.check_module),
        ('PYTHON', '<Key-o>', lambda event: self.options.display()),
        ('PYTHON', '<Key-O>', self.check_all))

    @classmethod
    def c_path(cls, path):
        printd('Deadcode - Setting Vulture path = ', cls.path)
        cls.path = path
    
    def check_all(self, event=None):
        path  = get_project_root(self.area.filename)
        child = Popen([self.path,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(.+):([0-9]+):?[0-9]*:(.+)' 
        ranges = findall(regex, output)
        sys.stdout.write('Vulture found global errors:\n%s\n' % output)
        self.area.chmode('NORMAL')

        root.status.set_msg('Vulture errors: %s' % len(ranges))
        if ranges:
            self.options(ranges)

    def check_module(self, event=None):
        path  = get_project_root(self.area.filename)
        child = Popen([self.path,  path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(%s):([0-9]+):?[0-9]*:(.+)' % relpath(self.area.filename)
        ranges = findall(regex, output)

        sys.stdout.write('%s errors:\n%s\n' % (self.area.filename, output))
        self.area.chmode('NORMAL')

        root.status.set_msg('Vulture errors: %s' % len(ranges))
        if ranges:
            self.options(ranges)
        
install = PythonAnalysis
@Command()
def py_analysis(area):
    python_analysis = PythonAnalysis(area)
    python_analysis.check_all()

