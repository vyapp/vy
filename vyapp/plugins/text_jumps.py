"""

Overview
========

This plugin implements two Key-Commands to make the cursor jump to the begining/end of the file.

Usage
=====

In order to jump to the beginning of the file wherever the cursor is placed on, just type <Key-1>
in NORMAL mode. To place the cursor at the end of file then type <Key-2> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-1> 
Description: Place the cursor at the beginning of the file.


Mode: NORMAL
Event: <Key-2> 
Description: Place the cursor at the end of the file.

"""

def install(area):
    area.install(('NORMAL', '<Key-1>', lambda event: event.widget.go_text_start()),
                 ('NORMAL', '<Key-2>', lambda event: event.widget.go_text_end()))





