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

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

def find(regex, handle, *args, **kwargs):
    """
    """
    seq = AreaVi.ACTIVE.find(regex, *args, **kwargs)    
    for ind in seq:
        handle(*ind)

def sniff(regex, handle, *args, **kwargs):
    """
    """
    seq = AreaVi.ACTIVE.collect('sel', regex, *args, **kwargs) 
    for ind in seq:
        handle(*ind)

def sel(*args, **kargs):
    """
    """
    AreaVi.ACTIVE.map_matches('sel', 
    AreaVi.ACTIVE.find(*args, **kwargs))

def gsub(*args, **kwargs):
    """
    """
    AreaVi.ACTIVE.replace_all(*args, **kwargs)

def get(*args):
    """
    """
    AreaVi.ACTIVE.get(*args)

def split(*args, **kwargs):
    """
    """
    AreaVi.ACTIVE.map_matches('sel', 
    AreaVi.ACTIVE.split(*args, **kwargs))

def lsub(*args):
    """
    """
    AreaVi.ACTIVE.replace_ranges('sel', *args)

ENV['find']  = find
ENV['sniff'] = sniff
ENV['sel']   = sel
ENV['gsub']  = gsub
ENV['get']   = get
ENV['split'] = split
ENV['lsub']  = lsub


