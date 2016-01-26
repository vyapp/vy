"""
Overview
========

This plugin implements key-commands to delete text selection, delete line, delete char.

Usage
=====


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
    area.install(('NORMAL', '<Key-d>', lambda event: event.widget.clsel()),
                 ('NORMAL', '<Key-x>', lambda event: event.widget.cllin()),
                 ('NORMAL', '<Key-z>', lambda event: event.widget.clchar()))
        










