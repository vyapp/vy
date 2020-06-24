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

Mode: NORMAL
Event: <Key-4>
Description: Get the AreaVi instance in BETA mode.

Mode: NORMAL
Event: <Key-6>
Description: Get the AreaVi instance in DELTA mode.

Mode: <NORMAL>
Event: <Key-5>
Description: Get the AreaVi instance that has focus in GAMMA mode.

Mode: NORMAL
Event: <Key-3>
Description: Get the AreaVi instance that is focused in ALPHA mode.
"""

class BuiltinModes:
    def __init__(self, area):
        self.area = area

        area.add_mode('NORMAL')
        area.chmode('NORMAL')
   
        area.add_mode('INSERT', opt=True)
        area.add_mode('DELTA')
        area.add_mode('GAMMA')
        area.add_mode('BETA')
        area.add_mode('ALPHA')
        area.add_mode('EXTRA')

        area.install('builtin-modes', 
        (-1, '<Escape>', self.switch_normal),
        (-1, '<Alt-n>', self.switch_extra),
        ('NORMAL', '<Key-i>', self.switch_insert),
        ('NORMAL', '<Key-6>', self.switch_delta),
        ('NORMAL', '<Key-5>', self.switch_gamma),
        ('NORMAL', '<Key-4>', self.switch_beta),
        ('NORMAL', '<Key-3>', self.switch_alpha))
    
    def switch_delta(self, event):
        """
        """
        self.area.chmode('DELTA')

    def switch_gamma(self, event):
        """
        """

        self.area.chmode('GAMMA')

    def switch_beta(self, event):
        """
        """

        self.area.chmode('BETA')

    def switch_alpha(self, event):
        """
        """

        self.area.chmode('ALPHA')

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
 

