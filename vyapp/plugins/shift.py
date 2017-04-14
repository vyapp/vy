"""
Overview
========

This plugin implements Key-Commands to shift blocks of text.

Key-Commands
============

Namespace: shift

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
        area.install('shift', ('NORMAL', '<Key-greater>', lambda event: event.widget.shift_sel_right(self.width, self.char)),
                     ('NORMAL', '<Key-less>', lambda event: event.widget.shift_sel_left(self.width)))


install = Shift






