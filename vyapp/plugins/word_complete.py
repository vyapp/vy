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

        area.install(('INSERT', '<Control-q>', lambda event: self.complete()))

    def complete(self):
        """
        """

        if time() - self.snd > self.MAX: 
            self.reset()

        try:
            data = self.seq.next()
        except StopIteration:    
            self.reset()        
        else:
            self.area.delete(self.index, 'insert')
            self.area.insert(self.index, data)
        self.snd = time()


    def reset(self):
        """
        """

        if self.area.compare('insert', '==', 'insert linestart'):
            return

        self.index = self.area.search(' ', 'insert', 
                                      stopindex='insert linestart',regexp=True, 
                                      backwards=True)

        if not self.index: self.index = 'insert linestart'
        else: self.index = '%s +1c' % self.index
        if self.area.compare(self.index, '==', 'insert'): return

        data     = self.area.get(self.index, 'insert')
        self.seq = self.area.find_on_all(root, '%s[^ ]+' % data)

install = WordComplete



