"""
Overview
========

This plugin implements Key-Commands to shift blocks of text.

Usage
=====

To shift a block of text, first select it then press <Key-greater> in NORMAL mode to shift to the right.
In order to shift blocks of text to the left, select the block of text then press <Key-less> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-greater>
Description: Shift to the right.

Mode: NORMAL
Event: <Key-less>
Description: Shift to the left.

"""

class Shift(object):
    def __init__(self, area, width=4, char=' '):
        self.width = width
        self.char  = char
        area.install(('NORMAL', '<Key-greater>', lambda event: event.widget.shift_sel_right(self.width, self.char)),
                     ('NORMAL', '<Key-less>', lambda event: event.widget.shift_sel_left(self.width)))


install = Shift



