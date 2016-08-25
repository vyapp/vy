"""
Overview
========

This plugin implements python functions to get text in lower case and upper case.

Commands
========

Command: lower()
Description: Turn the selected text into lower case.

Command: uppwer()
Description: Turn the selected text into upper case.
"""

from vyapp.areavi import AreaVi
from vyapp.plugins import ENV

def transform(func):
    map  = AreaVi.ACTIVE.tag_ranges('sel')
    for index in xrange(0, len(map) - 1, 2):
        data = AreaVi.ACTIVE.get(map[index], map[index + 1])
        AreaVi.ACTIVE.delete(map[index], map[index + 1])
        AreaVi.ACTIVE.insert(map[index], func(data))

def lower():
    transform(lambda data: data.lower())

def upper():
    transform(lambda data: data.upper())


ENV['lower'] = lower
ENV['upper'] = upper


