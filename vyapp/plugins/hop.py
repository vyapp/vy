"""
Overview
========

"""

from vyapp.plugins.leap import Leap

class Hop(Leap):
    def __init__(self, area):
        """

        """
        self.area = area
        area.install(('NORMAL', '<Key-backslash>', lambda event: self.start_search()))

    def start_range(self):
        return ('@0,0', self.area.index('@0,%s' % self.area.winfo_height()))

    def search_down_range(self):
        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[-1], self.area.index('@0,%s' % self.area.winfo_height()))
        else:
            return ('insert', self.area.index('@0,%s' % self.area.winfo_height()))


    def search_up_range(self):
        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[0], '@0,0')
        else:
            return ('insert', '@0,0')

install = Hop








