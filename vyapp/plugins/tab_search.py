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
        get = Get(events={
        '<<Data>>': lambda wid: root.note.switch_next(wid.get()), 
        '<Alt-p>': lambda wid: root.note.switch_next(wid.get(), True), 
        '<Alt-o>': lambda wid: root.note.switch_back(wid.get(), True), 
        '<Escape>': self.stop, 
        '<Return>': self.stop})
        return 'break'

    def search_back(self):
        get = Get(events={
        '<<Data>>': lambda wid: root.note.switch_back(wid.get()), 
        '<Alt-p>': lambda wid: root.note.switch_next(wid.get(), True), 
        '<Alt-o>': lambda wid: root.note.switch_back(wid.get(), True), 
        '<Escape>': self.stop, 
        '<Return>': self.stop})
        return 'break'

    def stop(self, wid):
        root.note.set_area_focus()
        return True

install = TabSearch




