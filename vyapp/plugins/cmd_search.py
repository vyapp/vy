"""
Overview
========

This module implements command search tools. It is possible to execute python
functions to highlight patterns of text and replace patterns.

"""

from vyapp.plugins import Command
from vyapp.areavi import AreaVi

@Command()
def find(area, regex, handle, index='1.0', stopindex='end', 
    backwards=False, exact=False, regexp=True, nocase=False, 
    elide=False, nolinestop=False, step=''):

    """
    Execute handle for each one of the regex matches in the target 
    Areavi instance. The handle receives:

    Example:

        def handle(data, start, end):
            print('Match:' data, 'Start:%s', 'End:', end)

        find('foobar', handle)
    
    """

    seq = area.find(regex, index, stopindex, backwards, exact, 
    regexp, nocase, elide, nolinestop, step)

    for ind in seq:
        handle(*ind)

@Command()
def sniff(area, regex, handle, index='1.0', stopindex='end', exact=False, 
    regexp=True, nocase=False, elide=False, nolinestop=False, step=''):

    """
    Perform regex match in the selected text.

    """

    seq = area.collect('sel', regex, index, stopindex, 
    exact, regexp, nocase, elide, nolinestop, step)

    for ind in seq:
        handle(*ind)

@Command()
def sel(area, regex, index='1.0', stopindex='end', exact=False, 
    regexp=True, nocase=False, elide=False, nolinestop=False, step=''):

    """
    Add selection to all regex matches in the AreaVi instance.
    """
    matches = area.find(regex, index, stopindex, False, exact, 
    regexp, nocase, elide, nolinestop, step)

    for _, index0, index1 in matches:
        area.tag_add('sel', index0, index1)

@Command()
def split(area, *args, **kwargs):
    """
    """
    area.select_matches('sel', 
    area.split(*args, **kwargs))

@Command()
def lsub(area, regex, data, exact=False, regexp=True, 
    nocase=False, elide=False, nolinestop=False, step=''):

    """
    Replae text in a selected region of an AreaVi instance.

    """

    area.replace_ranges('sel', regex, data, exact=False, 
    regexp=True, nocase=False, elide=False, nolinestop=False)

Command('gsub')(AreaVi.replace_all)
Command('get')(AreaVi.get)
