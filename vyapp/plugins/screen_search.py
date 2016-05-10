"""
Overview
========

This mode permits one to quickly switch the cursor to a desired position. It uses a kind of fuzzy search to attempt to match
a sequence of keystrokes with the visible region of the document. 

Usage
=====

Consider the following text below.

    1 The text contains hyperlinks between the two parts, allowing you to quickly
    2 jump between the description of an editing task and a precise explanation of
    3 the commands and options used for it.  Use these two commands:
    

Suppose the cursor is placed at the line 1 and you want to place the cursor on the string below at the line 3:

    these two

You would type the Key-Command below in NORMAL mode:

    <Key-g>

Try typing something, you'll notice the incremental search process. The search pattern
will appear on the statusbar whenever you press a key. There will happen match attempts whenever a key is
pressed. So, in order to place the cursor over the desired line, one could press the keys to produce the 
following string.

    th se 

That is enough to place the cursor over the desired string. The search pattern would appear on the statusbar.
If you press the key below it will delete a char from the search pattern.

    <BackSpace>

In order to make the cursor jump to the next possible match just press the Key-Command below in SCREEN_SEARCH mode.

    <Control-j>

If you want to go back to the previous match just press the command below in SCREEN_SEARCH mode.

    <Control-k>

In order to switch to NORMAL mode just press.

    <Escape>

The plugin adds a .+? regex pattern to the search pattern when one presses the key below.

    <Key-space>

In this way, the plugin searches for patterns in the following format over the visible region of the document.

    seq1.+?seq2.+?seq3.+? ...


Key-Commands
============

Mode: NORMAL
Event: <Key-g>
Description: Switch to SCREEN_SEARCH mode.

Event: <Control-j>
Description: Place the cursor over the next match.

Event: <Control-k>
Description: Place the cursor over the previous match.
"""

from vyapp.plugins.quick_search import QuickSearch

class ScreenSearch(QuickSearch):
    def __init__(self, area):
        """

        """
        self.area = area
        area.install(('NORMAL', '<Key-g>', lambda event: self.start_search()))

    def start_range(self):
        return ('@0,0', self.area.index('@0,%s' % self.area.winfo_height()))

    def range_down(self):
        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[-1], self.area.index('@0,%s' % self.area.winfo_height()))
        else:
            return ('insert', self.area.index('@0,%s' % self.area.winfo_height()))

    def range_up(self):
        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[0], '@0,0')
        else:
            return ('insert', '@0,0')

install = ScreenSearch




