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

from vyapp.plugins import Command

@Command()
def cpsel(area, sep='\n'):
    """
    Copy the selected region to the clipboard.
    """

    area.cpsel(sep)

@Command()
def ctsel(area, sep='\n'):
    """
    Cut the selected region to the clipboard.
    """
    area.ctsel(sep)

@Command()
def chmode(area, id):
    """
    Switch modes for an AreaVi instance set as target.
    """
    area.chmode(id)
