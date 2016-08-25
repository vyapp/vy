"""
Overview
========

It is used to remember an important position of the text and quickly switch to it.


Key-Commands
============

Mode: NORMAL
Event: 
Description: 

Mode: NORMAL
Event: 
Description: 

"""

class QuickJumps(object):
    def __init__(self, area):
        self.area  = area
        area.install(('NORMAL', '<Key-space>', lambda event: self.area.mark_set('(PREV_POSITION)', 'insert')),
                     ('NORMAL', '<BackSpace>', lambda event: self.area.seecur('(PREV_POSITION)')))

install = QuickJumps


