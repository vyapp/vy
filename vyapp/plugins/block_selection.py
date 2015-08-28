""" 
Overview
========

This plugin implements block selection of text.

Usage
=====

There are situations where range selection is not sufficient. It may be needed
to select blocks of text. For such, switch to NORMAL mode then place the cursor
over the starting of the block that needs to be selected then press <Control-V>
to drop a mark at that place. 

After pressing <Control-V> there will appear a msg on the statusbar telling the block selection mark
was dropped.

In order to add selection to the region you use the keys <Control-K>, <Control-J>,
<Control-H>, <Control-L> in NORMAL mode to move the cursor around then adding selection to the region.

Whenever <Control-V> in NORMAL mode is pressed the block selection mark will change it turns possible to have
multiple regions of text selected.


Key-Commands
============

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
from vyapp.tools import set_status_msg

def drop_start_mark(area):
    area.start_block_selection()
    set_status_msg('Dropped block selection mark.')

def install(area):
    area.install(('NORMAL', '<Control-K>', lambda event: event.widget.block_up()),
                 ('NORMAL', '<Control-J>', lambda event: event.widget.block_down()),
                 ('NORMAL', '<Control-H>', lambda event: event.widget.block_left()),
                 ('NORMAL', '<Control-L>', lambda event: event.widget.block_right()),
                 ('NORMAL', '<Control-V>', lambda event: drop_start_mark(event.widget)))




