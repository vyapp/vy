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
    

You would switch to ISEARCh mode by pressing <Key-0> then insert that pattern in the 
input data field and press <Return>. It would place the cursor
on the first occurrence of that pattern that is.

    mellowed to that tender light which heaven to gaudy
    
If there are more occurrences of the set of patterns you can navigate through them 
using Key-Commands. 

The Key-Command <Key-j> places the cursor on the next less possible match. The way
to go back to the previous possible match is using the Key-Command <Key-k>


Key-Commands
============

Mode: NORMAL
Event: <Key-0>
Description: Switch to ISEARCH mode.

Mode: ISEARCH
Event: <Key-j> 
Description: Put the cursor on the next less possible match.

Mode: ISEARCH
Event: <Key-k>
Description: Put the cursor on the previous possible match.
"""

from vyapp.ask import Ask
from vyapp.tools import set_status_msg
from itertools import permutations, product, groupby
from re import escape

class ISearch(object):
    def __init__(self, area):
        """

        """
        area.add_mode('ISEARCH')
        area.install(('NORMAL', '<Key-0>', lambda event: self.set_data(event.widget)),
                        ('ISEARCH', '<Key-j>', lambda event: self.go_down(event.widget)),
                        ('ISEARCH', '<Key-k>', lambda event: self.go_up(event.widget)))


        self.seq   = []
        self.index = -1

    def set_data(self, area):
        """

        """

        self.seq   = []
        self.index = -1
        ask        = Ask(area)
        if not ask.data: return

        data     = ask.data.split(' ')
        find     = lambda ind: area.find(escape(ind), '1.0', step='+1l')
        self.seq = self.match_possible_regions(find, data)

        area.chmode('ISEARCH')

        if not self.seq:
            self.no_match(area)
        else:
            self.go_down(area)
    
    def no_match(self, area):
        set_status_msg('No pattern found!')
        area.chmode('NORMAL')

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


    def go_up(self, area):
        """

        """


        if self.index - 1 < 0: return
        line = self.seq[self.index - 1][1]
        pos0 = '%s.0' % line
        pos1 = '%s.0 lineend' % line
        area.tag_add('sel', pos0, pos1)
        area.seecur(pos0)
        self.index = self.index - 1

    
    def go_down(self, area):
        """

        """
        if self.index + 1 >= len(self.seq): return

        line = self.seq[self.index + 1][1]
        pos0 = '%s.0' % line
        pos1 = '%s.0 lineend' % line
        area.tag_add('sel', pos0, pos1)
        area.seecur(pos0)

        self.index = self.index + 1

install = ISearch









