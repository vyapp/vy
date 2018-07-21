"""
Overview
========

It is handy to have Key-Commands to insert blank lines up/down the cursor when in NORMAL mode.

Key-Commands
============

Namespace: line-feed

Mode: NORMAL
Event: <Key-m> 
Description: Insert a line down then goes insert mode.


Mode: NORMAL
Event: <Key-n> 
Description: Insert a line up then goes insert mode.


"""

class LineFeed:
    def __init__(self, area):
        area.install('line-feed', 
        ('NORMAL', '<Key-m>', self.insert_down),
        ('NORMAL', '<Key-n>', self.insert_up))

        self.area = area

    def insert_down(self, event):
        """
        It inserts one line down from the cursor position.
        """

        self.area.edit_separator()
        self.area.insert('insert +1l linestart', '\n')
        self.area.mark_set('insert', 'insert +1l linestart')

        self.area.see('insert')
        self.area.chmode('INSERT')
    
    def insert_up(self, event):
        """
        It inserts one line up.
        """

        self.area.edit_separator()
        self.area.insert('insert linestart', '\n')
        self.area.mark_set('insert', 'insert -1l linestart')
        self.area.see('insert')

        self.area.chmode('INSERT')

install = LineFeed
