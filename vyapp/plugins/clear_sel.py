"""
Overview
========

This module implements keycommands that clear selection from text.

Usage
=====

When <Escape> is pressed in NORMAL mode, selection tag will be removed, same when <Key-i>
happens in NORMAL mode as well.

Key-Commands
============

Mode: NORMAL
Event: <Escape>
Description: Remove selection from text.

Mode: NORMAL
Event: <Key-i>
Description: Remove selection from text.
"""

def install(area):
    clear = lambda event: event.widget.clear_selection()
    area.install(('NORMAL', '<Escape>', clear), 
                 ('NORMAL', '<Key-i>', clear))

