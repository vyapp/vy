"""
Overview
========

This plugin implements keycommands to delete text selection, delete line, delete char.


Key-Commands
============

Namespace: data-del

Mode: NORMAL
Event: <Key-d> 
Description: Delete selection of text.


Mode: NORMAL
Event: <Key-x> 
Description: Delete a line where the cursor is on.


Mode: NORMAL
Event: <Key-z> 
Description: Delete a char from the cursor position.

"""

def install(area):
    area.install('data-del', ('NORMAL', '<Key-d>', lambda event: event.widget.del_sel()),
                 ('NORMAL', '<Key-x>', lambda event: event.widget.del_line()),
                 ('NORMAL', '<Key-z>', lambda event: event.widget.del_char()))
        















