"""
Overview
========

This plugin implements a handy functionality that is shading lines and being
capable of making the cursor jump back/next to these shaded lines. It is basically a 
mark system.

Key-Commands
============

Namespace: text-spots

Mode: NORMAL
Event <Control-b>
Description: Shade/unshade a line.

Mode: NORMAL
Event: <Control-n>
Description: Make the cursor jump to the next shaded line from the cursor position.

Mode: NORMAL
Event: <Control-m>
Description: Make the cursor jump to the previous shaded line from the cursor position.

Mode: NORMAL
Event: <Control-B>
Description: Remove all (SPOT) tags from the text.

"""
from vyapp.plugins import Namespace

class TextSpotsNS(Namespace):
    pass

class TextSpots:
    setup={'background':'green', 'foreground':'black'}
    def __init__(self, area):
        self.area = area

        area.tag_configure('(SPOT)', **self.setup)
        area.install(TextSpotsNS, ('NORMAL', '<Control-b>', self.add_spot),
        ('NORMAL', '<Control-n>', self.back_spot),
        ('NORMAL', '<Control-B>', self.del_spots),
        ('NORMAL', '<Control-m>', self.next_spot))
    
    def add_spot(self, event):
        self.area.tag_toggle('(SPOT)', 'insert linestart', 'insert lineend')

    def del_spots(self, event):
        self.area.tag_remove('(SPOT)', '1.0', 'end')

    def next_spot(self, event):
        self.area.mark_set('insert', 
        self.area.tag_nextrange('(SPOT)', 'insert lineend')[0])
        self.area.see('insert')

    def back_spot(self, event):
        self.area.mark_set('insert', 
        self.area.tag_prevrange('(SPOT)', 'insert linestart')[0])
        self.area.see('insert')

install = TextSpots

