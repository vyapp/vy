"""
Overview
========

This plugin implements the basic cursor movements.

Key-Commands
============

Namespace: main-jumps

Mode: NORMAL
Event: <Key-j> 
Description: Move the cursor one line down.


Mode: NORMAL
Event: <Key-k> 
Description: Move the cursor one line up.


Mode: NORMAL
Event: <Key-h> 
Description: Move the cursor one character left.


Mode: NORMAL
Event: <Key-l> 
Description: Move the cursor one character right.


"""


def install(area):
    area.install('main-jumps', ('NORMAL', '<Key-j>', lambda event: event.widget.down()),
                 ('NORMAL', '<Key-k>', lambda event: event.widget.up()),
                 ('NORMAL', '<Key-h>', lambda event: event.widget.left()),
                 ('NORMAL', '<Key-l>', lambda event: event.widget.right()))







