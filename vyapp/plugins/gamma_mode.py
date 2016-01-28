"""
Overview
========

The GAMMA mode is an auxiliary mode that should be used by plugins to implement new keycommands.

Usage
=====

In order to get the focused AreaVi instance in GAMMA mode, switch to NORMAL mode then press 
<Key-5>.

Key-Commands
============

Mode: <NORMAL>
Event: <Key-5>
Description: Get the AreaVi instance that has focus in GAMMA mode.
"""

def gamma(area):
    area.chmode('GAMMA')

def install(area):
    area.add_mode('GAMMA')
    area.install(('NORMAL', '<Key-5>', lambda event: gamma(event.widget)))


