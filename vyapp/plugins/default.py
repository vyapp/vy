"""
Overview
========

This module implements functionalities to handle what happens when files are loaded
and when AreaVi widgets are selected by mouse clicks.

Key-Commands
============

Namespace: default

Mode: -1
Event: <ButtonPress>
Description: The AreaVi widget gets focus.

Mode: -1
Event: <<LoadData>>
Description: The cursor will be placed in the beginning at the beginning
of the loaded file.
"""


def install(area):
    area.install('default', (-1, '<ButtonPress>', lambda event: event.widget.focus()),
           (-1, '<<LoadData>>', lambda event: event.widget.go_text_start()))





