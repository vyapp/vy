"""
Overview
========

Usage
=====

Key-Commands
============

"""

from re import escape
from vyapp.tools import set_status_msg

class QuickSearch(object):

    def __init__(self, area):
        """

        """
        area.add_mode('QUICK_SEARCH')
        area.install(('QUICK_SEARCH', '<Key>', lambda event: self.add_data(event.widget, event.keysym_num)),
                        ('SCREEN_SEARCH', '<F1>', lambda event: self.start_mode(event.widget)),
                        ('QUICK_SEARCH', '<Escape>', lambda event: self.clear_data(event.widget)),
                        ('QUICK_SEARCH', '<BackSpace>', lambda event: self.del_data(event.widget)),
                        ('QUICK_SEARCH', '<Tab>', lambda event: self.go_down(event.widget)),
                        ('QUICK_SEARCH', '<Control-Tab>', lambda event: self.go_up(event.widget)),
                        ('QUICK_SEARCH', '<Key-space>', lambda event: self.data.append('')))


    def start_mode(self, area):
        self.data = ['']
        set_status_msg('')
        area.chmode('QUICK_SEARCH')

    def start_range(self, area):
        return ('1.0', 'end')

    def search_down_range(self, area):
        return ('insert', 'end')

    def search_up_range(self, area):
        return ('insert', '1.0')

    def clear_data(self, area):
        self.data = ['']
        area.tag_remove('sel', *self.start_range(area))

    def add_data(self, area, char):
        """

        """

        try:
            char = chr(char)
        except ValueError:
            return
        else:
            self.data[-1] = self.data[-1] + char

        set_status_msg('Pattern:%s' % '.+?'.join(self.data))
        area.tag_remove('sel', *self.start_range(area))
        area.pick_next_down('sel', self.make_pattern(), *self.start_range(area))
        

    def make_pattern(self):
        data = ''
        for ind in xrange(0, len(self.data)-1):
            data = data + escape(self.data[ind]) + '.+?'
        data = data + self.data[-1]
        return data

    def del_data(self, area):
        """

        """

        self.data[-1] = self.data[-1][:-1]
        if not self.data[-1] and len(self.data) > 1: self.data.pop()

        set_status_msg('Pattern:%s' % '.+?'.join(self.data))
        area.tag_remove('sel', *self.start_range(area))
        area.pick_next_down('sel', self.make_pattern(), *self.start_range(area))

    def go_up(self, area):
        """

        """
        area.tag_remove('sel', *self.start_range(area))
        area.pick_next_up('sel', self.make_pattern(), *self.search_up_range(area))
        
        
    def go_down(self, area):
        """

        """
        area.tag_remove('sel', *self.start_range(area))
        area.pick_next_down('sel', self.make_pattern(), *self.search_down_range(area))



install = QuickSearch









