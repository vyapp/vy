"""
Overview
========

Panels are a cool way to perform some tasks. This plugin implements Key-Commands to create horizontal/vertical
panes.

Usage
=====

The idea consists of a single vertical paned window in which it is possible to create
horizontal paned windows. Inside these horizontal paned windows it is possible to add vertical panes.

Let us suppose there is one pane named A opened in a given tab. The cursor is active in the
pane AreaVi named A.

    -----
    | A |
    -----

After pressing <Alt-less> in Global mode you will get.
    
------------
| A  |  B  |
------------

Suppose now the cursor is over A or B. If you press <Alt-greater> in Global mode 
then you will get.

------------
| A  |  B  |
------------
|    C     |
------------

Now, suppose the cursor is over C then you press again <Alt-less> in Global mode.
Then you will get.

------------
| A  |  B  |
------------
| C  |  D  |
------------


Consider the case that you want to remove a given pane. For such
you place the cursor over the pane then type <Alt-X>.

For moving the focus between AreaVi instances, see the commands below.

Key-Commands
============

Mode: Global
Event: <Alt-less>
Description: Add a vertical pane.

Mode: Global
Event: <Alt-greater>
Description: Add a horizontal pane.

Mode: Global
Event: <Alt-X> 
Description: Remove a pane.

Mode: NORMAL
Event: <Shift-H>
Description: Change focus one pane left.

Mode: NORMAL
Event: <Shift-L>
Description: Change focus one pane right.

Mode: NORMAL
Event: <Shift-K>
Description: Change focus one pane up.

Mode: NORMAL
Event: <Shift-J>
Description: Change focus one pane down.

"""

from vyapp.areavi import AreaVi
from vyapp.app import root

def add_vertical_area(area):
    """
    It opens a vertical area.
    """

    area.master.master.master.create()
    return 'break'


def add_horizontal_area(area):
    """
    It creates a new horizontal area.
    """

    area.master.master.create()
    return 'break'

def remove_area(area):
    """
    It removes the focused area.
    """

    if len(area.master.master.master.panes()) == 1 and len(area.master.master.panes()) == 1: return
    
    area.master.destroy()

    if not area.master.master.panes(): area.master.master.destroy()
    root.note.set_area_focus()
    return 'break'

def go_left_area(area):
    wids  = area.master.master.panes()
    wids  = map(lambda item: str(item), wids)
    count = wids.index(str(area.master))
    count = count - 1
    wid   = area.nametowidget(wids[count])
    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())
    
    # as there is only one.
    wid[0].focus_set()
    return 'break'

def go_right_area(area):
    wids   = area.master.master.panes()
    wids  = map(lambda item: str(item), wids)
    count = wids.index(str(area.master))
    count = (count + 1) % len(wids)
    wid   = area.nametowidget(wids[count])
    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())
    
    # as there is only one.
    wid[0].focus_set()
    return 'break'

def go_down_area(area):
    wids   = area.master.master.panes()
    wids  = map(lambda item: str(item), wids)
    index = wids.index(str(area.master))

    wids   = area.master.master.master.panes()
    wids  = map(lambda item: str(item), wids)
    count = wids.index(str(area.master.master))
    count = (count + 1) % len(wids)

    wid   = area.nametowidget(wids[count])
    size  = len(wid.panes())
    wid   = area.nametowidget(wid.panes()[index if index < size else (size - 1)])

    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())

    # as there is only one.
    wid[0].focus_set()
    return 'break'

def go_up_area(area):
    wids   = area.master.master.panes()
    wids  = map(lambda item: str(item), wids)
    index = wids.index(str(area.master))

    wids   = area.master.master.master.panes()
    wids  = map(lambda item: str(item), wids)
    count = wids.index(str(area.master.master))
    count = count - 1

    wid   = area.nametowidget(wids[count])
    size  = len(wid.panes())
    wid   = area.nametowidget(wid.panes()[index if index < size else (size - 1)])
    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())

    # as there is only one.
    wid[0].focus_set()
    return 'break'

def install(area):
    area.install((-1, '<Alt-less>', lambda event: add_horizontal_area(event.widget)),
                 (-1, '<Alt-greater>', lambda event: add_vertical_area(event.widget)),
                 (-1, '<Alt-X>', lambda event: remove_area(event.widget)),
                 ('NORMAL', '<Shift-H>', lambda event: go_left_area(event.widget)),
                 ('NORMAL', '<Shift-L>', lambda event: go_right_area(event.widget)),
                 ('NORMAL', '<Shift-K>', lambda event: go_up_area(event.widget)),
                 ('NORMAL', '<Shift-J>', lambda event: go_down_area(event.widget)))



