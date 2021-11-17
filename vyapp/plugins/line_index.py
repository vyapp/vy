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
from vyapp.app import root

class LineIndex:
    def __init__(self, area):
        self.area = area
        area.install('line-index', 
        ('EXTRA', '<Key-q>', self.set_pos))

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

