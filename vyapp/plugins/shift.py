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
    def __init__(self, area, width=4):
        self.width = width

        area.install('shift', 
        ('NORMAL', '<Key-greater>', self.sel_right),
        ('NORMAL', '<Key-less>',  self.sel_left))
        self.area = area

    def sel_right(self, event):
        """
        Shift ranges of selected text to the right.
        """
        srow, scol = self.area.indref('sel.first')
        erow, ecol = self.area.indref('sel.last')
        self.area.shift_right(srow, erow, self.width)
    
    def sel_left(self, event):
        """
        Shift ranges of selected text to the left.
        """

        srow, scol = self.area.indref('sel.first')
        erow, ecol = self.area.indref('sel.last')
        self.area.shift_left(srow, erow, self.width)

install = Shift







