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
from vyapp.plugins import Namespace

class ShiftNS(Namespace):
    pass

class Shift:
    def __init__(self, area):
        area.install(ShiftNS, 
        ('NORMAL', '<Key-greater>', self.sel_right),
        ('NORMAL', '<Key-less>',  self.sel_left))
        self.area = area

    def sel_right(self, event):
        """
        Shift ranges of selected text to the right.
        """
        srow, scol = self.area.indexsplit('sel.first')
        erow, ecol = self.area.indexsplit('sel.last')

        self.area.edit_separator()
        for ind in range(srow, erow + 1):
            self.area.insert('%s.0' % ind, self.area.tabchar) 
    
    def sel_left(self, event):
        """
        Shift ranges of selected text to the left.
        """

        srow, scol = self.area.indexsplit('sel.first')
        erow, ecol = self.area.indexsplit('sel.last')

        self.area.edit_separator()
        for ind in range(srow, erow + 1):
            self.area.delete('%s.0' % ind, '%s.%s' % (ind, 1)) 

install = Shift


