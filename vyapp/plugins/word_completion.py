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
from vyapp.app import root

class WordCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        pattern     = area.get(*area.get_seq_range())
        completions = [ind[1][0] for ind in area.find_all(root, '[^ ]*%s[^ ]*' % pattern 
        if pattern else '[^ ]+', nocase=True)]

        completions = set(completions)
        completions = [Option(ind) for ind in completions]

        CompletionWindow.__init__(self, area, 
        completions, *args, **kwargs)

def install(area):
    area.install('word-completion', ('INSERT', '<Control-q>', 
    lambda event: WordCompletionWindow(event.widget)))











