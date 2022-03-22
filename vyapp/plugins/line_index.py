"""
Overview
========

This plugin implements a way to place the cursor at a given row.col.


Key-Commands
============

Namespace: line-index

Mode: EXTRA
Event: <Key-q>
Description: Shows an input text field to insert a Line.Col value to place the cursor at that position.

"""
from vyapp.ask import Ask
from tkinter import TclError
from vyapp.tools import e_stop
from vyapp.app import root
from vyapp.plugins import Namespace

class LineIndexNS(Namespace):
    pass

class LineIndex:
    def __init__(self, area):
        self.area = area
        area.install(LineIndexNS, 
        (-1, '<Alt-w>', self.set_pos))

    @e_stop
    def set_pos(self, area):
        root.status.set_msg('Jump Line/Line.Col:')

        ask = Ask()
        vals = ask.data.split('.')
        
        try:
            self.area.setcur(*vals)
        except TclError as e:
            root.status.set_msg('Failed: %s' % e)
        else:
            root.status.set_msg('Jumped to: %s' % ask.data)
    
install = LineIndex

