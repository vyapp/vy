"""
Overview
========

Usage
=====

Key-Commands
============

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


