"""
Overview
========

This plugin implements a handy functionality that is shading lines and being
capable of making the cursor jump back/next to these shaded lines. It is basically a 
mark system.

Usage
=====

In order to shade a line it is neeeded to switch to ALPHA mode by pressing
<Key-3> in NORMAL mode. Make sure the cursor is positioined over the line that 
should be shaded/marked. 

After being in ALPHA mode it is enough to type <Key-q> the line over the cursor 
will be shaded according to the dictionary options passed to the install function.

When it is needed to unshade a line, just put the cursor over the shaded line
then switch to ALPHA mode then press <Key-q> it will toggle the selection.

After having shaded/marked some lines it is possible to jump back/next to those
lines by pressing <Key-a> or <Key-s> in ALPHA mode.

Once the cursor is positioned on the right line , just press <Escape> to go
back to NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event <Control-b>
Description: Shade/unshade a line.

Mode: NORMAL
Event: <Control-n>
Description: Makes the cursor jump to the next shaded line from the cursor position.

Mode: NORMAL
Event: <Control-m>
Description: Makes the cursor jump to the previous shaded line from the cursor position.

"""


def toggle_status(area):
    map0 = area.tag_nextrange('(SPOT)', 'insert', 'insert lineend')
    map1 = area.tag_prevrange('(SPOT)', 'insert', 'insert linestart')

    if map0 or map1:
        area.tag_remove('(SPOT)', 'insert linestart', 
                        'insert lineend')
    else:
        area.tag_add('(SPOT)', 'insert linestart', 
                     'insert lineend')
        
def prev_spot(area):
    map = area.tag_prevrange('(SPOT)', 'insert linestart')
    if not map: return

    area.mark_set('insert', map[0])
    area.see('insert')

def next_spot(area):
    map = area.tag_nextrange('(SPOT)', 'insert lineend')
    if not map: return

    area.mark_set('insert', map[0])
    area.see('insert')


def install(area, setup={'background':'green', 'foreground':'black'}):
    area.tag_configure('(SPOT)', **setup)
    area.install(('NORMAL', '<Control-b>', lambda event: toggle_status(event.widget)),
           ('NORMAL', '<Control-n>', lambda event: prev_spot(event.widget)),
           ('NORMAL', '<Control-m>', lambda event: next_spot(event.widget)))








