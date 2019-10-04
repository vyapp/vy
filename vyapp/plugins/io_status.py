"""
Overview
========

Update statusbar when a given AreaVi instance load/save data from disk. 
It also updates the statusbar mode field.
"""

from vyapp.app import root
from os.path import basename

class IOStatus:
    def __init__(self, area):
        self.area = area
        area.install('io-status', 
        (-1, '<Escape>', self.clear_statusbar),
        (-1, '<<SaveData>>', self.update_title), 
        (-1, '<<LoadData>>', self.update_title),
        (-1, '<<ClearData>>', self.update_title),
        (-1, '<FocusIn>', self.update_title),
        (-1, '<<SaveData>>', self.update_tabname),
        (-1, '<<LoadData>>', self.update_tabname),
        (-1, '<<ClearData>>', self.update_tabname),
        (-1, '<FocusIn>', self.update_tabname), 
        (-1, '<FocusIn>', self.update_mode),
        (-1, '<<Chmode>>', self.update_mode))

    def clear_statusbar(self, event):
        root.status.set_msg('')

    def update_title(self, event):
        root.title('Vy %s' % self.area.filename)

    def update_tabname(self, event):
        root.note.tab(self.area.master.master.master,
        text=basename(self.area.filename))

    def update_mode(self, event):
        root.status.set_mode(self.area.id)

install = IOStatus

