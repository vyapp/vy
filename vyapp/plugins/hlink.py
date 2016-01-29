"""
Overview
========

This module implements functionalities to highligh text that maps to URL links.

Key-Commands
============

Mode: -1
Event: <<LoadData>>
Description: Highligh all URLS that appear in the file text.
"""

TAG_LINK      = '_link_'
REG_LINK      = 'https?\:\/\/[^ ]+'

def hlink(area):
    """
    It highlighes links.
    
    """

    seq = area.find(REG_LINK, '1.0', 'end')

    for (_, pos0, pos1) in seq:
        area.tag_add(TAG_LINK, pos0, pos1)



def install(area, setup={'background':'yellow', 'foreground':'blue'}):
    area.tag_config(TAG_LINK, **setup)
    area.install((-1, '<<LoadData>>', lambda event: hlink(event.widget)))







