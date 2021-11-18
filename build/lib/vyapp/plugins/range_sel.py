""" 
Overview
========

This plugin implements range selection.

Key-Commands
============

Namespace: range-sel

Mode: NORMAL
Event: <Control-k> 
Description: Add/remove selection one line up from the initial selection mark.


Mode: NORMAL
Event: <Control-j> 
Description: Add/remove selection one line down from the initial selection mark.


Mode: NORMAL
Event: <Control-l> 
Description: Add/remove selection one character right from the initial selection mark.


Mode: NORMAL
Event: <Control-h> 
Description: Add/remove selection one character left from the initial selection mark.


Mode: NORMAL
Event: <Control-v> 
Description: Drop a selection mark.
"""

from vyapp.app import root

class RangeSel:
    def __init__(self, area):
        area.install('range-sel', 
        ('NORMAL', '<Control-k>', self.sel_up),
        ('NORMAL', '<Control-j>', self.sel_down),
        ('NORMAL', '<Control-h>', self.sel_left),
        ('NORMAL', '<Control-l>', self.sel_right),
        ('NORMAL', '<Control-v>', self.start_selection))
        area.mark_set('(RANGE_SEL_MARK)', '1.0')

        self.area = area

    def start_selection(self, event):
        """  
        Start range selection.
        """

        self.area.mark_set('(RANGE_SEL_MARK)', 'insert')
        root.status.set_msg('Dropped selection mark.')

    def sel_up(self, event):
        """
        It adds 'sel' one line up the 'insert' position
        and sets the cursor one line up.
        """

        self.area.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.area.up()
        self.area.addsel('(RANGE_SEL_MARK)', 'insert')

    def sel_down(self, event):
        """ 
        It adds or removes selection one line down. 
        """

        self.area.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.area.down()
        self.area.addsel('(RANGE_SEL_MARK)', 'insert')
    
    def sel_right(self, event):
        """ 
        It adds or removes selection one character right.
        """


        self.area.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.area.right()
        self.area.addsel('(RANGE_SEL_MARK)', 'insert')
    
    def sel_left(self, event):
        """ 
        It adds or removes selection one character left.
        """

        self.area.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.area.left()
        self.area.addsel('(RANGE_SEL_MARK)', 'insert')

install = RangeSel
