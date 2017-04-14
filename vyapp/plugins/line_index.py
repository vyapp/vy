"""
Overview
========

This plugin implements a way to place the cursor at a given row.col.


Key-Commands
============

Namespace: line-index

Mode: NORMAL
Event: <Control-q>
Description: Shows an input text field to insert a Line.Col value to place the cursor at that position.

"""
from vyapp.ask import *

def go_to_pos(area):
    ask = Ask()

    try:
        area.seecur(ask.data)
    except TclError:
        pass

    try:
        area.setcur(ask.data)
    except TclError:
        pass

install = lambda area: area.install('line-index', 
('NORMAL', '<Control-q>', lambda event: go_to_pos(event.widget)))












