"""

"""

from vyapp.ask import Get
from re import escape, split
from vyapp.tools import set_status_msg

class QuickSearch(object):
    def __init__(self, area):
        """

        """
        self.area = area
        area.install(('NORMAL', '<Key-backslash>', lambda event: self.start_search()))

    def start_search(self):
        ask = Get(self.area, on_next=self.search_down, on_prev=self.search_up, on_data=self.update_search, 
                            on_done=lambda data: self.area.tag_remove('sel', *self.start_range()))
        set_status_msg('')

    def start_range(self):
        return ('1.0', 'end')

    def range_down(self):
        """
        This method return the range to be searched that is down to the cursor position.
        """

        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[-1], 'end')
        else:
            return ('insert', 'end')

    def range_up(self):
        """
        The range to be searched up to the cursor position.
        """

        ranges = self.area.tag_ranges('sel')
        if ranges:
            return (ranges[0], '1.0')
        else:
            return ('insert', '1.0')

    def update_search(self, data):
        """

        """

        pattern = self.make_pattern(data)
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

    def search_up(self, data):
        """

        """

        pattern = self.make_pattern(data)
        range = self.range_up()
        self.area.tag_remove('sel', *self.start_range())
        self.area.pick_next_up('sel', pattern, *range)

        
    def search_down(self, data):
        """

        """

        pattern = self.make_pattern(data)
        range = self.range_down()
        self.area.tag_remove('sel', *self.start_range())
        self.area.pick_next_down('sel', pattern, *range)

install = QuickSearch






