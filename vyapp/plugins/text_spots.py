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

def install(area, setup={'background':'green', 'foreground':'black'}):
    area.tag_configure('(SPOT)', **setup)
    area.install('text-spots', ('NORMAL', '<Control-b>', lambda event: 
    area.toggle_range('(SPOT)', 'insert linestart', 'insert lineend')),
    ('NORMAL', '<Control-n>', lambda event: 
    area.seecur(area.tag_prevrange('(SPOT)', 'insert linestart')[0])),
    ('NORMAL', '<Control-B>', lambda event: 
    area.tag_remove('(SPOT)', '1.0', 'end')),
    ('NORMAL', '<Control-m>', lambda event: 
    area.seecur(area.tag_nextrange('(SPOT)', 'insert lineend')[0])))




