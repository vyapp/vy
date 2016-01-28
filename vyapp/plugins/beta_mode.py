"""
Overview
========

This module implements one of the auxiliary modes that implements keycommands 
that aren't very often used.

Usage
=====

In order to get the focused AreaVi instance in BETA mode, press <Key-4> em NORMAL mode.

Key-Commands
============

Mode: NORMAL
Event: <Key-4>
Description: Get the AreaVi instance in BETA mode.
"""

def beta(area):
    area.chmode('BETA')

def install(area):
    area.add_mode('BETA')
    area.install(('NORMAL', '<Key-4>', lambda event: beta(event.widget)))


