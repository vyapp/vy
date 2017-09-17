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

def python_mode(area):
    area.chmode('PYTHON')

def install(area):
    area.add_mode('PYTHON')
    area.install('python-mode', ('NORMAL', '<Key-exclam>', 
    lambda event: python_mode(area)))



















