"""
Overview
========

This is an auxiliary mode that implements keycommands that aren't often used.

Usage
=====

This mode is implemented in NORMAL mode, in order to switch to ALPHA mode, press
<Escape> to get in NORMAL mode then press <Key-3>.

Key-Commands
============

Mode: NORMAL
Event: <Key-3>
Description: Get the AreaVi instance that is focused in ALPHA mode.
"""

def alpha(area):
    area.chmode('ALPHA')

def install(area):
    area.add_mode('ALPHA')
    area.install(('NORMAL', '<Key-3>', lambda event: alpha(event.widget)))


