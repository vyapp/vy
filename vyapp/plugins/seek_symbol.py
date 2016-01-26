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
Event: <Control-Key>
Description: It adds/removes selection from the cursor position to the first occurrence of the 
printable char that corresponds to the pressed key.

Mode: JUMP_BACK
Event: <Return>
Description: Switch to INSERT mode.

Mode: JUMP_BACK
Event: <Control-Key>
Description: It adds/removes selection from the cursor position to the previous occurrence of the 
printable char that corresponds to the pressed key.
"""

def get_char(num):
    try:
        char = chr(num)
    except ValueError:
        return ''
    else:
        return char

def sel_next(area, num):
    char = get_char(num)
    index0 = area.index('insert')
    index1 = area.seek_next_down(char, regexp=False)
    if index1: area.toggle_sel(index0, index1[1])

def sel_back(area, num):
    char = get_char(num)
    index0 = area.index('insert')
    index1 = area.seek_next_up(char, regexp=False)
    if index1: area.toggle_sel(index0, index1[0])

def jump_next(area, num):
    char = get_char(num)
    area.seek_next_down(char, regexp=False)

def jump_back(area, num):
    char = get_char(num)
    area.seek_next_up(char, regexp=False)

def install(area):
        area.add_mode('JUMP_BACK')
        area.add_mode('JUMP_NEXT')

        area.install(('NORMAL', '<Key-v>', lambda event: event.widget.chmode('JUMP_NEXT')), 
                     ('NORMAL', '<Key-c>', lambda event: event.widget.chmode('JUMP_BACK')),
                     ('JUMP_BACK', '<Key>', lambda event: jump_back(event.widget, event.keysym_num)),
                     ('JUMP_BACK', '<Control-Key>', lambda event: sel_back(event.widget, event.keysym_num)),
                     ('JUMP_BACK', '<Return>', lambda event: event.widget.chmode('INSERT')),
                     ('JUMP_NEXT', '<Return>', lambda event: event.widget.chmode('INSERT')),
                     ('JUMP_NEXT', '<Tab>', lambda event: event.widget.chmode('JUMP_BACK')),
                     ('JUMP_BACK', '<Tab>', lambda event: event.widget.chmode('JUMP_NEXT')),
                     ('JUMP_NEXT', '<Control-Key>', lambda event: sel_next(event.widget, event.keysym_num)),
                     ('JUMP_NEXT', '<Key>', lambda event: jump_next(event.widget, event.keysym_num)))




