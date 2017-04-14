"""
Overview
========

This module implements keycommands that clear selection from text.

Key-Commands
============

Namespace: clear-sel

Mode: NORMAL
Event: <Escape>
Description: Remove selection from text.

Mode: NORMAL
Event: <Key-i>
Description: Remove selection from text.
"""

def install(area):
    clear = lambda event: event.widget.clear_selection()
    area.install('clear-sel', ('NORMAL', '<Escape>', clear), 
                 ('NORMAL', '<Key-i>', clear))




