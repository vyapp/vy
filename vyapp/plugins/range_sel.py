""" 
Overview
========

This plugin implements range selection.

Usage
=====

First of all it is needed to drop a selection mark to start range selection.
Switch to NORMAL mode then type <Control-v>.

Once the selection mark is dropped you can start selection by using the keys <Control-h>,
<Control-j>, <Control-k>, <Control-l> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Control-k> 
Description: Add/remove selection one line up from the initial selection mark.


Mode: NORMAL
Event: <Control-j> 
Description: Add/remove selection one line down from the initial selection mark.


Mode: NORMAL
Event: <Control-l> 
Description: Add/remove selection one character right from the initial selection mark.


Mode: NORMAL
Event: <Control-h> 
Description: Add/remove selection one character left from the initial selection mark.


Mode: NORMAL
Event: <Control-v> 
Description: Drop a selection mark.
"""

from vyapp.tools import set_status_msg

def drop_selection_mark(area):
    area.start_selection()
    set_status_msg('Dropped selection mark.')

def install(area):
    area.install(('NORMAL', '<Control-k>', lambda event: event.widget.sel_up()),
                 ('NORMAL', '<Control-j>', lambda event: event.widget.sel_down()),
                 ('NORMAL', '<Control-h>', lambda event: event.widget.sel_left()),
                 ('NORMAL', '<Control-l>', lambda event: event.widget.sel_right()),
                 ('NORMAL', '<Control-v>', lambda event: drop_selection_mark(event.widget)))




