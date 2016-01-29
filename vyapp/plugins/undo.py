"""
Overview
========

This plugin implements undo/redo operations.

Usage
=====

This module implements keycommands to do redo/undo operations. After
having deleted, inserted some text in an AreaVi instance, press <Key-comma>
to undo the operation, press <Key-period> to redo the operation.

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



