"""
Overview
========

This plugin implements basic Key-Commands to open/save files.

Usage
=====

It is possible to pops a file window selection to load the contents of a file
in a given AreaVi instance by pressing <Control-d>.

After some changes to a opened file it is possible to save the contents of the file
by pressing <Control-s> in NORMAL mode.

The way to save the contents of an AreaVi instance as a different filename is by
pressing <Shift-S> in NORMAL mode. It will open a file save dialog to pick up a name.

Sometimes it is handy to just save and quit, for such just press <Control-Escape> in NORMAL mode.
You can just quit without saving by pressing <Shift-Escape> in NORMAL mode as well.

There is a Key-Command to clean all the text from a given active AreaVi instance. For such
type <Key-D> in NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Control-d>
Description: It pops a file selection window to load the contents of a file.

Mode: NORMAL
Event: <Control-s>
Description: It saves the content of the AreaVi instance into the opened file.

Mode: NORMAL
Event: <Shift-S>
Description: It pops a save file dialog to save the contents of the active AreaVi
instance with a different filename.

Mode: NORMAL
Event: <Key-D>
Description: Clear all text of the active AreaVi instance.

Mode: NORMAL
Event: <Control-Escape>
Description: Save and quit.

Mode: NORMAL
Event: <Shift-Escape>
Description: Quit.
"""

from tkMessageBox import *
from tkFileDialog import askopenfilename, asksaveasfilename
from vyapp.app import root
from vyapp.tools import set_status_msg

def save_as(area):
    """
    It pops a asksaveasfilename window to save the contents of
    the text area.
    """

    filename = asksaveasfilename()

    # If the user presses cancel it returns ''.

    if not filename: 
        return

    try:
        area.save_data_as(filename)
    except Exception:
        set_status_msg('It failed to save data.')
    else:
        set_status_msg('Data saved.')
        

def save_quit(area):
    """
    It saves the contents of the text area then quits.
    """

    try:
        area.save_data()
    except Exception:
        set_status_msg('It failed to save data.')
    else:
        area.quit()

def load(area):
    """
    It pops a askopenfilename to find a file to drop
    the contents in the focused text area.
    """

    filename = askopenfilename()

    # If i don't check it ends up cleaning up
    # the text area when one presses cancel.

    if not filename: 
        return

    try:
        area.load_data(filename)
    except Exception:
        set_status_msg('It failed to load.')
    else:
        set_status_msg('File loaded.')


def save(area):
    """
    It just saves the text area contents into the    
    actual opened file.
    """

    try:
        area.save_data()
    except Exception:
        set_status_msg('It failed to save data.')
    else:
        set_status_msg('Data saved.')



def install(area):
    area.install(('NORMAL', '<Control-s>', lambda event: save(event.widget)),
                 ('NORMAL', '<Shift-S>', lambda event: save_as(event.widget)),
                 ('NORMAL', '<Control-d>', lambda event: load(event.widget)),
                 ('NORMAL', '<Key-D>', lambda event: event.widget.clear_data()),
                 ('NORMAL', '<Control-Escape>', lambda event: save_quit(event.widget)),
                 ('NORMAL', '<Shift-Escape>', lambda event: event.widget.quit()))





