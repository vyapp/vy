"""

Overview
========

This plugin implements two Key-Commands to make the cursor jump to the begining/end of the file.

Key-Commands
============

Namespace: text-jumps

Mode: NORMAL
Event: <Key-1> 
Description: Place the cursor at the beginning of the file.


Mode: NORMAL
Event: <Key-2> 
Description: Place the cursor at the end of the file.

"""

def install(area):
    area.install('text-jumps', ('NORMAL', '<Key-1>', lambda event: event.widget.go_text_start()),
                 ('NORMAL', '<Key-2>', lambda event: event.widget.go_text_end()))








