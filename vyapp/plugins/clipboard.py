"""
Overview
========

This plugin implements a set of basic functionalities to deal with text. Like copying,
cutting, deleting, pasting text to the clipboard.


Key-Commands
============

Namespace: clipboard

Mode: NORMAL
Event: <Key-y> 
Description: Copy selection to the clipboard.


Mode: NORMAL
Event: <Key-u> 
Description: Cut selection then add to the clipboard.


Mode: NORMAL
Event: <Key-t> 
Description: Paste text from the clipboard in the cursor position.


Mode: NORMAL
Event: <Key-r> 
Description: Paste text from the clipboard one line down.


Mode: NORMAL
Event: <Key-e> 
Description: Paste text from the clipboard one line up.

Mode: NORMAL
Event: <Control-Y> 
Description: Add selection to the clipboard with a separator \n.


Mode: NORMAL
Event: <Control-U> 
Description: Cut selection and add to the clipboard with a separator \n.


"""

class Clipboard:
    def __init__(self, area):
        area.install('clipboard', 
        ('NORMAL', '<Key-y>', lambda event: event.widget.cpsel()),
        ('NORMAL', '<Key-u>', lambda event: event.widget.ctsel()),
        ('NORMAL', '<Key-t>', self.ptsel),
        ('NORMAL', '<Key-r>', self.ptsel_after),
        ('NORMAL', '<Key-e>', self.ptsel_before),
        ('NORMAL', '<Control-Y>', lambda event: event.widget.cpsel('\n')),
        ('NORMAL', '<Control-I>', self.ptsel_block),
        ('NORMAL', '<Control-U>', lambda event: event.widget.ctsel('\n')))
        self.area = area

    def ptsel(self, event):
        """
        Paste text at the cursor position.
        """

        data = self.area.clipboard_get()
        self.area.edit_separator()
        self.area.insert('insert', data)

    def ptsel_after(self, event):
        """
        Paste text one line down the cursor position.
        """

        data = self.area.clipboard_get()
        self.area.edit_separator()
        self.area.insert('insert +1l linestart', data)


    def ptsel_before(self, event):
        """
        Paste text one line up the cursor position.
        """

        data = self.area.clipboard_get()
        self.area.edit_separator()
        self.area.insert('insert linestart', data)

    def ptsel_block(self, event):
        data      = self.area.clipboard_get()
        data      = data.split('\n')
        line, col = self.area.indcur()

        self.area.edit_separator()
        for ind in range(0, len(data)):
            self.area.insert('%s.%s' % (line + ind, col), data[ind])

install = Clipboard

