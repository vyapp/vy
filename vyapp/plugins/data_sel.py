"""
Overview
========

This module implements keycommands to select sequences of chars that
match a special pattern, words, non blank sequences etc.

Usage
=====

It is useful to have a word whose cursor is placed on sometimes.
For such just press <Key-bracketleft> in NORMAL mode.

In order to select a sequence of characters that is not a space that is over
the cursor, press <Control-bracketleft> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-bracketleft> 
Description: Add selection to a word where the cursor is placed on.

Mode: NORMAL
Event: <Control-bracketleft>
Description: Select a sequence of non blank chars that is over
the cursor.
"""

def install(area):
    area.install(('NORMAL', '<Control-bracketleft>', lambda event: event.widget.select_seq()),
                 ('NORMAL', '<Key-bracketleft>', lambda event: event.widget.select_word()))

