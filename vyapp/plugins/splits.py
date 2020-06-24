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

from vyapp.app import root

def add_vertical_area(area):
    """
    It opens a vertical area.
    """

    vpane = area.master.master.master
    vpane.create()

    wids  = vpane.panes()
    height = root.winfo_height()//(len(wids) + 1)
    root.update()

    for ind in range(0, len(wids) - 1):
        vpane.sash_place(ind,  0,  (ind + 1) * height)
    return 'break'

def add_horizontal_area(area):
    """
    It creates a new horizontal area.
    """

    hpane = area.master.master
    hpane.create()

    wids  = hpane.panes()
    width = root.winfo_width()//(len(wids) + 1)
    root.update()

    for ind in range(0, len(wids) - 1):
        hpane.sash_place(ind,  (ind + 1) * width,  0)

    return 'break'

def remove_area(area):
    """
    It removes the focused area.
    """

    vpanes = len(area.master.master.master.panes())
    hpanes = len(area.master.master.panes())

    if vpanes == 1 and hpanes == 1: return
    area.master.destroy()

    if not area.master.master.panes(): 
        area.master.master.destroy()

    root.note.restore_area_focus()
    return 'break'


def install(area):
    area.install('splits', 
    (-1, '<Alt-less>', lambda event: add_horizontal_area(event.widget)),
    (-1, '<Alt-greater>', lambda event: add_vertical_area(event.widget)),
    (-1, '<Alt-X>', lambda event: remove_area(event.widget)))

