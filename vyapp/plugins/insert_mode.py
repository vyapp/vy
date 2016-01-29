"""
Overview
========

This module implements the INSERT mode that implements the functionality of inserting chars
in the AreaVi instances.

Usage
=====

This mode is a builtin mode that is used to edit the content of a given AreaVi instance.
In order to place an AreaVi instance in INSERT mode, switch to NORMAL mode then press <Key-i>.

Key-Commands
============

Mode: NORMAL
Event: <Key-i>
Description: Get the focused AreaVi instance in INSERT mode.
"""

def insert(area):
    area.chmode('INSERT')

def install(area):
    # The two basic modes, insert and selection.
    area.add_mode('INSERT', opt=True)
    area.install(('NORMAL', '<Key-i>', lambda event: insert(event.widget)))



