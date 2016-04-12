"""

"""
from vyapp.ask import Ask
from vyapp.app import root

class TabSearch(object):
    def __init__(self, area):
        self.area = area
        area.install((-1, '<Control-space>', self.start_search))


    def start_search(self, event):
        ask = Ask(self.area, wait=False)
        self.ask = ask
        ask.bindtags(('Entry', ask, '.', 'all'))
        ask.bind('<Control-k>', self.prev_tab)
        ask.bind('<Control-j>', self.next_tab)
        ask.bind('<Key>', self.update_search)
        ask.bind('<Destroy>', lambda event: root.note.set_area_focus())

    def update_search(self, event):
        """

        """

        pattern    = event.widget.get()
        self.seq   = tuple(root.note.find(lambda text: pattern in text))
        self.index = 0

        # workaround to get back focus to the entry widget. it seems note.select
        # give focus to the child widget when it is selected.
        root.after(30, lambda : self.ask.focus_set())
        root.note.select(self.seq[self.index])
        
    def next_tab(self, event):
        """

        """
        if self.index < len(self.seq) - 1: self.index = self.index + 1
        else: return
        root.after(30, lambda : self.ask.focus_set())
        root.note.select(self.seq[self.index])

    def prev_tab(self, event):
        """

        """
        if self.index > 0: self.index = self.index - 1
        else: return
        root.after(30, lambda : self.ask.focus_set())
        root.note.select(self.seq[self.index])

    
install = TabSearch


