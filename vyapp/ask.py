"""
This module implements basic input data scheme.
"""

from Tkinter import *
from vyapp.app import root
from vyapp.areavi import DataEvent, IdleEvent
import string

class InputBox(object):
    def __init__(self, default_data=''):
        self.default_data = default_data

        self.area  = root.focus_get()
        self.frame = Frame(root, border=1, padx=3, pady=3)
        self.entry = Entry(self.frame)
        self.entry.config(background='grey')
        self.entry.focus_set()

        # Maybe there is a more elegant way.
        self.entry.bind('<FocusOut>', lambda event: self.entry.focus_set())
        self.entry.insert('end', default_data)
        self.entry.pack(side='left', expand=True, fill=BOTH)
        self.frame.grid(row=1, sticky='we')

    def done(self):
        self.entry.destroy()
        self.frame.destroy()
        self.area.focus_set()

class Get(InputBox, DataEvent, IdleEvent):
    def __init__(self, events={}, default_data=''):
        InputBox.__init__(self, default_data)
        DataEvent.__init__(self, self.entry)
        IdleEvent.__init__(self, self.entry)

        self.entry.bindtags(('Entry', self.entry, '.', 'all'))
        for indi, indj in events.iteritems():
            self.entry.bind(indi, lambda event, handle=indj: 
                        self.dispatch(handle) , add=True)

    def dispatch(self, handle):
        is_done = handle(self.entry)
        if is_done == True: 
            self.done()

class Ask(InputBox):
    """
    """

    def __init__(self, default_data =''):
        InputBox.__init__(self, default_data)
        self.entry.bind('<Return>', lambda event: self.on_success())
        self.entry.bind('<Escape>', lambda event: self.done())
        self.data = ''
        self.area.wait_window(self.frame)

    def on_success(self):
        self.data = self.entry.get()
        InputBox.done(self)

    def __str__(self):
        return self.data

    __repr__ = __str__






