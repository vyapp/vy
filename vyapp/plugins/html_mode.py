"""
Overview
========

Extra mode for dealing with HTML.

Key-Commands
============

Namespace: html-mode

Mode: NORMAL
Event: <Key-at>
Description: Switch to HTML mode.
"""

from vyapp.plugins import Namespace

class HmtlModeNS(Namespace):
    pass

def html_mode(area):
    area.chmode('HTML')

def install(area):
    area.add_mode('HTML')
    area.install(HmtlModeNS, ('NORMAL', '<Key-at>', 
    lambda event: html_mode(area)))



