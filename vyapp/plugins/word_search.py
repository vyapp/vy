"""
Overview
========

This plugin implements a mechanism of search based on an initial pattern. It takes the
words of the data input then calculates the permutations. The search processes happens
regardless of the punctuation between the words.

Key-Commands
============

Namespace: word-search

Mode: NORMAL
Event: <Key-0>
Description: Switch to ISEARCH mode.

Event: <Alt-p> 
Description: Put the cursor on the next less possible match.

Event: <Alt-o>
Description: Put the cursor on the previous possible match.
"""

from vyapp.ask import Get
from itertools import permutations, product, groupby
from re import escape
from vyapp.app import root

class WordSearch(object):
    def __init__(self, area, setup={'background':'yellow', 'foreground':'black'}):
        self.area = area
        area.tag_configure('(ISEARCH_MATCH)', **setup)
        area.install('word-search', ('NORMAL', '<Key-0>', lambda event: 
        Get(events={
        '<Return>' : self.start, 
        '<Alt-p>'  : lambda wid: self.go_down(), 
        '<Alt-o>'  : lambda wid: self.go_up(), 
        '<Destroy>': lambda wid: self.area.tag_remove(
        '(ISEARCH_MATCH)', '1.0', 'end'),
        '<Escape> ': lambda wid: True})))

        self.seq   = []
        self.index = -1

    def start(self, wid):
        """

        """

        self.seq   = []
        self.index = -1
        data       = wid.get().split(' ')
        find       = lambda ind: self.area.find(
        escape(ind), '1.0', step='+1l linestart')

        self.seq = self.match_possible_regions(find, data)

        if not self.seq:
            self.no_match()
        else:
            self.go_down()
    
    def no_match(self):
        root.status.set_msg('No pattern found!')

    def match_possible_regions(self, find, data):
        regions = []

        for ind in data:
            for ch, index0, index1 in find(ind):
                regions.append((int(index0.split('.')[0]),  ch))

        regions.sort()
        seq = groupby(regions, lambda ind: ind[0])
        matches = self.sort_possible_matches(seq, data)
        return matches

    def sort_possible_matches(self, seq, data):
        matches = []

        for line, group in seq:
            count = 0
            for line, word in group:
                if word in data:
                    count = count + 1
            matches.append((count, line))
        matches.sort(reverse=True)
        return matches

    def go_up(self):
        """

        """


        if self.index - 1 < 0: return
        line = self.seq[self.index - 1][1]
        pos0 = '%s.0' % line
        pos1 = '%s.0 lineend' % line
        self.area.tag_remove('(ISEARCH_MATCH)', '1.0', 'end')
        self.area.tag_add('(ISEARCH_MATCH)', pos0, pos1)
        self.area.seecur(pos0)
        self.index = self.index - 1
    
    def go_down(self):
        """

        """
        if self.index + 1 >= len(self.seq): return
        line = self.seq[self.index + 1][1]
        pos0 = '%s.0' % line
        pos1 = '%s.0 lineend' % line
        self.area.tag_remove('(ISEARCH_MATCH)', '1.0', 'end')
        self.area.tag_add('(ISEARCH_MATCH)', pos0, pos1)
        self.area.seecur(pos0)

        self.index = self.index + 1

install = WordSearch







