"""
Overview
========

This module implements command search tools. It is possible to execute python
functions to highlight patterns of text and replace patterns.

Commands
========

Command: sel(regex, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None):
Description: Highlight patterns in the AreaVi instance that has focus.
regex     = The pattern to be searched.
index     = The starting index of the search.
stopindex = The stop index of the search.

Command: gsub(regex, data, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None):

Description: Replace all occurrences of a given pattern for data.
regex = The pattern to be searched.
data  = The replacement for the pattern.

Command: get(index, stopindex)
Description: Get the text between index and stopindex from an AreaVi instance
that was set as target for commands.
index     = The start index.
stopindex = The stopindex.
"""

from vyapp.plugins import Command
from vyapp.areavi import AreaVi

@Command()
def find(area, regex, handle, *args, **kwargs):
    """
    """
    seq = area.find(regex, *args, **kwargs)    
    for ind in seq:
        handle(*ind)

@Command()
def sniff(area, regex, handle, *args, **kwargs):
    """
    """
    seq = area.collect('sel', regex, *args, **kwargs) 
    for ind in seq:
        handle(*ind)

@Command()
def sel(area, *args, **kwargs):
    """
    """
    area.select_matches('sel', 
    area.find(*args, **kwargs))

@Command()
def gsub(area, *args, **kwargs):
    """
    """
    area.replace_all(*args, **kwargs)

@Command()
def get(area, *args):
    """
    """
    return area.get(*args)

@Command()
def split(area, *args, **kwargs):
    """
    """
    area.select_matches('sel', 
    area.split(*args, **kwargs))

@Command()
def lsub(area, *args):
    """
    """
    area.replace_ranges('sel', *args)
