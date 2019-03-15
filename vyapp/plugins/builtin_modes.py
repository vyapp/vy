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

class BuiltinModes(object):
    def __init__(self, area):
        self.area = area

        area.add_mode('NORMAL')
        area.chmode('NORMAL')
   
        area.add_mode('INSERT', opt=True)
        area.add_mode('DELTA')
        area.add_mode('GAMMA')
        area.add_mode('BETA')
        area.add_mode('ALPHA')

        area.install('builtin-modes', 
        (-1, '<Escape>', lambda event: area.chmode('NORMAL')),
        ('NORMAL', '<Key-i>', lambda event: area.chmode('INSERT')),
        ('NORMAL', '<Key-6>', lambda event: area.chmode('DELTA')),
        ('NORMAL', '<Key-5>', lambda event: area.chmode('GAMMA')),
        ('NORMAL', '<Key-4>', lambda event: area.chmode('BETA')),
        ('NORMAL', '<Key-3>', lambda event: area.chmode('ALPHA')))

install = BuiltinModes
 

