"""
Overview
========

This module implements one of the auxiliary modes that implements keycommands 
that aren't very often used.

Key-Commands
============

Namespace: beta-mode

Mode: NORMAL
Event: <Key-4>
Description: Get the AreaVi instance in BETA mode.
"""

def beta(area):
    area.chmode('BETA')

def install(area):
    area.add_mode('BETA')
    area.install('beta-mode', ('NORMAL', '<Key-4>', lambda event: beta(event.widget)))





