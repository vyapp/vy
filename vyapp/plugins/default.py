"""
Overview
========

This module implements functionalities to handle what happens when files are loaded
and when AreaVi widgets are selected by mouse clicks.

Usage
=====

When an AreaVi widget receives a mouse click then this module defines that the AreaVi
widget will gain focus.

When a file is opened in an AreaVi widget then the cursor will be placed at the beginning
of the file.

Key-Commands
============

Mode: -1
Event: <ButtonPress>
Description: The AreaVi widget gets focus.

Mode: -1
Event: <<LoadData>>
Description: The cursor will be placed in the beginning at the beginning
of the loaded file.
"""


def install(area):
    area.install((-1, '<ButtonPress>', lambda event: event.widget.focus()),
           (-1, '<<LoadData>>', lambda event: event.widget.go_text_start()))


