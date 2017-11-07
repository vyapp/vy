"""
Overview
========

Offers syntax checking for python with vulture.

Plugin dependencies: 
    vyapp.plugins.text_spots
    vyapp.plugins.python_checker

Extern dependencies:
    vulture

Key-Commands
============

Namespace: python-analysis

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

from vyapp.plugins import ENV
from vyapp.plugins.python_checker import PythonChecker
from vyapp.app import root

class PythonAnalysis(PythonChecker):
    PATH = 'vulture'

def install(area):
    python_analysis = PythonAnalysis(area)
    picker = lambda event: python_analysis.check()

    area.install('python-analysis', 
    ('PYTHON', '<Key-o>', picker))

def py_analysis():
    python_analysis = PythonAnalysis(AreaVi.ACTIVE)
    python_analysis.check()

ENV['py_analysis'] = py_analysis







