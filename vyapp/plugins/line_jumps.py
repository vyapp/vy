"""
Overview
========
This plugin implements Key-Commands to make the cursor jump to the end/beginning of the line whose
the cursor is on.

Key-Commands
============

Namespce: line-jumps

Mode: NORMAL
Event: <Key-o> 
Description: Place the cursor at the beginning of the line.


Mode: NORMAL
Event: <Key-p> 
Description: Place the cursor at the end of the line.
"""

def install(area):
    area.install('line-jumps', ('NORMAL', '<Key-o>', lambda event: event.widget.go_line_start()),
                 ('NORMAL', '<Key-p>', lambda event: event.widget.go_line_end()))







