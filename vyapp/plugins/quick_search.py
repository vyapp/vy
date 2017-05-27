"""

Key-Commands
============

Namespace: quick-search
"""

from vyapp.ask import Get
from vyapp.regutils import build_regex
from vyapp.app import root

class QuickSearch(object):
    TAGCONF = {'(SEARCH_MATCH)' : {
    'background':'yellow', 'foreground':'black'}}

    def __init__(self, area, nocase=True):

        """

        """
        self.area   = area
        self.nocase = nocase
        area.tags_config(self.TAGCONF)

        area.install('quick-search',
        ('NORMAL', '<Key-q>', self.start_backwards),
        ('NORMAL', '<Key-a>', self.start_forwards))

    def start_forwards(self, event):
        self.index     = self.area.index('insert')
        self.stopindex = 'end'
        self.backwards = False

        Get(events = {
        '<Alt-p>':self.search_down, 
        '<Alt-o>': self.search_up, 
        '<<Data>>': self.update, 
        '<BackSpace>': self.update,
        '<Destroy>': lambda wid: self.area.tag_remove(
        '(SEARCH_MATCH)', '1.0', 'end'),
        '<Escape>':  lambda wid: True})

    def start_backwards(self, event):
        self.index     = self.area.index('insert')
        self.backwards = True
        self.stopindex = '1.0'

        Get(events = {
        '<Alt-p>':self.search_down, 
        '<Alt-o>': self.search_up, 
        '<<Data>>': self.update, 
        '<BackSpace>': self.update,
        '<Destroy>': lambda wid: self.area.tag_remove(
        '(SEARCH_MATCH)', '1.0', 'end'),
        '<Escape>':  lambda wid: True})

    def update(self, wid):
        """

        """
        data    = wid.get()
        pattern = build_regex(data)
        root.status.set_msg('Pattern:%s' % pattern)
        self.area.ipick('(SEARCH_MATCH)', pattern,
        verbose=True, backwards=self.backwards, index=self.index, 
        nocase=self.nocase, stopindex=self.stopindex)

    def search_up(self, wid):
        """

        """
        data    = wid.get()
        pattern = build_regex(data)
        self.area.ipick('(SEARCH_MATCH)', pattern, index='insert', 
        nocase=self.nocase, stopindex='1.0', backwards=True)

    def search_down(self, wid):
        """

        """
        data    = wid.get()
        pattern = build_regex(data)
        self.area.ipick('(SEARCH_MATCH)', pattern, nocase=self.nocase, 
        stopindex='end', index='insert')


install = QuickSearch


