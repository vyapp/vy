"""
Overview
========

Usage
=====


Key-Commands
============

Mode: NORMAL
Event: <Key-P> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

 
Mode: NORMAL
Event: <Key-O> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

"""

def install(area):
    area.install(('NORMAL', '<Key-P>', lambda event: event.widget.go_next_sym()),
                 ('NORMAL', '<Key-O>', lambda event: event.widget.go_prev_sym()))




