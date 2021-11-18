"""
Overview
========

Quickly edit your vyrc file.

Key-Commands
============

Mode: EXTRA
Event: <Alt-v>
Description: Load your ~/.vy/vyrc file in the current
AreaVi instance.

"""

from vyapp.app import root

def loadrc(event):
    event.widget.load_data(root.rc)
    event.widget.chmode('NORMAL')

def install(area):
    area.install('editrc', ('EXTRA', '<Key-v>', loadrc))




