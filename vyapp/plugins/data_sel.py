"""
Overview
========

This module implements keycommands to select sequences of chars that
match a special pattern, words, non blank sequences etc.

Key-Commands
============

Namespace: data-sel

Mode: NORMAL
Event: <Key-bracketleft> 
Description: Add selection to a word where the cursor is placed on.

Mode: NORMAL
Event: <Control-bracketleft>
Description: Select a sequence of non blank chars that is over
the cursor.
"""

def install(area):
    area.install('data-sel', ('NORMAL', '<Control-bracketleft>', lambda event: event.widget.select_seq()),
                 ('NORMAL', '<Key-bracketleft>', lambda event: event.widget.select_word()))




