"""
Overview
========

Key-Commands
============

Namespace: tab-search

"""

from vyapp.ask import Get
from vyapp.app import root

class TabSearch:
    def __init__(self, area):
        self.area = area

        area.install('tab-search', 
        (-1, '<Alt-i>', self.on_next_mode),
        (-1, '<Alt-u>', self.on_back_mode))

    def on_next_mode(self, event):
        get = Get(events={'<<Data>>': self.switch_next, 
        '<Alt-p>': self.switch_next, 
        '<Alt-o>': self.switch_back, 
        '<Escape>': self.stop, 
        '<Return>': self.stop})

        return 'break'

    def on_back_mode(self, event):
        get = Get(events={
        '<<Data>>': self.switch_back, 
        '<Alt-p>': self.switch_next, 
        '<Alt-o>': self.switch_back, 
        '<Escape>': self.stop, 
        '<Return>': self.stop})

        return 'break'

    def switch_next(self, wid):
        """
        """
        data = wid.get()
        seq  = root.note.next(lambda text: data in text)
        elem = next(seq)
        root.note.on(elem)

        wid  = root.note.nametowidget(root.note.select())
        root.title('Vy %s' % wid.focused_area.filename)

    def switch_back(self, wid):
        """
        """

        data = wid.get()
        seq  = root.note.back(lambda text: data in text)
        elem = next(seq)
        root.note.on(elem)

        wid  = root.note.nametowidget(root.note.select())
        root.title('Vy %s' % wid.focused_area.filename)

    def stop(self, wid):
        root.note.set_area_focus()
        return True

install = TabSearch



