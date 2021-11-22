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
    lhs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    rhs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    MAX = 2500
    def __init__(self, area):
        area.install('pair-sel', 
        ('NORMAL', '<Key-a>', self.sel_inner),
        ('NORMAL', '<Control-a>', self.sel_all))
        self.area = area
    
    def sel_inner(self, event):
        """
        Select inner text between pair tokens.
        """

        token = self.area.get('insert', 'insert +1c')
        if token in self.lhs:
            self.area.tag_add('sel', 'insert +1c', 
                self.area.pair(token,self.lhs[token], 
                    'insert', self.MAX)[0])
        elif token in self.rhs:
            self.area.tag_add('sel', self.area.pair(self.rhs[token], 
                token, 'insert +1c', 
                    self.MAX, True)[1], 'insert')

    def sel_all(self, event):
        """
        Select text between pair tokens also the tokens.
        """

        token = self.area.get('insert', 'insert +1c')
        if token in self.lhs:
            self.area.tag_add('sel', 'insert', self.area.pair(
                token,self.lhs[token], 'insert', self.MAX)[1])
        elif token in self.rhs:
            self.area.tag_add('sel', self.area.pair(self.rhs[token], 
                token, 'insert +1c', self.MAX, True)[0], 'insert +1c')

install = PairSel


