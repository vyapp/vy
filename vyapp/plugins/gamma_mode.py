"""
Overview
========

The GAMMA mode is an auxiliary mode that should be used by plugins to implement new keycommands.

Key-Commands
============

Namespace: gamma-mode

Mode: <NORMAL>
Event: <Key-5>
Description: Get the AreaVi instance that has focus in GAMMA mode.
"""

def gamma(area):
    area.chmode('GAMMA')

def install(area):
    area.add_mode('GAMMA')
    area.install('gamma-mode', ('NORMAL', '<Key-5>', lambda event: gamma(event.widget)))





