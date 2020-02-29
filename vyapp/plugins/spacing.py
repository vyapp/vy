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

from vyapp.plugins import Command
from os.path import splitext
from vyapp.app import root

class Tab:
    scheme = {}

    def __init__(self, area):
        self.area = area
        area.install('spacing', (-1, '<<LoadData>>', self.set_scm),
        (-1, '<<SaveData>>', self.set_scm), 
        ('INSERT', '<Tab>',  self.insert_tabchar))
    
    def set_scm(self, event):
        ph, ext    = splitext(self.area.filename.lower())
        # When no '' default is specified it uses size = 4 and char = ' '.
        size, char = self.scheme.get(ext, self.scheme.get('', (4, ' ')))

        self.area.settab(size, char)

    def insert_tabchar(self, event):
        self.area.indent()
        return 'break'

    @classmethod
    def set_scheme(cls, scheme={}):
        cls.scheme.update(scheme)

@Command()
def tabset(area, size, char):
    """
    Change tab default size/char globally based
    on the actual areavi filename extension.
    """

    ph, ext = splitext(area.filename.lower())
    Tab.scheme[ext] = size, char 
    area.tabsize = size
    area.tabchar = char
    root.status.set_msg('Tab size:char:%s:%s' % (size, repr(char)))

install = Tab
