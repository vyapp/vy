"""
Overview
========

This module implements functionalities to find/replace patterns of text in an AreaVi instance
that has focus.

Usage
=====

In order to perform searches it is needed to press <Alt-slash> in NORMAL mode. It will show up
an input field where to insert tcl regex patterns. 

Once inserting the pattern then it is possible to find the next/previous occurrence
of the pattern by pressing <Alt-p>, <Alt-o> in the input text field
that is a Get widget.

For replacements, it is needed to first set a text in NORMAL mode by pressing <Alt-bracketright>.
Once the replacement is set then press <Alt-slash> to initiate the search process. Use <Alt-period>
to replace the current picked pattern of text and <Alt-comma> to replace all matched patterns.

It is possible to perform searches over selected regions of text, for such, select a region of text
then press <Alt-slash> and <Alt-b> to highligh all matched patterns in the region of text. In order
to replace all matched patterns inside a region of text, use <Alt-semicolon>.

Key-Commands
============

Mode: NORMAL
Event: <Alt-slash>
Description: Set a search pattern.

Mode: NORMAL
Event: <Alt-bracketright>
Description: Set a replacement pattern.

Mode: Get
Event: <Alt-o>
Description: Pick the previous pattern from the cursor position.

Mode: Get
Event: <Alt-comma>
Description: Replace all occurrences.

Mode: Get
Event: <Alt-p>
Description: Pick the next pattern from the cursor position.

Mode: Get
Event: <Alt-period>
Description: Replace the next matched pattern for the previously set replacement.

Mode: Get
Event: <Alt-b>
Description: Highligh all matched patterns inside a selected region of text.

Mode: Get
Event: <Alt-semicolon>
Description: Replace all matched patterns inside a selected region of text for the
previously set replacement.

"""

from vyapp.ask import Get, Ask

class Find(object):
    def __init__(self, area, setup={'background':'green', 'foreground':'white'}):
        self.area  = area
        self.data  = ''
        self.index = None
        self.regex = ''

        area.tag_config('(CATCHED)', **setup)

        area.install(('NORMAL', '<Alt-slash>'    , lambda event: self.start()), 
                     ('NORMAL', '<Alt-bracketright>'    , lambda event: self.set_data()))


    def start(self):
        self.index = ('insert', 'insert')
        get = Get(self.area, events={'<Alt-o>': self.up, '<Escape>': self.stop, 
                                     '<Alt-p>': self.down, '<Return>': self.stop,
                                     '<Alt-b>': lambda regex: self.area.map_matches('(CATCHED)', self.area.collect('sel', regex)),
                                     '<Alt-period>': lambda regex: self.area.replace(regex, self.data, self.index[0]),
                                     '<Alt-semicolon>': lambda regex: self.area.replace_ranges('sel', regex, self.data), 
                                     '<Alt-comma>': lambda regex: self.area.replace_all(regex, self.data, '1.0', 'end')}, default_data=self.regex)
    def set_data(self):
        ask = Ask(self.area, default_data = self.data)
        self.data = ask.data

    def stop(self, regex):
        self.regex = regex
        self.area.tag_remove('(CATCHED)', '1.0', 'end')
        return True

    def up(self, regex):
        index = self.area.pick_next_up('(CATCHED)', regex, self.index[0])
        self.index = ('insert', 'insert') if not index else index

    def down(self, regex):
        index = self.area.pick_next_down('(CATCHED)', regex, self.index[1])
        self.index = ('insert', 'insert') if not index else index

install = Find





