"""

"""

from vyapp.ask import Get
from vyapp.tools import set_status_msg
from vyapp.regutils import build_regex

class QuickSearch(object):
    def __init__(self, area, setup={'background':'yellow', 'foreground':'black'}):
        """

        """
        self.area = area
        area.tag_configure('(SEARCH_MATCH)', **setup)
        area.install(('NORMAL', '<Key-backslash>', 
        lambda event: self.start_search()))

    def start_search(self):
        ask = Get(self.area, events = {'<Alt-p>':self.search_down, 
        '<Alt-o>': self.search_up, 
        '<Control-j>': self.search_down,     
        '<Control-k>': self.search_up, 
        '<<Data>>':self.update_search, 
        '<BackSpace>': self.update_search,
        '<Return>': lambda wid: self.stop_search(), 
        '<Escape>': lambda wid: self.stop_search()})

        set_status_msg('')

    def stop_search(self):
        self.area.tag_remove('(SEARCH_MATCH)', *self.start_range())
        return True

    def start_range(self):
        return ('1.0', 'end')
        
    def range_down(self):
        """
        This method return the range to be searched that is down to the cursor position.
        """

        ranges = self.area.tag_ranges('(SEARCH_MATCH)')
        if ranges:
            return (ranges[-1], 'end')
        else:
            return ('insert', 'end')

    def range_up(self):
        """
        The range to be searched up to the cursor position.
        """

        ranges = self.area.tag_ranges('(SEARCH_MATCH)')
        if ranges:
            return (ranges[0], '1.0')
        else:
            return ('insert', '1.0')

    def update_search(self, wid):
        """

        """
        data    = wid.get()
        pattern = build_regex(data)
        range   = self.start_range()
        set_status_msg('Pattern:%s' % pattern)
        self.area.pick_next_down('(SEARCH_MATCH)', pattern, *range)

    def search_up(self, wid):
        """

        """
        data    = wid.get()
        pattern = build_regex(data)
        range   = self.range_up()
        self.area.pick_next_up('(SEARCH_MATCH)', pattern, *range)
        
    def search_down(self, wid):
        """

        """
        data    = wid.get()
        pattern = build_regex(data)
        range   = self.range_down()
        self.area.pick_next_down('(SEARCH_MATCH)', pattern, *range)

install = QuickSearch



