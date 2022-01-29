"""
Overview
========

This plugin implements incremental search which is handy to quickly
jump to specific positions of the text.

Key-Commands
============

Namespace: quick-search


"""

from vyapp.ask import Get
from vyapp.regutils import build_regex
from vyapp.stderr import printd
from vyapp.app import root
from tkinter import Listbox, Toplevel,  BOTH, END, TOP, ACTIVE, Text, LEFT, SCROLL
from vyapp.plugins import Namespace

class QuickSearchNS(Namespace):
    pass

class QuickSearch:
    confs = {
        'background':'yellow', 'foreground':'black'
    }

    def __init__(self, area, nocase=True):
        self.area   = area
        self.nocase = nocase
        area.tag_config('(SEARCH_MATCH)', self.confs)

        area.install(QuickSearchNS,
        (-1, '<Alt-k>', self.start_backwards),
        (-1, '<Alt-j>', self.start_forwards))

    @classmethod
    def c_appearance(cls, **confs):
        """
        Used to set matched region properties. These properties
        can be background, foreground etc. 

        Check Tkinter Text widget documentation on tags for more info.
        """

        cls.confs.update(confs)
        printd('Quick Search - Setting confs = ', cls.confs)

    def start_forwards(self, event):
        self.index     = self.area.index('insert')
        self.stopindex = 'end'
        self.backwards = False

        Get(events = {
        '<Alt-p>':self.search_down, 
        '<Alt-o>': self.search_up, 
        '<Alt-s>': self.clear_pattern, 
        '<<Data>>': self.update, 
        '<BackSpace>': self.update,
        '<Escape>':  self.end_search})
        return 'break'

    def end_search(self, wid):
        self.area.tag_remove('(SEARCH_MATCH)', '1.0', 'end')
        return True

    def clear_pattern(self, wid):
        wid.delete(0, END)
        self.index = self.area.index('insert')

    def start_backwards(self, event):
        self.index     = self.area.index('insert')
        self.backwards = True
        self.stopindex = '1.0'

        Get(events = {
        '<Alt-p>':self.search_down, 
        '<Alt-o>': self.search_up, 
        '<Alt-s>': self.clear_pattern, 
        '<<Data>>': self.update, 
        '<BackSpace>': self.update,
        '<Escape>':  self.end_search})
        return 'break'

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
        self.area.ipick('(SEARCH_MATCH)', pattern, 
        nocase=self.nocase, stopindex='end', index='insert')


install = QuickSearch

