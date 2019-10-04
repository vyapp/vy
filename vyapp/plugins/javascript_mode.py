"""
Overview
========

Extra mode for javascript programming language.

Key-Commands
============

Namespace: javascript-mode

Mode: NORMAL
Event: <Key-exclam>
Description: Switch to PYTHON mode.
"""

def javascript_mode(area):
    area.chmode('JAVASCRIPT')

def install(area):
    area.add_mode('JAVASCRIPT')
    area.install('javascript-mode', ('NORMAL', '<Key-percent>', 
    lambda event: javascript_mode(area)))


