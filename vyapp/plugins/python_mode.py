"""
Overview
========

Extra mode for python programming language.

Key-Commands
============

Namespace: python-mode

Mode: NORMAL
Event: <Key-exclam>
Description: Switch to PYTHON mode.
"""

from vyapp.plugins import Namespace

class PythonModeNS(Namespace):
    pass

class PythonMode:
    def __init__(self, area):
        self.area = area
        area.add_mode('PYTHON')
        area.install(PythonModeNS, 
        ('NORMAL', '<Key-exclam>', self.python_mode))

    def python_mode(self, event):
        self.area.chmode('PYTHON')

install = PythonMode

