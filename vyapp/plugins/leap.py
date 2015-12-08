"""
Overview
========

Usage
=====

Key-Commands
============

"""

from vyapp.ask import Ask
from re import escape, split
from vyapp.tools import set_status_msg

class Leap(object):

    def __init__(self, area):
        """

        """
        self.area = area
        area.install(('NORMAL', '<Control-backslash>', lambda event: self.start_search()))

    def start_search(self):
        ask = Ask(self.area, wait=False)
        ask.bindtags(('Entry', ask, '.', 'all'))
        ask.bind('<Control-k>', self.search_up)
        ask.bind('<Control-j>', self.search_down)
        ask.bind('<Key>', self.update_search)
        ask.bind('<Destroy>', lambda event: self.area.tag_remove('sel', *self.start_range()))
        set_status_msg('')

    def start_range(self):
        return ('1.0', 'end')

    def search_down_range(self):
        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[-1], 'end')
        else:
            return ('insert', 'end')

    def search_up_range(self):
        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[0], '1.0')
        else:
            return ('insert', '1.0')

    def update_search(self, event):
        """

        """

        pattern = self.make_pattern(event.widget.get())
        set_status_msg('Pattern:%s' % pattern)
        range = self.start_range()
        self.area.tag_remove('sel', *range)
        self.area.pick_next_down('sel', pattern, *range)

    def make_pattern(self, data):
        """

        """

        data    = split(' +', data)
        pattern = ''
        for ind in xrange(0, len(data)-1):
            pattern = pattern + escape(data[ind]) + '.+?'
        pattern = pattern + escape(data[-1])
        return pattern

    def search_up(self, event):
        """

        """

        pattern = self.make_pattern(event.widget.get())
        range = self.search_up_range()
        self.area.tag_remove('sel', *self.start_range())
        self.area.pick_next_up('sel', pattern, *range)

        
    def search_down(self, event):
        """

        """

        pattern = self.make_pattern(event.widget.get())
        range = self.search_down_range()
        self.area.tag_remove('sel', *self.start_range())
        self.area.pick_next_down('sel', pattern, *range)

install = Leap






