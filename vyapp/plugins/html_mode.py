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

def html_mode(area):
    area.chmode('HTML')

def install(area):
    area.add_mode('HTML')
    area.install('html-mode', ('NORMAL', '<Key-at>', 
    lambda event: html_mode(area)))



