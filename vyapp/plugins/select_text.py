"""
Overview
========

This plugin implements Key-Commands to select ranges of text to the beginning/end of the file from the
cursor position.

Usage
=====

A simple way to select all text from the cursor position to the end of the AreaVi instance is by
pressing <Control-Key-2> in NORMAL mode. The same behavior can be achieved to select
all text to the beginning of the AreaVi instance by pressing <Control-Key-1> in NORMAL mode as well.

Another possibility is selecting all text of the AreaVi instance, for such just press 
<Control-a> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Control-Key-1> 
Description: Add selection from the cursor positon to the beginning of the file.


Mode: NORMAL
Event: <Control-Key-2> 
Description: Add selection from the cursor position to the end of the file.


Mode: NORMAL
Event: <Control-a> 
Description: Add selection from the beginning to the end of the file.
"""


def install(area):
    area.install(('NORMAL', '<Control-Key-1>', lambda event: event.widget.sel_text_start()),
                 ('NORMAL', '<Control-Key-2>', lambda event: event.widget.sel_text_end()),
                 ('NORMAL', '<Control-a>', lambda event: event.widget.select_all()))


