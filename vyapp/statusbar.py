"""
This module implements the vy statusbar widget.
"""

from Tkinter import *

class StatusBar(Frame):
    """
    This class implements a statusbar.
    """

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(border=1)

        self.msg = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.msg.pack(side='left', expand=True, fill=X)

        self.column = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.column.config(text='Col: 0')
        self.column.pack(side='right', fill=X)

        self.line = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.line.config(text='Line: 1')
        self.line.pack(side='right', fill=X)


        self.mode = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.mode.config(text='Mode: 1')
        self.mode.pack(side='right', fill=X)


    def set_msg(self, data):
        """
        Set statusbar msg.
        """

        self.msg.config(text=data)
        self.msg.update_idletasks()

    def clear_msg(self):
        """
        Clear statusbar msg.
        """

        self.msg.config(text="")
        self.msg.update_idletasks()


    def set_column(self, col):
        """
        Set the column field with col.
        """

        self.column.config(text='Col: %s' % col)
        self.column.update_idletasks()

    def set_line(self, line):
        """
        Set the line field.
        """

        self.line.config(text='Line: %s' % line)
        self.line.update_idletasks()

    def set_mode(self, mode):
        """
        Set the mode field.
        """

        self.mode.config(text='Mode: %s' % mode)
        self.mode.update_idletasks()



