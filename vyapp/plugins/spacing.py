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
    default_size, default_char = 4, ' '
    scheme = {}

    def __init__(self, area):
        self.area = area
        area.install('spacing', ('INSERT', '<Tab>',  self.insert_tab))
    
    def insert_tab(self, event):
        ph, ext    = splitext(self.area.filename.lower())
        size, char = self.scheme.get(ext, 
        (self.default_size, self.default_char))

        self.area.edit_separator()
        self.area.insert('insert', char * size)
        return 'break'

    @classmethod
    def set_scheme(cls, scheme={}):
        cls.scheme.update(scheme)

    @classmethod
    def set_default(cls, default_size, default_char):
        cls.default_size = default_size
        cls.default_char = default_char

def tabset(size, char):
    """
    Change tab default size/char globally based
    on the actual areavi filename extension.
    """

    ph, ext = splitext(AreaVi.ACTIVE.filename.lower())
    Tab.scheme[ext] = size, char 

ENV['tabset'] = tabset
install = Tab



