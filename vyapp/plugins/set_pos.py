"""
Overview
========

This plugin implements a way to place the cursor at a given row.col.

Usage
=====

When dealing with some programming files we get some warnings/errors from the interpreter/compiler
then we need to quickly jump to that line to see whats going on.

In order to make the cursor jump to a given line.row, just press <F3> in NORMAL mode.
It will show up an input data field where you can insert the line or the row.

Example:

Would make the cursor be placed at the line 30 and at the col 4.
30.4

Would make the cursor be placed at the line 30 and at the col 0.
10

Key-Commands
============

Mode: NORMAL
Event: <F3>
Description: Shows an input text field to insert a Line.Col value to place the cursor at that position.

"""
from vyapp.ask import *

def go_to_pos(area):
    ask = Ask(area)

    try:
        area.seecur(ask.data)
    except TclError:
        pass

    try:
        area.setcur(ask.data)
    except TclError:
        pass

install = lambda area: area.install(('NORMAL', '<F3>', lambda event: go_to_pos(event.widget)))







