"""
Overview
========

Tabs are a great feature when manipulating several files. This plugin implements Key-Commands to create, 
open files, change the focus between opened tabs.

Usage
=====

The way to create a blank tab is by pressing <Alt-period> in NORMAL mode.    
It will open a new blank tab but keep the focus in the actual one.

There is a handy Key-Command to create a tab and load the contents of a file into it.
For such, just put in NORMAL mode then type <Alt-comma>. By pressig <Alt-comma> it pops a file
selection window to pick up a file.

Sometimes you will be done with a given tab, you can remove such a tab by pressing <Delete> in
NORMAL mode.

It is possible to change the focus left from a given tab by pressing <Alt-o>
or changing the focus right by pressing <Alt-p> in NORMAL mode.


Key-Commands
============

Mode: Global
Event: <Alt-comma>
Description: It pops a file selection window to load the contents of a file in a new tab.

Mode: Global
Event: <Alt-period>
Description: It creates a new blank tab.

Mode: Global
Event: <Delete>
Description: It removes the focused tab.

Mode: Global
Event: <Alt-o>
Description: It changes the focus left from a tab.

Mode: Global
Event: <Alt-p>
Description: It changes the focus right from a tab.

"""

from vyapp.app import root
from vyapp.tools import set_status_msg
from tkMessageBox import *
from tkFileDialog import askopenfilename, asksaveasfilename
from vyapp.areavi import AreaVi

def load_tab():
    """
    It pops a askopenfilename window to drop
    the contents of a file into another tab's text area.
    """

    filename = askopenfilename()

    # If i don't check it ends up cleaning up
    # the text area when one presses cancel.

    if not filename: 
        return 'break'

    try:
        root.note.load([ [filename] ])
    except Exception:
        set_status_msg('It failed to load.')
    else:
        set_status_msg('File loaded.')
    return 'break'

def create_tab():
    root.note.create('None')
    return 'break'

def remove_tab():
    """
    It removes the selected tab.
    """

    if len(root.note.tabs()) <= 1: return
    name = root.note.select()
    wid  = root.note.nametowidget(name)
    wid.destroy()
    root.note.select(0)
    root.note.set_area_focus()

    # We don't need to call forget after destroy.
    # It seems the method forget from note doesnt destroy
    # the widget at all consequently the event <Destroy> isn't
    # spreaded.
    # root.note.forget(wid)

def select_left():
    """
    """

    root.note.select(root.note.index(root.note.select()) - 1)
    root.note.set_area_focus()
    return 'break'

def select_right():
    """
    """

    root.note.select(root.note.index(root.note.select()) + 1)
    root.note.set_area_focus()
    return 'break'

def install(area):
    area.install((-1, '<Alt-comma>', lambda event: load_tab()),
                 (-1, '<Alt-period>', lambda event: create_tab()),
                 (-1, '<Delete>', lambda event: remove_tab()),
                 (-1, '<Alt-o>', lambda event: select_left()),
                 (-1, '<Alt-p>', lambda event: select_right()))





