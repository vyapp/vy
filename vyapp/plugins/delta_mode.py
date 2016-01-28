"""
Overview
========

This is another auxiliary mode that plugins could use to implement new keycommands.

Usage
=====

In order to get in DELTA mode, switch to NORMAL mode then press <Key-6>

Key-Commands
============

Mode: NORMAL
Event: <Key-6>
Description: Get the AreaVi instance in DELTA mode.
"""

def delta(area):
    area.chmode('DELTA')

def install(area):
    area.add_mode('DELTA')
    area.install(('NORMAL', '<Key-6>', lambda event: delta(event.widget)))












