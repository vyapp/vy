"""
Overview
========

This plugin implements Key-Commands to select lines and chunks of text inside a line.

Key-Commands
============

Namespace: line-sel

Mode: NORMAL
Event: <Key-f> 
Description: Add selection to a line over the cursor.

Mode: NORMAL
Event: <Control-o> 
Description: Add selection from the cursor position to the beginning of the line.


Mode: NORMAL
Event: <Control-p> 
Description: Add selection from the cursor position to the end of the line.
"""

def install(area):
    area.install('line-sel', ('NORMAL', '<Key-f>', lambda event: event.widget.toggle_line_selection()),
                 ('NORMAL', '<Control-o>', lambda event: event.widget.sel_line_start()),
                 ('NORMAL', '<Control-p>', lambda event: event.widget.sel_line_end()))






