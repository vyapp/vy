"""
Overview
========

This plugin implements Key-Commands to redirect the default python sys.stdout object
to an AreaVi instance. As it is possible to drop python code to vy in order
to affect the editor state, the python interpreter writes output to
sys.stdout. 

With this plugin it is possible to drop the output to a given 
Line.Col inside an AreaVi instance.

Key-Commands
============

Mode: Global
Event: <Control-Alt-bracketleft>
Description: it restores sys.stdout.

Mode: Global
Event: <Alt-braceleft> 
Description: It removes a given AreaVi instance from having output written in.

Mode: Global
Event: <Alt-bracketleft>
Description: It redirects output from sys.stdout to a given AreaVi instance.
"""

from vyapp.stdout import Stdout
from vyapp.app import root
import sys

def add_output_target(event):
    try:
        sys.stdout.remove(event.widget)
    except ValueError:
        pass

    sys.stdout.append(Stdout(event.widget))
    root.status.set_msg('Output set on: %s' % \
    event.widget.index('insert'))
    return 'break'

def rm_output_target(event):
    try:
        sys.stdout.remove(event.widget)
    except Exception:
        root.status.set_msg('Output removed!')
    else:
        root.status.set_msg('Output removed!')
    return 'break'

def restore_default_target(event):
    sys.stdout.restore()
    root.status.set_msg('Stdout restored!')
    return 'break'

def install(area):
    area.install((-1, '<Alt-bracketleft>', add_output_target),
    (-1, '<Alt-braceleft>', rm_output_target),
    (-1, '<Control-Alt-bracketleft>',  restore_default_target))







