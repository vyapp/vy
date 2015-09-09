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
    

Suppose the cursor is placed at the line 1 and you want to place on nthe string below at the line 3.

    these two

You would type the Key-Command below in NORMAL mode to switch to SCREEN_SEARCH

    <Key-backslash>

Whatever the keys you press in SCREEN_SEARCH mode it will be seen as a search pattern. The search pattern
will appear on the statusbar whenever you press a key. There will happen match attempts whenever a key is
pressed. So, in order to place the cursor over the desired line, one could press the keys to produce the 
following string.

    th se 

That is enough to place the cursor over the desired string. The search pattern would appear on the statusbar.
If you press the key below it will delete a char from the search pattern.

    <BackSpace>

In order to make the cursor jump to the next possible match just press the Key-Command below in SCREEN_SEARCH mode.

    <Tab>

If you want to go back to the previous match just press the command below in SCREEN_SEARCH mode.

    <Control-Tab>

In order to switch to NORMAL mode just press.

    <Escape>

The plugin adds a .+? regex pattern to the search pattern when one presses the key below.

    <Key-space>

In this way, the plugin searches for patterns in the following format over the visible region of the document.

    seq1.+?seq2.+?seq3.+? ...


Key-Commands
============

Mode: NORMAL
Event: <Key-backslash>
Description: Switch to SCREEN_SEARCH mode.

Mode: SCREEN_SEARCH
Event: <Tab>
Description: Place the cursor over the next match.

Mode: SCREEN_SEARCH
Event: <Control-Tab>
Description: Place the cursor over the previous match.

Mode: SCREEN_SEARCH
Event: <BackSpace>
Description: Delete the last char from the search pattern.

Mode: SCREEN_SEARCH
Event: <Key>
Description: Append a char to the search pattern.
"""

from vyapp.plugins.quicksearch import *

class ScreenSearch(QuickSearch):
    def __init__(self, area):
        """

        """
        area.add_mode('SCREEN_SEARCH')
        area.install(('SCREEN_SEARCH', '<Key>', lambda event: self.add_data(event.widget, event.keysym_num)),
                        ('NORMAL', '<Key-backslash>', lambda event: self.start_mode(event.widget)),
                        ('SCREEN_SEARCH', '<Escape>', lambda event: self.clear_data(event.widget)),
                        ('SCREEN_SEARCH', '<BackSpace>', lambda event: self.del_data(event.widget)),
                        ('SCREEN_SEARCH', '<Tab>', lambda event: self.go_down(event.widget)),
                        ('SCREEN_SEARCH', '<Control-Tab>', lambda event: self.go_up(event.widget)),
                        ('SCREEN_SEARCH', '<Key-space>', lambda event: self.data.append('')))


    def start_mode(self, area):
        self.data = ['']
        set_status_msg('')
        area.chmode('SCREEN_SEARCH')

    def start_range(self, area):
        return ('@0,0', area.index('@0,%s' % area.winfo_height()))

    def search_down_range(self, area):
        return ('insert', area.index('@0,%s' % area.winfo_height()))

    def search_up_range(self, area):
        return ('insert', '@0,0')

install = ScreenSearch



