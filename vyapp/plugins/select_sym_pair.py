"""
Overview
========
This plugin implements a Key-Command to select text between pairs of () [] {}.

Usage
=====

When the cursor is placed over one of the () [] {} and the key press event
<Key-slash> happens in NORMAL mode then the text between the pair will be selected.

Such a behavior is useful when dealing with some programming languages like lisp.


Key-Commands
============

Mode: NORMAL
Event: <Key-slash> 
Description: Select text between pairs of ( ) [] {} when the cursor
is placed over one of these characters.
"""


def install(area):
    area.install(('NORMAL', '<Key-slash>', lambda event: event.widget.select_case_pair(('(', ')'))),
                 ('NORMAL', '<Key-slash>', lambda event: event.widget.select_case_pair(('[', ']'))),
                 ('NORMAL', '<Key-slash>', lambda event: event.widget.select_case_pair(('{', '}'))))



