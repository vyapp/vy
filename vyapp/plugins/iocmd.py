"""
Overview
========

This module implements commands to save file and load files into AreaVi instances.

Commands
========

Command: ss(filename)
Description: It dumps the AreaVi command target's content into a file whose name is
specified.
filename = The name of the file.

Command: lo(filename)
Description: Load the contents of filename into the AreaVi command target.
"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.app import root

def save():
    """
    """
    AreaVi.ACTIVE.save_data()
    root.status.set_msg('File saved!')

def quit():
    """
    """

    root.quit()

def save_as(filename):
    """
    """

    AreaVi.ACTIVE.save_data_as(filename)
    root.status.set_msg('File saved as %s!' % filename)

def load_split(filename):
    """
    """

    AreaVi.ACTIVE.load_data(filename)
    root.status.set_msg('Loaded %s' % filename)

def load_tab(filename):
    """
    """

    root.note.load([[filename]])
    root.status.set_msg('Loaded %s' % filename)

def vsplit():
    """
    """
    AreaVi.ACTIVE.master.master.master.create()

def hsplit():
    """    
    """
    AreaVi.ACTIVE.master.master.create()

ENV['s'] = save
ENV['q'] = quit
ENV['ss'] = save_as
ENV['lo'] = load_split
ENV['to'] = load_tab
ENV['vsplit'] = vsplit
ENV['hsplit'] = hsplit

