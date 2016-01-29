"""
Overview
========

This plugin implements word tools.

Usage
=====

In order to use some functions it is needed to set an AreaVi widget as target for commands.
It implements the cw function that is used to count the number of words
that a given AreaVi widget has.

Commands
========

Command: cw()
Description: Count the number of words that appear in the AreaVi widget that was
set as command target. The result would appear at the statusbar.
"""

from vyapp.areavi import AreaVi
from vyapp.tools import set_status_msg
from vyapp.plugins import ENV
from re import findall

def cw():
    area = AreaVi.ACTIVE

    data = area.get('1.0', 'end')
    set_status_msg('Count of words:%s' % len(findall('\W+', data)))

ENV['cw'] = cw


