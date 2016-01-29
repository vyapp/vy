"""
Overview
========

This module implements the NORMAL mode that is the mode in which most
editing keycommands are implemented.

Usage
=====

When <Escape> is pressed regardless of the AreaVi instance mode then the focused AreaVi instance
mode will be changed to NORMAL mode. The <Escape> keycommand is implemented in global mode.

Key-Commands
============

Mode: -1
Event: <Escape>
Description: Get the focused AreaVi instance in NORMAL mode.
"""

def install(area):
    area.add_mode('NORMAL')
    area.chmode('NORMAL')
    area.install((-1, '<Escape>', lambda event: area.chmode('NORMAL')))




