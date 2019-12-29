"""
Overview
========

This plugin implements python functions to get text in lower case and upper case.

Commands
========

Command: lower()
Description: Turn the selected text into lower case.

Command: upper()
Description: Turn the selected text into upper case.
"""

from vyapp.plugins import Command

@Command()
def lower(area):
    """
    """

    map  = area.tag_ranges('sel')
    for index in range(0, len(map) - 1, 2):
        area.swap(area.get(map[index], 
            map[index + 1]).lower(), map[index], map[index + 1])

@Command()
def upper(area):
    """
    """

    map  = area.tag_ranges('sel')
    for index in range(0, len(map) - 1, 2):
        area.swap(area.get(map[index], 
            map[index + 1]).upper(), map[index], map[index + 1])



