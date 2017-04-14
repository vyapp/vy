"""
Overview
========

This is another auxiliary mode that plugins could use to implement new keycommands.

Key-Commands
============

Namespace: delta-mode

Mode: NORMAL
Event: <Key-6>
Description: Get the AreaVi instance in DELTA mode.
"""

def delta(area):
    area.chmode('DELTA')

def install(area):
    area.add_mode('DELTA')
    area.install('delta-mode', ('NORMAL', '<Key-6>', lambda event: delta(event.widget)))















