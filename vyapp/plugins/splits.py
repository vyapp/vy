"""
Overview
========

Panels are a cool way to perform some tasks. This plugin implements Key-Commands to create horizontal/vertical
panes.

Key-Commands
============

Namespace: splits

Mode: Global
Event: <Alt-less>
Description: Add a vertical pane.

Mode: Global
Event: <Alt-greater>
Description: Add a horizontal pane.

Mode: Global
Event: <Alt-X> 
Description: Remove a pane.

Mode: Global
Event: <Control-Alt-h>
Description: Change focus one pane left.

Mode: Global
Event: <Control-Alt-l>
Description: Change focus one pane right.

Mode: Global
Event: <Control-Alt-k>
Description: Change focus one pane up.

Mode: Global
Event: <Control-Alt-j>
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
    area.install('splits', (-1, '<Alt-less>', lambda event: add_horizontal_area(event.widget)),
                 (-1, '<Alt-greater>', lambda event: add_vertical_area(event.widget)),
                 (-1, '<Alt-X>', lambda event: remove_area(event.widget)),
                 (-1, '<Control-Alt-h>', lambda event: go_left_area(event.widget)),
                 (-1, '<Control-Alt-l>', lambda event: go_right_area(event.widget)),
                 (-1, '<Control-Alt-k>', lambda event: go_up_area(event.widget)),
                 (-1, '<Control-Alt-j>', lambda event: go_down_area(event.widget)))








