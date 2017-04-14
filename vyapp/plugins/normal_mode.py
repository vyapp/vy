"""
Overview
========

This module implements the NORMAL mode that is the mode in which most
editing keycommands are implemented.

Key-Commands
============

Namespace: normal-mode

Mode: -1
Event: <Escape>
Description: Get the focused AreaVi instance in NORMAL mode.
"""

def install(area):
    area.add_mode('NORMAL')
    area.chmode('NORMAL')
    area.install('normal-mode', (-1, '<Escape>', lambda event: area.chmode('NORMAL')))







