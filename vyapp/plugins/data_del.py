"""
Overview
========

This plugin implements keycommands to delete text selection, delete line, delete char.


Key-Commands
============

Namespace: data-del

Mode: NORMAL
Event: <Key-d> 
Description: Delete selection of text.


Mode: NORMAL
Event: <Key-x> 
Description: Delete a line where the cursor is on.


Mode: NORMAL
Event: <Control-x> 
Description: Delete a char from the cursor position.

"""

class DataDel:
    def __init__(self, area):
        area.install('data-del', 
        ('NORMAL', '<Key-d>', self.del_sel),
        ('NORMAL', '<Key-x>', self.del_line),
        ('NORMAL', '<Control-x>', self.del_char))
        self.area = area

    def del_line(self, event):
        """
        It deletes the cursor line, makes the cursor visible
        and adds a separator to the undo stack.
        """

        self.area.edit_separator()
        self.area.delete('insert linestart', 'insert +1l linestart')
        self.area.see('insert')

    def del_char(self, event):
        """
        It deletes a char from the cursor position.
        """

        self.area.edit_separator()
        self.area.delete('insert', 'insert +1c')

    def del_sel(self, event):
        """
        It deletes all selected text.
        """
        self.area.edit_separator()
        self.area.swap_ranges('sel', '', '1.0', 'end')

install = DataDel        

















