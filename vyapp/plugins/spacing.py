"""
Overview
========

Used to insert tabs based on the type of file being edited.

Key-Commands
============

Namespace: spacing

Mode: INSERT
Event: <Tab>
Description: Insert a tab/space based on the programming file type.

"""

from os.path import splitext
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

class Tab(object):
    DEFAULT_SIZE, DEFAULT_CHAR = 4, ' '
    SCHEME, SIZE, CHAR         = {}, 4, ' '

    def __init__(self, area):
        self.area = area
        area.install('spacing', 
        (-1, '<<LoadData>>', self.set_tab_scheme),
        (-1, '<<SaveData>>', self.set_tab_scheme),
        (-1, '<<ClearData>>', self.set_tab_scheme),
        ('INSERT', '<Tab>', lambda event: 
        self.insert_tab(event.widget)))
    
    def set_tab_scheme(self, event):
        ph, ext = splitext(self.area.filename.lower())
        opt     = self.SCHEME.get(
        ext, (self.DEFAULT_SIZE, self.DEFAULT_CHAR))

        Tab.SIZE, Tab.CHAR = opt

    def insert_tab(self, area):
        area.edit_separator()
        data = self.CHAR * self.SIZE

        area.insert('insert', data)
        return 'break'

def tabset(size, char=Tab.CHAR):
    """
    Change tab size/char globally based
    on the actual areavi filename extension.
    """

    ph, ext = splitext(
    AreaVi.ACTIVE.filename.lower())
    Tab.SCHEME[ext]    = size, char
    Tab.SIZE, Tab.CHAR = size, char

ENV['tabset'] = tabset
install = Tab


