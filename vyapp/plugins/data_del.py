"""
Overview
========

This plugin implements keycommands to delete text selection, delete line, delete char.

Usage
=====

The keycommand most used in this module probably is the one to delete ranges of text
that are selected. It is done by pressing <Key-d> in NORMAL mode.

Another keycommand that is often used is the one to delete the cursor line. Place
the cursor over the desired line then press <Key-x> in NORMAL mode.

This module implements one keycommand to delete the character at the cursor
position. Place the cursor at the desired position then press <Key-z> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-d> 
Description: Delete selection of text.


Mode: NORMAL
Event: <Key-x> 
Description: Delete a line where the cursor is on.


Mode: NORMAL
Event: <Key-z> 
Description: Delete a char from the cursor position.

"""

def install(area):
    area.install(('NORMAL', '<Key-d>', lambda event: event.widget.del_sel()),
                 ('NORMAL', '<Key-x>', lambda event: event.widget.del_line()),
                 ('NORMAL', '<Key-z>', lambda event: event.widget.del_char()))
        












