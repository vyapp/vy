"""
Overview
========

This plugin implements undo/redo operations.

Key-Commands
============

Namespace: undo

Mode: NORMAL
Event: <Key-comma> 
Description: Do undo.

Mode: NORMAL
Event: <Key-period> 
Description: Do redo.
"""

class Undo:
    def __init__(self, area):
        area.install('undo', 
        ('NORMAL', '<Key-comma>', lambda event: event.widget.edit_undo()),
        ('NORMAL', '<Key-period>', lambda event: event.widget.edit_redo()))

install = Undo






