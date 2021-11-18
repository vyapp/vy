"""
Overview
========

Extra mode for c programming language.

Key-Commands
============

Namespace: c-mode

Mode: NORMAL
Event: <Key-exclam>
Description: Switch to C mode.
"""

def c_mode(area):
    area.chmode('C')

def install(area):
    area.add_mode('C')
    area.install('c-mode', ('NORMAL', '<Key-dollar>', 
    lambda event: c_mode(area)))


