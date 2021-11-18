"""
Overview
========

This module implements functions to adjust AreaVi widget encoding.


Commands
========

Command: charset(name)
Description: Set the default encoding to save files.
name = The name of the encoding.

Command: decode(name)
Description: Adjust an AreaVi widget text encoding.
name = The name of the encoding.
"""

from vyapp.plugins import Command
from vyapp.app import root

@Command()
def decode(area, name):
    try:
        area.decode(name)
    except UnicodeDecodeError:
        root.status.set_msg('Failed! Charset %s' % name)

@Command()
def charset(area, name):
    area.charset = name
    root.status.set_msg('Charset %s set.' % name)
