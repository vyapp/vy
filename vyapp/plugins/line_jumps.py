"""
Overview
========
This plugin implements Key-Commands to make the cursor jump to the end/beginning of the line whose
the cursor is on.

Usage
=====

Sometimes it is handy to quickly jump to the beginning of the line whose cursor is on.
For such, switch to NORMAL mode then press <Key-o>. To place the cursor at the end
of the line just press <Key-p> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-o> 
Description: Place the cursor at the beginning of the line.


Mode: NORMAL
Event: <Key-p> 
Description: Place the cursor at the end of the line.
"""

def install(area):
    area.install(('NORMAL', '<Key-o>', lambda event: event.widget.go_line_start()),
                 ('NORMAL', '<Key-p>', lambda event: event.widget.go_line_end()))




