"""

"""
from vyapp.ask import Get
from vyapp.app import root

class TabSearch(object):
    def __init__(self, area):
        self.area = area
        area.install((-1, '<Alt-i>', lambda event: self.start_search()))


    def start_search(self):
        get = Get(self.area, on_data=self.update_search, on_next=self.next_tab, 
                    on_prev=self.prev_tab, on_done=lambda data: root.note.set_area_focus())
        return 'break'

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



