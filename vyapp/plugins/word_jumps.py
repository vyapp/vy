"""
Overview
========

This plugin implements Key-Commands to make the cursor jump to the next/previous word as well as
selecting a given word when the cursor is on.

Usage
=====

The cursor jumps to the next occurence of a word by pressing <Key-bracketright> in NORMAL mode,
in order to make the cursor jumps to the previous occurrence of a word you type 
<Key-braceright> in NORMAL mode.

It is useful to have a word whose cursor is placed on sometimes.
For such just press <Key-bracketleft> in NORMAL mode.

Key-Commands
============

Mode: 1
Event: <Key-bracketright> 
Description: Place the cursor at the beginning of the next word.


Mode: 1
Event: <Key-braceright> 
Description: Place the cursor at the beginning of the previous word.


Mode: 1
Event: <Key-bracketleft> 
Description: Add selection to a word where the cursor is placed on.

"""

def install(area):
    area.install(('NORMAL', '<Key-bracketright>', lambda event: event.widget.go_next_word()),
                 ('NORMAL', '<Key-braceright>', lambda event: event.widget.go_prev_word()),
                 ('NORMAL', '<Key-bracketleft>', lambda event: event.widget.select_word()))





