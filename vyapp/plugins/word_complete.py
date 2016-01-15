"""
Mode: 0
Event: <Control-q>
Description: Complete word pattern based on all AreaVi instances.
"""

from vyapp.app import root


class WordComplete(object):
    """

    """
    def __init__(self, area):
        """
        """

        area.install(('INSERT', '<Control-q>', lambda event: self.complete(event.widget)))
        area.install(('INSERT', '<Control_R>', lambda event: self.reset(event.widget)))
        area.install(('INSERT', '<Control_L>', lambda event: self.reset(event.widget)))

    def complete(self, area):
        """
        """

        try:    
            self.seq.next()
        except StopIteration:
            pass

    def reset(self, area):
        self.seq = area.complete_word(root)

install = WordComplete





