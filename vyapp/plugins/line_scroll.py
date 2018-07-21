"""
Overview
========

This plugin implements Key-Commands to scroll lines.

Key-Commands
============

Namespace: line-scroll

Mode: NORMAL
Event: <Key-w> 
Description: Scroll one line up.


Mode: NORMAL
Event: <Key-s> 
Description: Scroll one line down.
"""
from tkinter import SCROLL

class LineScroll:
    def __init__(self, area):
        area.install('line-scroll', 
        ('NORMAL', '<Key-w>', self.scroll_up),
        ('NORMAL', '<Key-s>', self.scroll_down))

        self.area = area

    def scroll_up(self, event):
        """
        It scrolls one line up
        """

        # should be rewritten.
        # it fails with append.

        self.area.yview(SCROLL, -1, 'units')
        is_visible = self.area.dlineinfo('insert')

        if not is_visible:
            self.area.mark_set('insert', 'insert -1l')

    def scroll_down(self, event):
        """
        It scrolls one line down.
        """

        self.area.yview(SCROLL, 1, 'units')
        is_visible = self.area.dlineinfo('insert')

        if not is_visible:
            self.area.mark_set('insert', 'insert +1l')

install = LineScroll
