"""
Overview
========

Used to select chars.

Usage
=====

Place the cursor over a char then type <Key-C> in NORMAL mode. it will select the char.
When you press <Key-V> over a selected char then it will remove selection from that char.

Key-Commands
============

Mode: NORMAL
Event: <Key-C> 
Description: Add selection to a character whose cursor is on.


Mode: NORMAL
Event: <Key-V> 
Description: Remove selection from a character whose cursor is on.
"""

def install(area):
    area.install(('NORMAL', '<Key-C>', lambda event: event.widget.select_char()),
                 ('NORMAL', '<Key-V>', lambda event: event.widget.unselect_char()))




