"""
Overview
========

This module implements functionalities to find/replace patterns of text in an AreaVi instance
that has focus.

Usage
=====

In order to start a search it is needed to set a pattern, it is done with the keycommand 
<Control-q> in NORMAL mode. After having set a search pattern it is possible to set a 
replacement for the pattern by using the keycommand <Control-Q> in NORMAL mode.

The keycommands <Control-Up> and <Control-Down> in NORMAL mode are used to pick the next and previous
occurrence of the pattern from the cursor position. 

It is possible to replace the next occurrence of the pattern for its replacement by issuing
the keycommand <Control-Right> in NORMAL mode. The next match from the cursor position will be replaced.

The keycommands <Shift-Up> and <Shift-Down> in NORMAL mode are used to replace all occurrences of the pattern for its
replacement that occurs upward and downward from the cursor position. The keycommand <Shift-Right> would
replace all the occurrences.

It is possible to perform searches/replacements inside regions of text that are selected.
The keycommand <Control-Left> in NORMAL mode will highligh all matched patterns in regions of text that are
selected. In order to perform replacement for these patterns, issue the keycommand <Shift-Left> in NORMAL mode.

The ranges of text that corresponds to a match get highlighed, press <Key-Q> in NORMAL mode
to remove the highligh from matched patterns.

Key-Commands
============

Mode: NORMAL
Event: <Control-q>
Description: Set a search pattern.

Mode: NORMAL
Event: <Control-Q>
Description: Set a replacement pattern.

Mode: NORMAL
Event: <Control-Up>
Description: Pick the previous pattern from the cursor position.

Mode: NORMAL
Event: <Shift-Up>
Description: Replace all occurrences upwards.

Mode: NORMAL
Event: <Shift-Down>
Description: Replace all occurrences downwards.

Mode: NORMAL
Event: <Shift-Right>
Description: Replace all occurrences.

Mode: NORMAL
Event: <Control-Down>
Description: Pick the next pattern from the cursor position.

Mode: NORMAL
Event: <Control-Right>
Description: Replace the next matched pattern for the previously set replacement.

Mode: NORMAL
Event: <Control-Left>
Description: Highligh all matched patterns inside a selected region of text.

Mode: NORMAL
Event: <Shift-Left>
Description: Replace all matched patterns inside a selected region of text for the
previously set replacement.

Mode: NORMAL
Event: <Key-Q>
Description: It removes highligh from all matched patterns.
"""

from vyapp.ask import *

class Find(object):
    def __init__(self, area, setup={'background':'blue', 'foreground':'yellow'}):
        self.area         = area
        self.regex        = ''
        self.data         = ''
        self.TAG_FOUND    = '__found__'

        area.tag_config(self.TAG_FOUND, **setup)

        area.install(('NORMAL', '<Control-q>'    , lambda event: self.set_regex()),
                        ('NORMAL', '<Control-Q>'    , lambda event: self.set_data()),
                        ('NORMAL', '<Key-Q>'        , lambda event: self.area.tag_remove(self.TAG_FOUND, '1.0', 'end')),
                        ('NORMAL', '<Control-Left>' , lambda event: self.area.map_matches(self.TAG_FOUND, self.area.collect('sel', self.regex))),
                        ('NORMAL', '<Shift-Left>' , lambda event: self.area.replace_ranges('sel', self.regex, self.data)),
                        ('NORMAL', '<Control-Right>', lambda event: self.area.replace(self.regex, self.data, 'insert')),
                        ('NORMAL', '<Shift-Up>'     , lambda event: self.area.replace_all(self.regex, self.data, '1.0', 'insert')),
                        ('NORMAL', '<Shift-Right>'  , lambda event: self.area.replace_all(self.regex, self.data)),
                        ('NORMAL', '<Shift-Down>'   , lambda event: self.area.replace_all(self.regex, self.data, 'insert', 'end')),
                        ('NORMAL', '<Control-Up>'   , lambda event: self.area.pick_next_up(self.TAG_FOUND, self.regex)),
                        ('NORMAL', '<Control-Down>' , lambda event: self.area.pick_next_down(self.TAG_FOUND, self.regex)))



    def set_regex(self):
        ask = Ask(self.area, self.regex)
        self.regex = ask.data

        # self.regex = self.area.get_ranges('sel')

    def set_data(self):
        ask = Ask(self.area,  self.data)
        self.data = ask.data

        # self.data = self.area.get_ranges('sel')


install = Find




