"""
Overview
========

This plugin implements Key-Commands to select lines and chunks of text inside a line.

Usage
=====

Once in NORMAL mode if you press <Key-f> then the line whose cursor is on will be selected.

In order to select a given range of the line from the cursor position you can type <Control-o> that
will select the range of the line starting from the cursor position to the beginning of the line.

In order to select a range of the line from the cursor position to the end of the line you type
<Control-p> in NORMAL mode.

Key-Commands
============

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
    area.install(('NORMAL', '<Key-f>', lambda event: event.widget.toggle_line_selection()),
                 ('NORMAL', '<Control-o>', lambda event: event.widget.sel_line_start()),
                 ('NORMAL', '<Control-p>', lambda event: event.widget.sel_line_end()))



