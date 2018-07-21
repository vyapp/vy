"""
Overview
========

This plugin implements two Key-Commands to do quick jumps with the cursor to match 
the symbols.

    ( ) { } [ ] : .

Key-Commands
============

Namespace: symbol-jumps

Mode: NORMAL
Event: <Key-P> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

 
Mode: NORMAL
Event: <Key-O> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

"""
from re import escape

class SymbolJumps:
    def __init__(self, area, chars):
        area.install('symbol-jumps', 
        ('NORMAL', '<Key-P>', self.next_sym),
        ('NORMAL', '<Key-O>', self.prev_sym))

        self.chars = chars
        self.area  = area        

    def next_sym(self, event):
        """
        Place the cursor at the next occurrence of one of the chars.
        """

        chars = [escape(ind) for ind in self.chars]
        REG   = '|'.join(chars)

        _, index0, index1 = self.area.isearch(REG, index='insert',
        stopindex='end', regexp=True)

        self.area.mark_set('insert', index1)
        self.area.see('insert')

    def prev_sym(self, event):
        """
        Place the cursor at the previous occurrence of one of the chars.
        """

        chars = [escape(ind) for ind in self.chars]
        REG   = '|'.join(chars)

        _, index0, index1 = self.area.isearch(REG,  index='insert', 
        backwards=True, stopindex='1.0', regexp=True)

        self.area.mark_set('insert', index0)
        self.area.see('insert')

install = SymbolJumps


