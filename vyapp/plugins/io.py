"""
Overview
========

This plugin implements basic Key-Commands to open/save files.

Key-Commands
============

Namespace: io

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
        root.status.set_msg('It failed to save data.')
    else:
        root.status.set_msg('Data saved.')
        

def save_quit(area):
    """
    It saves the contents of the text area then quits.
    """

    try:
        area.save_data()
    except Exception:
        root.status.set_msg('It failed to save data.')
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
        root.status.set_msg('It failed to load.')
    else:
        root.status.set_msg('File loaded.')


def save(area):
    """
    It just saves the text area contents into the    
    actual opened file.
    """

    try:
        area.save_data()
    except Exception:
        root.status.set_msg('It failed to save data.')
    else:
        root.status.set_msg('Data saved.')



def install(area):
    area.install('io', ('NORMAL', '<Control-s>', lambda event: save(event.widget)),
                 ('NORMAL', '<Shift-S>', lambda event: save_as(event.widget)),
                 ('NORMAL', '<Control-d>', lambda event: load(event.widget)),
                 ('NORMAL', '<Key-D>', lambda event: event.widget.clear_data()),
                 ('NORMAL', '<Control-Escape>', lambda event: save_quit(event.widget)),
                 ('NORMAL', '<Shift-Escape>', lambda event: event.widget.quit()))









