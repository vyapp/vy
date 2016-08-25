"""
Overview
========

This plugin implements undo/redo operations.

Key-Commands
============

Mode: NORMAL
Event: <Key-comma> 
Description: Do undo.

Mode: NORMAL
Event: <Key-period> 
Description: Do redo.
"""


def install(area):
    area.install(('NORMAL', '<Key-comma>', lambda event: event.widget.do_undo()),
                 ('NORMAL', '<Key-period>', lambda event: event.widget.do_redo()))




