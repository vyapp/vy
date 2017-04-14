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

def install(area):
    area.install('clipboard', ('NORMAL', '<Key-y>', lambda event: event.widget.cpsel()),
                 ('NORMAL', '<Key-u>', lambda event: event.widget.ctsel()),
                 ('NORMAL', '<Key-t>', lambda event: event.widget.ptsel()),
                 ('NORMAL', '<Key-r>', lambda event: event.widget.ptsel_after()),
                 ('NORMAL', '<Key-e>', lambda event: event.widget.ptsel_before()),
                 ('NORMAL', '<Control-Y>', lambda event: event.widget.cpsel('\n')),
                 ('NORMAL', '<Control-U>', lambda event: event.widget.ctsel('\n')))





