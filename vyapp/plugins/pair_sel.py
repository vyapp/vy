"""
Overview
========

This plugin implements a Key-Command to select text between pairs of () [] {}.


Key-Commands
============

Namespace: sym-pair-sel

Mode: NORMAL
Event: <Key-slash> 
Description: Select text between pairs of ( ) [] {} when the cursor
is placed over one of these characters.

Mode: NORMAL
Event: <Control-Key-slash> 
Description: Select text between pairs of ( ) [] {} including the pairs when the cursor
is placed over one of these characters.
"""

class PairSel:
    def __init__(self, area, max=2500):
        area.install('pair-sel', 
        ('NORMAL', '<Key-slash>', self.sel_data),
        ('NORMAL', '<Control-Key-slash>', self.sel_pair),)
        self.max = max
        self.area = area
    
    def get_pos(self):
        index = self.area.case_pair('insert', self.max, '(', ')')
        if index: return index

        index = self.area.case_pair('insert', self.max, '[', ']')
        if index: return index

        index = self.area.case_pair('insert', self.max, '{', '}')
        if index: return index

    def sel_data(self, event):
        index = self.get_pos()
        if not index: return

        min = self.area.min(index, 'insert')
        max = self.area.max(index, 'insert')
        min = '%s +1c' % min

        self.area.tag_add('sel', min, max)

    def sel_pair(self, event):
        """
        """
        index = self.get_pos()
        if not index: return

        min = self.area.min(index, 'insert')
        max = self.area.max(index, 'insert')
        max = '%s +1c' % max

        self.area.tag_add('sel', min, max)

install = PairSel


