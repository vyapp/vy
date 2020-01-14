"""
Overview
========

This plugin implements undo/redo operations.

Key-Commands
============

Namespace: undo

Mode: NORMAL
Event: <Key-bracketright> 
Description: Do undo.

Mode: NORMAL
Event: <Key-bracketleft> 
Description: Do redo.
"""

class Undo:
    def __init__(self, area):
        area.install('undo', 
        ('NORMAL', '<Key-bracketright>', lambda event: event.widget.edit_undo()),
        ('NORMAL', '<Key-bracketleft>', lambda event: event.widget.edit_redo()))

install = Undo






