"""
Overview
========

This module implements the NORMAL mode that is the mode in which most
editing keycommands are implemented.

Key-Commands
============

Namespace: normal-mode

Mode: -1
Event: <Escape>
Description: Get the focused AreaVi instance in NORMAL mode.

Mode: -1
Event: <Alt-n>
Description: Get the focused AreaVi instance in EXTRA mode.

Mode: NORMAL
Event: <Key-i>
Description: Get the focused AreaVi instance in INSERT mode.

"""

class BuiltinModes:
    def __init__(self, area):
        self.area = area

        area.add_mode('NORMAL')
        area.chmode('NORMAL')
   
        area.add_mode('INSERT', opt=True)
        area.add_mode('EXTRA')

        area.install('builtin-modes', 
        (-1, '<Escape>', self.switch_normal),
        (-1, '<Alt-n>', self.switch_extra),
        ('NORMAL', '<Key-i>', self.switch_insert))
    
    def switch_normal(self, event):
        """
        """
        self.area.chmode('NORMAL')
        self.area.clear_selection()

    def switch_insert(self, event):
        """
        """

        self.area.chmode('INSERT')
        self.area.clear_selection()

    def switch_extra(self, event):
        """
        """

        self.area.chmode('EXTRA')
        return 'break'

install = BuiltinModes
 

