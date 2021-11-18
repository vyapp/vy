"""
Overview
========

This module implements Commands to save file and load files into AreaVi instances.

Commands
========

Command: ss(filename)
Description: It dumps the AreaVi Command target's content into a file whose name is
specified.
filename = The name of the file.

Command: lo(filename)
Description: Load the contents of filename into the AreaVi Command target.
"""

from vyapp.plugins import Command
from vyapp.app import root

@Command('s')
def save(area):
    """
    Save the contents of the targeted areavi to disk.
    """
    area.save_data()
    root.status.set_msg('File saved!')

@Command('q')
def quit(area):
    """
    """

    root.quit()

@Command('ss')
def save_as(area, filename):
    """
    """

    area.save_data_as(filename)
    root.status.set_msg('File saved as %s!' % filename)

@Command('lo')
def load_split(area, filename):
    """
    """

    area.load_data(filename)
    root.status.set_msg('Loaded %s' % filename)

@Command('to')
def load_tab(area, filename):
    """
    """

    root.note.load([[filename]])
    root.status.set_msg('Loaded %s' % filename)

@Command('vsplit')
def vsplit(area):
    """
    """
    area.master.master.master.create()

@Command('hsplit')
def hsplit(area):
    """    
    """
    area.master.master.create()
