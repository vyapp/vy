"""
# Mode: 1 
# Event: Control-d

It opens a file selection window to pick up a file to edit.

Whenever you press Control-d over a text area it will open a file selection window
then after picking up a file it will load the content over the text area.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: F8

It opens a file selection window to pick up a file, after you have picked up a file
it will load the contents of the file in a new tab.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: F7

It creates a new tab area. 
-----------------------------------------------------------------------------------

# Mode: 1
# Event: Control-s

It saves the contents in the opened file.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: Key-S

It opens a file selection window to save the text area contents with
in a given path. 
-----------------------------------------------------------------------------------

# Mode: 1
# Event: Control-Escape

It saves the content of the text area then quits.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: Shift-Escape

It quits.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: F4

It adds a horizontal area.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: F5

It adds a vertical area.
-----------------------------------------------------------------------------------

# Mode 1:
# Event: F6

It removes the area with focus.
-----------------------------------------------------------------------------------

# Mode: 1
# Event: Delete

It removes the selected tab.
-----------------------------------------------------------------------------------

"""

from tkMessageBox import *
from tkFileDialog import askopenfilename, asksaveasfilename
from vyapp.app import root
from vyapp.tools.misc import set_status_msg

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

def load_tab():
    """
    It pops a askopenfilename window to drop
    the contents of a file into another tab's text area.
    """

    filename = askopenfilename()

    # If i don't check it ends up cleaning up
    # the text area when one presses cancel.

    if not filename: 
        return

    try:
        root.note.load([ [filename] ])
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

def add_vertical_area(area):
    """
    It opens a vertical area.
    """

    area.master.master.master.create()

def load_vertical_area(area):
    """
    It opens a vertical area.
    then asks to find a file to drop the contents
    inside it.
    """

    pass

def add_horizontal_area(area):
    """
    It creates a new horizontal area.
    """

    area.master.master.create()

def load_horizontal_area(area):
    """
    It pops a window to select a file then
    creates a new horizontal area to drop the contents
    of the file inside.
    """

    pass

def remove_area(area):
    """
    It removes the focused area.
    """

    if len(area.master.master.master.panes()) == 1 and len(area.master.master.panes()) == 1: return
    
    area.master.destroy()

    if not area.master.master.panes(): area.master.master.destroy()

def remove_tab():
    """
    It removes the selected tab.
    """

    if len(root.note.tabs()) <= 1: return
    root.note.forget(root.note.select())


def install(area):
    area.install(('NORMAL', '<Control-s>', lambda event: save(event.widget)),
           ('NORMAL', '<Shift-S>', lambda event: save_as(event.widget)),
           ('NORMAL', '<Control-d>', lambda event: load(event.widget)),
           ('NORMAL', '<Key-D>', lambda event: event.widget.clear_data()),
           ('NORMAL', '<Control-Escape>', lambda event: save_quit(event.widget)),
           ('NORMAL', '<Shift-Escape>', lambda event: event.widget.quit()),
           ('NORMAL', '<F8>', lambda event: load_tab()),
           ('NORMAL', '<F4>', lambda event: add_horizontal_area(event.widget)),
           ('NORMAL', '<F5>', lambda event: add_vertical_area(event.widget)),
           ('NORMAL', '<F6>', lambda event: remove_area(event.widget)),
           ('NORMAL', '<F7>', lambda event: root.note.create('None')),
           ('NORMAL', '<Delete>', lambda event: remove_tab()))













