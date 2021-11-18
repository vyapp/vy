"""
Overview
========

Extra mode for cplusplus programming language.

Key-Commands
============

Namespace: cplusplus-mode

Mode: NORMAL
Event: <Key-exclam>
Description: Switch to C++ mode.
"""

def cplusplus_mode(area):
    area.chmode('C++')

def install(area):
    area.add_mode('C++')
    area.install('cplusplus-mode', ('NORMAL', '<Key-ampersand>', 
    lambda event: cplusplus_mode(area)))



