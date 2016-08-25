"""
Overview
========

This plugin implements word tools.

Commands
========

Command: cw()
Description: Count the number of words that appear in the AreaVi widget that was
set as command target. The result would appear at the statusbar.
"""

from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from re import findall
from vyapp.app import root

def cw():
    area = AreaVi.ACTIVE

    data = area.get('1.0', 'end')
    root.status.set_msg('Count of words:%s' % len(findall('\W+', data)))

ENV['cw'] = cw




