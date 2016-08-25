"""
Overview
========

This plugin implements two Key-Commands to do quick jumps with the cursor to match 
the symbols.

    ( ) { } [ ] : .

Key-Commands
============

Mode: NORMAL
Event: <Key-P> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

 
Mode: NORMAL
Event: <Key-O> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

"""

def install(area, chars):
    area.install(('NORMAL', '<Key-P>', lambda event: event.widget.go_next_sym(chars)),
                 ('NORMAL', '<Key-O>', lambda event: event.widget.go_prev_sym(chars)))








