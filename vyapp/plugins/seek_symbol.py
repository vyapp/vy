"""
Overview
========

This plugin implements a mechanism to quickly make the cursor jump back/next to a position.

Key-Commands
============

Namespace: seek-symbol

Mode: NORMAL
Event: <Key-v> 
Description: Switch to JUMP_NEXT mode.

Mode: NORMAL
Event: <Key-c>
Description: Switch to JUMP_BACK mode.

Mode: JUMP_BACK
Event: <Backspace>
Description: Switch to JUMP_NEXT mode.

Mode: JUMP_NEXT
Event: <Backspace>
Description: Switch to JUMP_BACK mode.

Mode: JUMP_NEXT
Event: <Return>
Description: Switch to INSERT mode.

Mode: JUMP_NEXT
Event: <Tab>
Description: It adds/removes selection from initial cursor position to the insert position.

Mode: JUMP_BACK
Event: <Return>
Description: Switch to INSERT mode.

Mode: JUMP_BACK
Event: <Tab>
Description: It adds/removes selection from initial cursor position to the insert position.
"""

def get_char(num):
    try:
        char = chr(num)
    except ValueError:
        return ''
    else:
        return char

class SeekSymbol(object):
    def __init__(self, area):
        area.add_mode('JUMP_BACK')
        area.add_mode('JUMP_NEXT')

        area.install('seek-symbol', 
        ('NORMAL', '<Key-v>', lambda event: self.start_next_mode()), 
        ('NORMAL', '<Key-c>', lambda event: self.start_back_mode()),
        ('JUMP_BACK', '<Tab>', lambda event: self.select_data()),
        ('JUMP_BACK', '<Key>', lambda event: self.jump_back(event.keysym_num)),
        ('JUMP_BACK', '<Return>', lambda event: event.widget.chmode('INSERT')),
        ('JUMP_NEXT', '<Return>', lambda event: event.widget.chmode('INSERT')),
        ('JUMP_NEXT', '<BackSpace>', lambda event: event.widget.chmode('JUMP_BACK')),
        ('JUMP_BACK', '<BackSpace>', lambda event: event.widget.chmode('JUMP_NEXT')),
        ('JUMP_BACK', '<Control-v>', lambda event: self.area.start_selection()),
        ('JUMP_NEXT', '<Tab>', lambda event: self.select_data()),
        ('JUMP_NEXT', '<Control-v>', lambda event: self.area.start_selection()),
        ('JUMP_NEXT', '<Key>', lambda event: self.jump_next(event.keysym_num)))
    
        self.area = area

    def start_next_mode(self):
        self.area.start_selection()
        self.area.chmode('JUMP_NEXT')

    def start_back_mode(self):
        self.area.start_selection()
        self.area.chmode('JUMP_BACK')

    def jump_next(self, num):
        char = get_char(num)
        self.area.iseek(char, index='insert', stopindex='end', regexp=False)
    
    def jump_back(self, num):
        char = get_char(num)
        self.area.iseek(char, index='insert', stopindex='1.0',  regexp=False, backwards=True)
    
    def select_data(self):
        self.area.addsel('insert', '(RANGE_SEL_MARK)')
        self.area.chmode('NORMAL')

install = SeekSymbol










