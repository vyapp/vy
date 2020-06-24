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
Event: <Key-M>
Description: Ask for a pattern to search.

Event: <Key-V> 
Mode: NORMAL
Description: Display previous matches.

"""

from vyapp.widgets import LinePicker
from vyapp.ask import Ask
from itertools import groupby
from re import escape
from vyapp.app import root

class WordSearch:
    options = LinePicker()

    def __init__(self, area):
        self.area = area

        area.install('word-search', 
        ('NORMAL', '<Key-M>', self.match),
        ('NORMAL', '<Key-V>', self.display_matches))

    def display_matches(self, event):
        self.options.display()
        root.status.set_msg('Word Search matches!')

    def match(self, event):
        """

        """

        ask  = Ask()
        data = ask.data.split(' ')
        find = lambda ind: self.area.find(
        escape(ind).lower(), '1.0', step='+1l linestart')

        seq     = self.match_regions(find, data)
        matches = ((self.area.filename, line, 
            self.area.get_line('%s.0' % line)) 
                for count, line in seq)

        if not seq:
            root.status.set_msg('No pattern found!')
        else:
            self.options(matches)

    def match_regions(self, find, data):
        regions = []
    
        for ind in data:
            for ch, index0, index1 in find(ind):
                regions.append((int(index0.split('.')[0]),  ch))

        regions.sort()
        seq = groupby(regions, lambda ind: ind[0])
        matches = self.sort_matches(seq, data)
        return matches

    def sort_matches(self, seq, data):
        matches = []

        for line, group in seq:
            count = 0
            for line, word in group:
                if word in data:
                    count = count + 1
            matches.append((count, line))
        matches.sort(reverse=True)
        return matches

install = WordSearch

