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
from tkinter import SCROLL

class PageScroll:
    def __init__(self, area):
        area.install('page-scroll', 
        ('NORMAL', '<Key-Q>', self.scroll_up),
        ('NORMAL', '<Key-A>', self.scroll_down))

        self.area = area

    def scroll_up(self, event):
        """
        It scrolls one page up.
        """

        self.area.yview(SCROLL, -1, 'page')
        self.area.mark_set('insert', '@0,0')

    def scroll_down(self, event):
        """
        It scrolls one page down.
        """

        self.area.yview(SCROLL, 1, 'page')
        self.area.mark_set('insert', '@0,0')


install = PageScroll










