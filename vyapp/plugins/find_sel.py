"""
Overview
========

This plugin implements key-commands to find previous/next occurrences of text pattern that is selected.
It is useful when reading documentation that has a table of content.

Usage
=====

Select a word then press <Alt-period> in NORMAL mode it will jump to the next occurrence of that word from the cursor position.
In order to go back to the previous occurence just press <Alt-comma> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Alt-period>
Description: Make the cursor jump to the next occurrence of the text that is selected.

Mode: NORMAL
Event: <Alt-comma>
Description: Make the cursor jump to the previous occurrence of the text that is selected.

"""


def install(area, setup={'background':'green', 'foreground':'white'}):
    TAG_FOUND = '__FINDSEL__'
    area.tag_config(TAG_FOUND, **setup)
    area.install(('NORMAL', '<Alt-period>', lambda event: event.widget.pick_next_down(TAG_FOUND, event.widget.join_ranges('sel'))),
                 ('NORMAL', '<Alt-comma>', lambda event: event.widget.pick_next_up(TAG_FOUND, event.widget.join_ranges('sel'))),
                 (-1, '<Escape>', lambda event: event.widget.tag_remove(TAG_FOUND, '1.0', 'end')))



