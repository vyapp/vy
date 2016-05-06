"""
Overview
========

This plugin implements a mechanism to quickly make the cursor jump back/next to a position.

Usage
=====

Consider the cursor is over the char 'u' and you notice you want to edit the piece of
text that is placed some chars ahead in front of the char 'e'. The fastest way 
to move the cursor to that position is by switching to JUMP_NEXT mode by pressing <Key-v>
in NORMAL mode then pressing <Key-e>

It is a particular example it would work with any supported char by your keyboard.

The same scheme works to jump chars back from a given position by switching to
JUMP_BACK mode. For such, type <Key-c> in NORMAL mode.

Once you have placed the cursor in the desired position then you are done
to go back to NORMAL mode, just press <Escape> then vy will be go back to NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-v> 
Description: Switch to JUMP_NEXT mode.

Mode: NORMAL
Event: <Key-c>
Description: Switch to JUMP_BACK mode.

Mode: JUMP_BACK
Event: <Tab>
Description: Switch to JUMP_NEXT mode.

Mode: JUMP_NEXT
Event: <Tab>
Description: Switch to JUMP_BACK mode.

Mode: JUMP_NEXT
Event: <Return>
Description: Switch to INSERT mode.

Mode: JUMP_NEXT
Event: <Control-v>
Description: It adds/removes selection from initial cursor position to the insert position.

Mode: JUMP_BACK
Event: <Return>
Description: Switch to INSERT mode.

Mode: JUMP_BACK
Event: <Control-v>
Description: It adds/removes selection from initial cursor position to the insert position.
"""

def get_char(num):
    try:
        char = chr(num)
    except ValueError:
        return ''
    else:
        return char

class Seek(object):
    def __init__(self, area):
        area.add_mode('JUMP_BACK')
        area.add_mode('JUMP_NEXT')

        area.install(('NORMAL', '<Key-v>', lambda event: self.start_next_mode()), 
                     ('NORMAL', '<Key-c>', lambda event: self.start_back_mode()),
                     ('JUMP_BACK', '<Control-v>', lambda event: self.select_data()),
                     ('JUMP_BACK', '<Key>', lambda event: self.jump_back(event.keysym_num)),
                     ('JUMP_BACK', '<Return>', lambda event: event.widget.chmode('INSERT')),
                     ('JUMP_NEXT', '<Return>', lambda event: event.widget.chmode('INSERT')),
                     ('JUMP_NEXT', '<Tab>', lambda event: event.widget.chmode('JUMP_BACK')),
                     ('JUMP_BACK', '<Tab>', lambda event: event.widget.chmode('JUMP_NEXT')),
                     ('JUMP_NEXT', '<Control-v>', lambda event: self.select_data()),
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
        self.area.seek_next_down(char, regexp=False)
    
    def jump_back(self, num):
        char = get_char(num)
        self.area.seek_next_up(char, regexp=False)
    
    def select_data(self):
        self.area.addsel('insert', '(RANGE_SEL_MARK)')
        self.area.chmode('NORMAL')

install = Seek




