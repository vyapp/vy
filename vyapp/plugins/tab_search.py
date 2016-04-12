"""

"""
from vyapp.ask import Ask
from vyapp.app import root

class TabSearch(object):
    def __init__(self, area):
        self.area = area
        area.install(('NORMAL', '<Key-space>', self.start_search))


    def start_search(self, event):
        ask = Ask(self.area, wait=False)
        ask.bindtags(('Entry', ask, '.', 'all'))
        ask.bind('<Control-h>', self.next_tab)
        ask.bind('<Control-l>', self.prev_tab)
        ask.bind('<Key>', self.update_search)

    def update_search(self, event):
        """

        """

        pattern = event.widget.get()
        self.seq = tuple(root.note.find(lambda text: pattern in text))
        self.index = 0
        root.note.select(self.seq[self.index])
        

    def next_tab(self, event):
        """

        """
        if self.index < len(self.index): self.index = self.index + 1

        root.note.select(self.seq[self.index])

    def prev_tab(self, event):
        """

        """
        if self.index > 0: self.index = self.index - 1
        root.note.select(self.seq[self.index])

    
install = TabSearch
