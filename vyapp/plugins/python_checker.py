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

Mode: BETA
Event: <Key-h>
Description: Highlight all lines
with syntax errors. The checking functionality gets
available for files ending in ".py" extension.

Commands
========

Command: py_errors()
Description: When the file has no extension, this command can be
used to highligh the errors.

"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.app import root
from re import findall
import sys

class PythonChecker(object):
    PATH = 'pyflakes'

    def  __init__(self, area):
        self.area = area

    def check(self):
        child  = Popen([self.PATH,  self.area.filename], 
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]

        regex  = '(.+?):([0-9]+):?([0-9]*):(.+)'
        ranges = findall(regex, output)
        sys.stdout.write('Errors:\n%s\n' % output)
        self.area.reset_assoc_data()

        for filename, line, col, error in ranges:
            self.assoc_msg(line, error)

        if child.returncode:
            root.status.set_msg('Errors were found!')
        else:
            root.status.set_msg('No errors!')
        self.area.chmode('NORMAL')
        
    def assoc_msg(self, line, error):
        index0 = '%s.0' % line, 
        index1 = '%s.0 lineend' % line

        self.area.tag_add('(SPOT)', index0, index1)
        self.area.set_assoc_data(index0, index1, error)

def install(area):
    python_checker = PythonChecker(area)
    picker = lambda event: python_checker.check()

    area.install('python-checker', (-1, '<<Load/*.py>>', lambda event: 
    area.hook('python-checker', 'BETA', '<Key-h>', picker)),
    (-1, '<<LoadData>>', lambda event: 
    area.unhook('BETA', '<Key-h>')),
    (-1, '<<Save/*.py>>', lambda event: 
    area.hook('python-checker', 'BETA', '<Key-h>', picker)),
    (-1, '<<SaveData>>', lambda event: 
    area.unhook('BETA', '<Key-h>')))
    
def py_errors():
    python_checker = PythonChecker(AreaVi.ACTIVE)
    python_checker.check()

ENV['py_errors'] = py_errors




