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
        get = Get(events={'<<Data>>': self.next_tab, 
        '<Alt-p>': self.next_tab, 
        '<Alt-o>': self.prev_tab, 
        '<Escape>': self.stop, 
        '<Return>': self.stop})
        return 'break'

    def search_back(self):
        get = Get(events={'<<Data>>': self.prev_tab, 
        '<Alt-p>': self.next_tab, 
        '<Alt-o>': self.prev_tab, 
        '<Escape>': self.stop, 
        '<Return>': self.stop})
        return 'break'

    def stop(self, wid):
        root.note.set_area_focus()
        return True

    def next_tab(self, wid):
        """

        """
        data = wid.get()
        root.note.next(lambda text: data in text)

    def prev_tab(self, wid):
        """

        """
        data = wid.get()
        root.note.back(lambda text: data in text)

    
install = TabSearch


