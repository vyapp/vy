"""
Overview
========

This module implements the INSERT mode that implements the functionality of inserting chars
in the AreaVi instances.

Key-Commands
============

Namespace: insert-mode

Mode: NORMAL
Event: <Key-i>
Description: Get the focused AreaVi instance in INSERT mode.
"""

def insert(area):
    area.chmode('INSERT')

def install(area):
    # The two basic modes, insert and selection.
    area.add_mode('INSERT', opt=True)
    area.install('insert-mode', ('NORMAL', '<Key-i>', lambda event: insert(event.widget)))






