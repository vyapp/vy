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

Mode: EXTRA
Event: <Key-y> 
Description: Add selection to the clipboard with a separator \n.

Mode: EXTRA
Event: <Key-t> 
Description: Split clipboard content on \n and insert each one of the lines
in its corresponding line index's based on the cursor column.

Clipboard:

    ab
    cd
    ef

Text: 

    alpha
    beta
    gamma

If the cursor is on column l then text will be:

Text:

    aablpha
    bcdeta
    gefamma
    
Mode: EXTRA
Event: <Key-u> 
Description: Cut selection and add to the clipboard with a separator \n.

"""

from vyapp.app import root

class Clipboard:
    def __init__(self, area):
        area.install('clipboard', 
        ('NORMAL', '<Key-y>', self.copysel),
        ('NORMAL', '<Key-u>', self.cutsel),
        ('NORMAL', '<Key-t>', self.ptsel),
        ('NORMAL', '<Key-r>', self.ptsel_after),
        ('NORMAL', '<Key-e>', self.ptsel_before),
        ('EXTRA', '<Key-y>', self.cpsel_with_sep),
        ('EXTRA', '<Key-t>', self.ptsel_block),
        ('EXTRA', '<Key-u>', self.cutsel_with_sep))
        self.area = area

    def cutsel(self, event):
        """
        Cut selection.
        """

        event.widget.ctsel()
        root.status.set_msg('Text was cut!')

    def copysel(self, event):
        """
        Copy selection.
        """

        event.widget.cpsel()
        root.status.set_msg('Text was copied!')

    def cpsel_with_sep(self, event):
        """
        Copy selection.
        """
        self.area.cpsel('\n')
        root.status.set_msg('Text was copied with sep: \\n!')
        self.area.chmode('NORMAL')

    def cutsel_with_sep(self, event):
        self.area.ctsel('\n')
        root.status.set_msg('Text was cut with sep: \\n!')
        self.area.chmode('NORMAL')

    def ptsel(self, event):
        """
        Paste text at the cursor position.
        """

        data = self.area.clipboard_get()
        self.area.edit_separator()
        self.area.insert('insert', data)
        root.status.set_msg('Text was pasted!')

    def ptsel_after(self, event):
        """
        Paste text one line down the cursor position.
        """

        data = self.area.clipboard_get()
        self.area.edit_separator()
        self.area.insert('insert +1l linestart', data)
        root.status.set_msg('Text was pasted!')


    def ptsel_before(self, event):
        """
        Paste text one line up the cursor position.
        """

        data = self.area.clipboard_get()
        self.area.edit_separator()
        self.area.insert('insert linestart', data)
        root.status.set_msg('Text was pasted!')

    def ptsel_block(self, event):
        data      = self.area.clipboard_get()
        data      = data.split('\n')
        line, col = self.area.indexref()

        self.area.edit_separator()
        for ind in range(0, len(data)):
            self.area.insert('%s.%s' % (line + ind, col), data[ind])

        self.area.chmode('NORMAL')
        root.status.set_msg('Text block was pasted')

install = Clipboard

