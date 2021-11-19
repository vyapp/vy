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

    seq = area.tag_xmatch('sel', regex, index, stopindex, 
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

    matches = area.split(*args, **kwargs)
    for _, index0, index1 in matches:
        area.tag_add('sel', index0, index1)

@Command()
def lsub(area, regex, data, exact=False, regexp=True, 
    nocase=False, elide=False, nolinestop=False, step=''):

    """
    Replace text in a selected region of an AreaVi instance.

    Note: The search for regex will be performed along all ranges
    that correspond to the selected text. 

    The length of such matches may be longer than its 
    corresponding selected ranges.

    Consider regex as '.+' and as a selected region 'abc' a text 'abcdefg'.
    When invoking lsub with '.+' it will replace 'abcdefg' for data.

    In case it is used '.' as regex in the above scheme 
    it will replace only 'abc' for the specified data.
    """

    area.tag_xsub('sel', regex, data, exact=exact, 
    regexp=regex, nocase=nocase, elide=elide, nolinestop=nolinestop)

Command('gsub')(AreaVi.replace_all)
Command('get')(AreaVi.get)
