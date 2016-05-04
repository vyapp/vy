"""
Overview
========

This plugin implements a mechanism of search based on an initial pattern. It takes the
words of the data input then calculates the permutations. The search processes happens
regardless of the punctuation between the words.

Usage
=====

Consider the following text below, suppose it is somewhere inside a big file.

    She walks in beauty, like the night Of cloudless climes and starry skies;
    And all thats best of dark and bright meet in her aspect and her eyes;
    Thus mellowed to that tender light which heaven to gaudy day denies.

What you wanted to place the cursor over a line that appears the words?

    gaudy that mellow
    

You would open an input box dialog by pressing <Key-0> in NORMAL mode then insert that pattern in the 
input box field and press <Return>. It would place the cursor
on the first occurrence of that pattern that is.

    mellowed to that tender light which heaven to gaudy
    
If there are more occurrences of the set of patterns you can navigate through them 
using Key-Commands. 

The Key-Command <Control-j> places the cursor on the next less possible match. The way
to go back to the previous possible match is using the Key-Command <Control-k>


Key-Commands
============

Mode: NORMAL
Event: <Key-0>
Description: Switch to ISEARCH mode.

Event: <Control-j> 
Description: Put the cursor on the next less possible match.

Event: <Control-k>
Description: Put the cursor on the previous possible match.
"""

from vyapp.ask import Edit
from vyapp.tools import set_status_msg
from itertools import permutations, product, groupby
from re import escape

class ISearch(object):
    def __init__(self, area):
        self.area = area
        area.install(('NORMAL', '<Key-0>', lambda event: 
             Edit(area, on_data=self.start, on_next=lambda data: 
                 self.go_down(), on_prev=lambda data: self.go_up(), 
                     on_done=lambda data: self.area.tag_remove('sel', '1.0', 'end'))))

        self.seq   = []
        self.index = -1

    def start(self, data):
        """

        """

        self.seq   = []
        self.index = -1
        data       = data.split(' ')
        find       = lambda ind: self.area.find(escape(ind), '1.0', step='+1l linestart')
        self.seq   = self.match_possible_regions(find, data)
        if not self.seq:
            self.no_match()
        else:
            self.go_down()
    
    def no_match(self):
        set_status_msg('No pattern found!')

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
        self.area.tag_remove('sel', '1.0', 'end')
        self.area.tag_add('sel', pos0, pos1)
        self.area.seecur(pos0)
        self.index = self.index - 1

    
    def go_down(self):
        """

        """
        if self.index + 1 >= len(self.seq): return

        line = self.seq[self.index + 1][1]
        pos0 = '%s.0' % line
        pos1 = '%s.0 lineend' % line
        self.area.tag_remove('sel', '1.0', 'end')
        self.area.tag_add('sel', pos0, pos1)
        self.area.seecur(pos0)

        self.index = self.index + 1

install = ISearch


