"""
Overview
========

This plugin turns possible to scroll pages.

Key-Commands
============

Namespace: page-scroll

Mode: NORMAL
Event: <Key-Q> 
Description: Scroll a page up.


Mode: NORMAL
Event: <Key-A> 
Description: Scroll one page down.

"""


def install(area):
    area.install('page-scroll', ('NORMAL', '<Key-Q>', lambda event: event.widget.scroll_page_up()),
                 ('NORMAL', '<Key-A>', lambda event: event.widget.scroll_page_down()))








