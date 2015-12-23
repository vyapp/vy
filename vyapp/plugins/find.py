"""
Overview
========

This module implements functionalities to find/replace patterns of text in an AreaVi instance
that has focus.


Usage
=====

Key-Commands
============

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
                        ('NORMAL', '<Control-Left>' , lambda event: self.area.tag_add_found(self.TAG_FOUND, self.area.tag_find_ranges('sel', self.regex))),
                        ('NORMAL', '<Shift-Left>' , lambda event: self.area.tag_replace_ranges('sel', self.regex, self.data)),

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
























