"""
Overview
========

This plugin implements a Key-Command to select text between pairs of () [] {}.


Key-Commands
============

Namespace: sym-pair-sel

Mode: NORMAL
Event: <Key-comma> 
Description: Select text between pairs of ( ) [] {} when the cursor
is placed over one of these characters.

Mode: NORMAL
Event: <Control-comma> 
Description: Select text between pairs of ( ) [] {} 
including the pairs when the cursor is placed over one of these characters.
"""

class PairSel:
    def __init__(self, area, max=2500):
        area.install('pair-sel', 
        ('NORMAL', '<Key-comma>', self.sel_inner_data),
        ('NORMAL', '<Control-comma>', self.sel_pair))
        self.max  = max
        self.area = area
    
    def match_pair(self):
        pairs = (('(', ')'), ('[', ']'), ('{', '}'))
        for lhs, rhs in pairs:
            index = self.area.pair('insert', self.max, lhs, rhs)
            if index is not None: 
                return index

    def sel_inner_data(self, event):
        index = self.match_pair()

        if not index: 
            return None
        min = self.area.min(index, 'insert')
        max = self.area.max(index, 'insert')
        min = '%s +1c' % min

        self.area.tag_add('sel', min, max)

    def sel_pair(self, event):
        """
        """
        index = self.match_pair()
        if not index: 
            return None

        min = self.area.min(index, 'insert')
        max = self.area.max(index, 'insert')
        max = '%s +1c' % max

        self.area.tag_add('sel', min, max)

install = PairSel


