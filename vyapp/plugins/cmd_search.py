"""
Overview
========

This module implements command search tools. It is possible to execute python
functions to highlight patterns of text and replace patterns.

"""

from vyapp.plugins import Command

@Command()
def find(area, regex, handle, *args, **kwargs):
    """
    Execute handle for each one of the regex matches. The handle
    receives:

        def handle(chunk, start, end):
            pass

    The kwargs argument accepts:

    index='1.0', stopindex='end', forwards=None, 
    backwards=False, exact=False, regexp=True, nocase=False, elide=False, 
    nolinestop=False
    """
    seq = area.find(regex, *args, **kwargs)    
    for ind in seq:
        handle(*ind)

@Command()
def sniff(area, regex, handle, *args, **kwargs):
    """
    For each regex match in the areavi it calls handle with:

    def handle(chunk, start, end):
        pass

    The kwargs argument accepts:

    index='1.0', stopindex='end', forwards=None, 
    backwards=False, exact=False, regexp=True, nocase=False, elide=False, 
    nolinestop=False

    """
    seq = area.collect('sel', regex, *args, **kwargs) 
    for ind in seq:
        handle(*ind)

@Command()
def sel(area, regex, *args, **kwargs):
    """
    Add selection to all regex matches in the AreaVi instance.

    The kwargs argument accepts:

    index='1.0', stopindex='end', forwards=None, 
    backwards=False, exact=False, regexp=True, nocase=False, elide=False, 
    nolinestop=False
    """
    area.select_matches('sel', 
    area.find(regex, *args, **kwargs))

@Command()
def gsub(area, regex, data, *args, **kwargs):
    """
    It replaces all regex matches for data. The data argument may be a callable
    object. When it is a callable object it looks like:

    def handle(chunk, start, end):
        pass

    The kwargs argument accepts:

    index='1.0', stopindex='end', forwards=None, 
    backwards=False, exact=False, regexp=True, nocase=False, elide=False, 
    nolinestop=False

    """
    area.replace_all(regex, data, *args, **kwargs)

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
def lsub(area, regex, data, *args):
    """
    Replae text in a selected region of an AreaVi instance.

    The kwargs argument accepts:

    index='1.0', stopindex='end', forwards=None, 
    backwards=False, exact=False, regexp=True, nocase=False, elide=False, 
    nolinestop=False

    """
    area.replace_ranges('sel', regex, data, *args)
