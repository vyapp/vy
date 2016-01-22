"""
Overview
========

This plugin implements two Key-Commands to do quick jumps with the cursor to match 
the symbols.

    ( ) { } [ ] : .

Usage
=====

Suppose you are editing a python file.

    # blah.py
    def alpha():
        pass
    
    
    def beta():
        pass
    
Consider the cursor is placed in the beginning of the file, after pressing <Key-p> in NORMAL mode
it will make the cursor jump to the next occurence of one of the 

    ( ) { } [ ] : .

chars. It is useful to go through function definitions/block of codes.
You can make the cursor jump back by pressing <Key-O> in NORMAL mode.

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







