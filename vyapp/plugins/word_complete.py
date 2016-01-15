"""
Mode: 0
Event: <Control-q>
Description: Complete word pattern based on all AreaVi instances.
"""

from vyapp.app import root
from time import time


class WordComplete(object):
    """

    """
    def __init__(self, area):
        """
        """

        self.area  = area
        self.seq   = iter(())
        self.snd   = time()
        self.MAX   = 2
        self.index = None

        area.install(('INSERT', '<Control-q>', lambda event: self.complete(event.widget)))
        area.install(('INSERT', '<Key>', lambda event: self.reset(event.widget)))

    def complete(self, area):
        """
        """

        try:
            self.seq
        except AttributeError:
            self.reset()

        try:    
            self.seq.next()
        except StopIteration:
            pass

    def reset(self, area):
        self.seq = area.complete_word(root)

install = WordComplete




