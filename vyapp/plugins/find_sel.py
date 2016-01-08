"""
Overview
========

Usage
=====

Key-Commands
============

"""


def install(area, setup={'background':'green', 'foreground':'white'}):
    TAG_FOUND = '__FINDSEL__'
    area.tag_config(TAG_FOUND, **setup)
    area.install(('NORMAL', '<Alt-period>', lambda event: event.widget.pick_next_down(TAG_FOUND, event.widget.tag_get_ranges('sel'))),
                 ('NORMAL', '<Alt-comma>', lambda event: event.widget.pick_next_up(TAG_FOUND, event.widget.tag_get_ranges('sel'))),
                 (-1, '<Escape>', lambda event: event.widget.tag_remove(TAG_FOUND, '1.0', 'end')))

