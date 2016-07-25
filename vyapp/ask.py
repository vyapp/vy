"""
This module implements basic input data scheme.
"""

from Tkinter import *
from vyapp.app import root
import string

class InputBox(object):
    def __init__(self, area, default_data=''):
        self.default_data = default_data
        self.area    = area
        self.frame   = Frame(root.read_data, border=1, padx=3, pady=3)
        self.entry   = Entry(self.frame)
        self.entry.config(background='grey')
        self.entry.focus_set()
        self.entry.grab_set()

        self.entry.insert('end', default_data)
        self.entry.pack(side='left', expand=True, fill=BOTH)
        self.frame.pack(expand=True, fill=X)

        root.read_data.pack(fill=X)

    def done(self):
        self.entry.destroy()
        self.frame.destroy()
        root.read_data.pack_forget()
        self.area.focus_set()

class Get(InputBox):
    def __init__(self, area, events={}, default_data=''):
        InputBox.__init__(self, area, default_data)

        self.entry.bindtags(('Entry', self.entry, '.', 'all'))
        self.entry.bind('<Key>', self.dispatch_change_event, add=True)

        for indi, indj in events.iteritems():
            self.entry.bind(indi, lambda event, handle=indj: 
                        self.dispatch_event(handle) , add=True)

    def dispatch_change_event(self, event):
        if event.keysym in string.printable:
            self.entry.event_generate('<<Data>>')

    def dispatch_event(self, handle):
        is_done = handle(self.entry)
        if is_done == True: 
            self.done()

class Ask(InputBox):
    """
    """

    def __init__(self, area, default_data =''):
        InputBox.__init__(self, area, default_data)
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






