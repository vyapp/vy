"""
This module implements basic input data scheme.
"""

from Tkinter import *
from vyapp.app import root

class InputBox(object):
    def __init__(self, area, default_data='', on_done=lambda data: None):
        self.default_data = default_data
        self.area    = area
        self.on_done = on_done
        self.frame   = Frame(root.read_data, border=1, padx=3, pady=3)
        self.entry   = Entry(self.frame)
        self.entry.config(background='grey')
        self.entry.focus_set()
        self.entry.grab_set()

        self.entry.insert('end', default_data)
        self.entry.pack(side='left', expand=True, fill=BOTH)
        self.frame.pack(expand=True, fill=X)

        root.read_data.pack(fill=X)
        self.entry.bind('<Escape>', lambda event: self.done())
        self.entry.bind('<Return>', lambda event: self.done())

    def done(self):
        data = self.entry.get()
        self.on_done(data)
        self.entry.destroy()
        self.frame.destroy()
        root.read_data.pack_forget()
        self.area.focus_set()

class Edit(InputBox):
    def __init__(self, area, on_data, on_done, on_next, on_prev, default_data=''):
        InputBox.__init__(self, area, default_data)
        self.on_data = on_data
        self.on_next = on_next
        self.on_prev = on_prev
        self.on_done = on_done


        self.entry.bind('<Alt-o>', lambda event: self.on_prev(self.entry.get()))
        self.entry.bind('<Alt-p>', lambda event: self.on_next(self.entry.get()))
        self.entry.bind('<Control-k>', lambda event: self.on_prev(self.entry.get()))
        self.entry.bind('<Control-j>', lambda event: self.on_next(self.entry.get()))
        self.entry.bind('<Return>', lambda event: self.on_data(self.entry.get()))

    
class Get(InputBox):
    def __init__(self, area, on_data, on_done, on_next, on_prev, default_data=''):
        InputBox.__init__(self, area, default_data)
        self.on_data = on_data
        self.on_next = on_next
        self.on_prev = on_prev
        self.on_done = on_done
        self.entry.bindtags(('Entry', self.entry, '.', 'all'))
        self.entry.bind('<Alt-o>', lambda event: self.on_prev(self.entry.get()))
        self.entry.bind('<Alt-p>', lambda event: self.on_next(self.entry.get()))

        self.entry.bind('<Control-k>', lambda event: self.on_prev(self.entry.get()))
        self.entry.bind('<Control-j>', lambda event: self.on_next(self.entry.get()))
        self.entry.bind('<Key>', lambda event: self.on_data(self.entry.get()))

class Ask(InputBox):
    """
    """

    def __init__(self, area, default_data =''):
        InputBox.__init__(self, area, default_data)
        self.entry.bind('<Return>', lambda event: self.on_success())

        self.data  = ''
        self.area.wait_window(self.frame)

    def on_success(self):
        self.data = self.entry.get()
        InputBox.done(self)

    def __str__(self):
        return self.data

    __repr__ = __str__



