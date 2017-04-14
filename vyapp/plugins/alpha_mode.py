"""
Overview
========

This is an auxiliary mode that implements keycommands that aren't often used.

Key-Commands
============

Namespace: alpha-mode

Mode: NORMAL
Event: <Key-3>
Description: Get the AreaVi instance that is focused in ALPHA mode.
"""

def alpha(area):
    area.chmode('ALPHA')

def install(area):
    area.add_mode('ALPHA')
    area.install('alpha-mode', ('NORMAL', '<Key-3>', lambda event: alpha(event.widget)))





