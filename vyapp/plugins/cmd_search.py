"""
Overview
========

This module implements command search tools. It is possible to execute python
functions to highlight patterns of text and replace patterns.

Usage
=====

Set an AreaVi instance as target for command with <Control-E>
then execute the functions below with <Control-e>. In case of using
<Control-semicolon> there is no need to set a target for command since
that key-command automatically sets the AreaVi instance that has focus as target for commands.

Commands
========

Command: find(self, regex, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None):
Description: Highlight patterns in the AreaVi instance that has focus.
regex     = The pattern to be searched.
index     = The starting index of the search.
stopindex = The stop index of the search.

Command: replace_all(self, regex, data, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
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

ENV['find'] = lambda *args, **kwargs: AreaVi.ACTIVE.tag_add_found('sel', AreaVi.ACTIVE.find(*args, **kwargs))
ENV['sub'] = lambda *args, **kwargs: AreaVi.ACTIVE.replace_all(*args, **kwargs)
ENV['get'] = lambda *args: AreaVi.ACTIVE.get(*args)




