"""
Overview
========

This module implements two commands to strip chars off selected
regions of text.

Commands
========

Command: def strip(area, chars=' '):
Description: 

Command: def rstrip(area, chars=' '):
Description: 

"""

from vyapp.plugins import Command
from re import escape

@Command()
def strip(area, chars=' '):
    """
    Strip chars off the beginning of all selected lines.
    if chars is not given it removes spaces.
    """

    area.replace_ranges('sel', '^[%s]+' % escape(chars), '')

@Command()
def rstrip(area, chars=' '):
    """
    Strip chars off the end of all selected lines.
    if chars is not given it removes spaces.
    """

    area.replace_ranges('sel', '[%s]+$' % escape(chars), '')
