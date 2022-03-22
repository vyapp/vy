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
from vyapp.plugins import Namespace

class LineScrollNS(Namespace):
    pass

class LineScroll:
    def __init__(self, area):
        area.install(LineScrollNS, 
        (-1, '<Alt-period>', self.scroll_up),
        (-1, '<Alt-comma>', self.scroll_down))

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
        return 'break'

    def scroll_down(self, event):
        """
        It scrolls one line down.
        """

        self.area.yview(SCROLL, 1, 'units')
        is_visible = self.area.dlineinfo('insert')

        if not is_visible:
            self.area.mark_set('insert', 'insert +1l')
        return 'break'

install = LineScroll
