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

Mode: NORMAL
Event: <Control-W>
Description: Delete all the output dropped on an AreaVi instance.

Mode: NORMAL
Event: <Control-Tab>
Description: it restores sys.stdout.

Mode: NORMAL
Event: <Control-w> 
Description: It removes a given AreaVi instance from having output written in.

Mode: NORMAL
Event: <Tab>
Description: It redirects output from sys.stdout to a given AreaVi instance.
"""

from traceback import format_exc as debug
from vyapp.stdout import Stdout
from vyapp.exe import exec_quiet
from vyapp.ask import *
from vyapp.app import root
import sys

def redirect_stdout(area):
    try:
        sys.stdout.remove(area)
    except ValueError:
        pass
    sys.stdout.append(Stdout(area))
    root.status.set_msg('Output redirected to %s' % area.index('insert'))

def install(area):
    area.install(('NORMAL', '<Control-W>', lambda event: event.widget.delete_ranges(Stdout.TAG_CODE)),
           ('NORMAL', '<Control-Tab>', lambda event: sys.stdout.restore()),
           ('NORMAL', '<Key-W>', lambda event: event.widget.tag_delete(Stdout.TAG_CODE)),
           ('NORMAL', '<Control-w>', lambda event: exec_quiet(sys.stdout.remove, event.widget)),
           ('NORMAL', '<Tab>', lambda event: redirect_stdout(event.widget)))




