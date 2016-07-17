"""

"""
from vyapp.ask import Get
from vyapp.app import root

class TabSearch(object):
    def __init__(self, area):
        self.area = area
        area.install((-1, '<Alt-i>', lambda event: self.start_search()))


    def start_search(self):
        get = Get(self.area, events={'<<Data>>': self.update_search, '<Alt-p>': self.next_tab, 
                    '<Control-j>': self.next_tab, '<Alt-o>': self.prev_tab, '<Control-k>': self.prev_tab, 
                                '<Escape>': lambda data: self.stop_search(), '<Return>': lambda data: self.stop_search()})
        return 'break'

    def stop_search(self):
        root.note.set_area_focus()
        return True

    def update_search(self, data):
        """

        """

        self.seq   = tuple(root.note.find(lambda text: data in text))
        self.index = 0

        root.note.on(self.seq[self.index])
        
    def next_tab(self, data):
        """

        """
        self.index = self.index + 1 if self.index < len(self.seq) - 1 else self.index
        root.note.on(self.seq[self.index])

    def prev_tab(self, data):
        """

        """
        self.index = self.index - 1 if self.index > 0 else self.index
        root.note.on(self.seq[self.index])

    
install = TabSearch




