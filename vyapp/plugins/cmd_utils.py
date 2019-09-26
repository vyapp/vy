"""
Overview
========

Just some misc utils.

Commands
========

Command: cpsel(sep='\n')
Description: Copy selected region of text using sep.

Command: ctsel(sep='\n')
Description: Cut selected region of text using sep.

Command: chmode(sep='\n')
Description: Switch modes for an AreaVi instance.

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

def cpsel(sep='\n'):
    """
    Copy the selected region to the clipboard.
    """

    AreaVi.ACTIVE.cpsel(sep)

def ctsel(sep='\n'):
    """
    Cut the selected region to the clipboard.
    """
    AreaVi.ACTIVE.ctsel(sep)

def chmode(id):
    """
    Switch modes for an AreaVi instance set as target.
    """
    AreaVi.ACTIVE.chmode(id)

ENV['cpsel']  = cpsel
ENV['ctsel']  = ctsel
ENV['chmode'] = chmode


