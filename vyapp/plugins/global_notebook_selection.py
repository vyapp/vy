"""
Overview
========

This plugin is used to switch focus between notebook tabs using the alt key in global mode.

Usage
=====

Key-Commands
============

"""

from vyapp.plugins import notebook

def select_left():
    notebook.select_left()
    return 'break'

def select_right():
    notebook.select_right()
    return 'break'

def install(area):
    area.install((-1, '<Alt-o>', lambda event: select_left()), 
                 (-1, '<Alt-p>', lambda event: select_right()))



