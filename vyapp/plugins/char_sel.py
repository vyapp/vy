"""
Overview
========

Used to select chars.

Key-Commands
============

Namespace: char-sel

Mode: NORMAL
Event: <Key-C> 
Description: Add selection to a character whose cursor is on.


Mode: NORMAL
Event: <Key-V> 
Description: Remove selection from a character whose cursor is on.
"""

def install(area):
    area.install('char-sel', ('NORMAL', '<Key-C>', lambda event: event.widget.select_char()),
                 ('NORMAL', '<Key-V>', lambda event: event.widget.unselect_char()))







