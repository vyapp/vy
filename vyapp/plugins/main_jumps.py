"""
Overview
========

This plugin implements the basic cursor movements.

Key-Commands
============

Namespace: main-jumps

Mode: NORMAL
Event: <Key-j> 
Description: Move the cursor one line down.


Mode: NORMAL
Event: <Key-k> 
Description: Move the cursor one line up.


Mode: NORMAL
Event: <Key-h> 
Description: Move the cursor one character left.


Mode: NORMAL
Event: <Key-l> 
Description: Move the cursor one character right.


"""

class MainJumps:
    def __init__(self, area):
        self.area = area

        area.install('main-jumps', 
        (-1, '<Alt-a>', self.down),
        ('NORMAL', '<Key-j>', self.down),
        (-1, '<Alt-e>', self.up),
        ('NORMAL', '<Key-k>', self.up),
        (-1, '<Alt-n>', self.left),
        ('NORMAL', '<Key-h>', self.left),
        (-1, '<Alt-m>', self.right),
        ('NORMAL', '<Key-l>', self.right))
    
    def down(self, event):
        event.widget.down()
        return 'break'

    def up(self, event):
        event.widget.up()
        return 'break'

    def left(self, event):
        event.widget.left()
        return 'break'

    def right(self, event):
        event.widget.right()
        return 'break'

install = MainJumps