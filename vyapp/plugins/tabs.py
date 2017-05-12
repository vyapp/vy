"""
Overview
========

Tabs are a great feature when manipulating several files. This plugin implements Key-Commands to create, 
open files, change the focus between opened tabs.

Key-Commands
============

Namespace: tabs

Mode: Global
Event: <Alt-comma>
Description: It pops a file selection window to load the contents of a file in a new tab.

Mode: Global
Event: <Alt-period>
Description: It creates a new blank tab.

Mode: Global
Event: <Alt-x>
Description: It removes the focused tab.

Mode: Global
Event: <Alt-o>
Description: It changes the focus left from a tab.

Mode: Global
Event: <Alt-p>
Description: It changes the focus right from a tab.

"""

from vyapp.app import root
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
        root.status.set_msg('It failed to load.')
    else:
        root.status.set_msg('File loaded.')
    return 'break'

def create_tab():
    root.note.create('none')
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

    return 'break'

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
    area.install('tabs', (-1, '<Alt-comma>', lambda event: load_tab()),
                 (-1, '<Alt-period>', lambda event: create_tab()),
                 (-1, '<Alt-x>', lambda event: remove_tab()),
                 (-1, '<Alt-o>', lambda event: select_left()),
                 (-1, '<Alt-p>', lambda event: select_right()))











