""" 
Overview
========

This plugin implements block selection of text.

Key-Commands
============

Namespace: block-sel

Mode: NORMAL
Event: <Control-K> 
Description: Add block selection one line up.


Mode: NORMAL
Event: <Control-J>
Description: Add block selection one line down.

Mode: NORMAL
Event: <Control-H>
Description: Add block selection one char left.

Mode: NORMAL
Event: <Control-L>
Description: Add block selection one char right.

"""
from vyapp.app import root

def drop_start_mark(area):
    area.start_block_selection()
    root.status.set_msg('Dropped block selection mark.')

def install(area):
    area.install('block-sel', ('NORMAL', '<Control-K>', lambda event: event.widget.block_up()),
                 ('NORMAL', '<Control-J>', lambda event: event.widget.block_down()),
                 ('NORMAL', '<Control-H>', lambda event: event.widget.block_left()),
                 ('NORMAL', '<Control-L>', lambda event: event.widget.block_right()),
                 ('NORMAL', '<Control-V>', lambda event: drop_start_mark(event.widget)))








