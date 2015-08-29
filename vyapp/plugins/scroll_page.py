"""
Overview
========

This plugin turns possible to scroll pages.

Usage
=====

Press <Key-q> in NORMAL mode to scroll one page up.
Press <Key-a> in NORMAL mode to scroll one page down.

Key-Commands
============

Mode: NORMAL
Event: <Key-q> 
Description: Scroll a page up.


Mode: NORMAL
Event: <Key-a> 
Description: Scroll one page down.

"""


def install(area):
    area.install(('NORMAL', '<Key-q>', lambda event: event.widget.scroll_page_up()),
                 ('NORMAL', '<Key-a>', lambda event: event.widget.scroll_page_down()))



