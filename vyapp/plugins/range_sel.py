""" 
Overview
========

This plugin implements range selection.

Key-Commands
============

Namespace: range-sel

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

from vyapp.app import root

def drop_selection_mark(area):
    area.start_selection()
    root.status.set_msg('Dropped selection mark.')

def install(area):
    area.install('range-sel', ('NORMAL', '<Control-k>', lambda event: event.widget.sel_up()),
                 ('NORMAL', '<Control-j>', lambda event: event.widget.sel_down()),
                 ('NORMAL', '<Control-h>', lambda event: event.widget.sel_left()),
                 ('NORMAL', '<Control-l>', lambda event: event.widget.sel_right()),
                 ('NORMAL', '<Control-v>', lambda event: drop_selection_mark(event.widget)))








