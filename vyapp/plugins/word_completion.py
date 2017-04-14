"""
Overview
========

This plugin does word completion.


Key-Commands
============

Namespace: word-completion

Mode: INSERT
Event: <Control-q>
Description: Open the completion window with possible words for
completion.

"""

from vyapp.completion import CompletionWindow, Option
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.app import root
import sys

class WordCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        pattern     = area.get_seq()
        completions = map(lambda ind: ind[1][0], 
        area.find_all(root, '[^ ]*%s[^ ]*' % pattern 
        if pattern else '[^ ]+', nocase=True))

        completions = set(completions)
        completions = map(lambda ind: 
        Option(ind), completions)

        CompletionWindow.__init__(self, area, 
        completions, *args, **kwargs)

def install(area):
    area.install('word-completion', ('INSERT', '<Control-q>', 
    lambda event: WordCompletionWindow(event.widget)))










