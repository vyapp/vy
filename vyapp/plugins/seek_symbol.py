"""
Overview
========

This plugin implements a mechanism to quickly make the cursor jump back/next to a position.

Key-Commands
============

Namespace: seek-symbol

"""

from vyapp.app import root

def get_char(num):
    try:
        char = chr(num)
    except ValueError:
        return ''
    else:
        return char

class SeekSymbol:
    def __init__(self, area):
        area.add_mode('JUMP_BACK')
        area.add_mode('JUMP_NEXT')

        area.install('seek-symbol', 
        ('NORMAL', '<Key-period>', self.next_mode),
        ('NORMAL', '<Key-comma>', self.back_mode),
        ('JUMP_BACK', '<Tab>', self.sel_data),
        ('JUMP_BACK', '<Key>', self.jump_back),
        ('JUMP_BACK', '<Return>', self.switch_insert),
        ('JUMP_NEXT', '<Return>', self.switch_insert),
        ('JUMP_NEXT', '<Control-c>', self.back_mode),
        ('JUMP_BACK', '<Control-v>', self.next_mode),
        ('JUMP_NEXT', '<Tab>', self.sel_data),
        ('JUMP_NEXT', '<Key>', self.jump_next))
    
        self.area = area

    def next_mode(self, event):
        self.area.mark_set('(RANGE_SEL_MARK)', 'insert')
        self.area.chmode('JUMP_NEXT')

        root.status.set_msg('Switched to JUMP_NEXT mode.')

    def back_mode(self, event):
        self.area.mark_set('(RANGE_SEL_MARK)', 'insert')
        self.area.chmode('JUMP_BACK')

        root.status.set_msg('Switched to JUMP_BACK mode.')

    def switch_insert(self, event):
        self.area.chmode('INSERT')
        root.status.set_msg('Switched to INSERT mode.')

    def jump_next(self, event):
        char  = get_char(event.keysym_num)
        _, index0, index1 = self.area.isearch(char, index='insert', 
        stopindex='end', regexp=False)

        self.area.mark_set('insert', index1)
        self.area.see('insert')

    def jump_back(self, event):
        char  = get_char(event.keysym_num)
        _, index0, index1 = self.area.isearch(char, index='insert', 
        stopindex='1.0', regexp=False, backwards=True)

        self.area.mark_set('insert', index0)
        self.area.see('insert')

    def sel_data(self, event):
        self.area.addsel('insert', '(RANGE_SEL_MARK)')
        self.area.chmode('NORMAL')

install = SeekSymbol


