"""

"""
from vyapp.ask import Get
from vyapp.app import root

class TabSearch(object):
    def __init__(self, area):
        self.area = area
        area.install('tab-search', 
        (-1, '<Alt-i>', lambda event: self.search_next()),
        (-1, '<Alt-u>', lambda event: self.search_back()))

    def search_next(self):
        get = Get(events={'<<Data>>': self.update_next, 
        '<Alt-p>': self.next_tab, 
        '<Alt-o>': self.prev_tab, 
        '<Escape>': self.stop, 
        '<Return>': self.stop})
        return 'break'

    def search_back(self):
        get = Get(events={'<<Data>>': self.update_back, 
        '<Alt-p>': self.next_tab, 
        '<Alt-o>': self.prev_tab, 
        '<Escape>': self.stop, 
        '<Return>': self.stop})
        return 'break'

    def stop(self, wid):
        root.note.set_area_focus()
        return True

    def update_next(self, wid):
        data = wid.get()
        root.note.next(lambda text: data in text)

    def next_tab(self, wid):
        """

        """
        data = wid.get()
        root.note.next(lambda text: data in text, True)

    def update_back(self, wid):
        data = wid.get()
        root.note.back(lambda text: data in text)

    def prev_tab(self, wid):
        """

        """
        data = wid.get()
        root.note.back(lambda text: data in text, True)

    
install = TabSearch



