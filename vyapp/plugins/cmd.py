"""
Overview
========

It implements functionalities to execute python code that affects vy state. 

With this plugin it is possible to drop the output to a given 
Line.Col inside an AreaVi instance.

Key-Commands
============

Namespace: cmd

Mode: Global
Event: <Control-Alt-semicolon>
Description: Set an AreaVi instance as target for commands.

Mode: NORMAL
Event: <Key-semicolon>
Description: Executes a sequence of python code that is selected.

Mode: Global
Event: <Alt-semicolon>
Description: Open an input box in order to type inline python code to be executed.

"""

from traceback import print_exc as debug
from vyapp.tools import exec_pipe
from vyapp.ask import Ask
from vyapp.plugins import ENV
from vyapp.app import root
import sys

def exec_cmd(area, env):
    ask = Ask()
    area.active()
    sys.stdout.write('\nLine executed:\n%s\n>>>\n' % ask.data)

    data = ask.data.encode('utf-8')
    exec_pipe(data, env)
    return 'break'

def exec_region(area, env):
    data = area.join_ranges('sel')
    sys.stdout.write('\nRegion executed:\n%s\n>>>\n' % data)

    data = data.encode('utf-8')
    exec_pipe(data, env)
    area.clear_selection()

def set_target(area):
    area.active()
    root.status.set_msg('Target set!')
    return 'break'

install = lambda area: area.install('cmd',
(-1, '<Alt-semicolon>', lambda event: exec_cmd(event.widget, ENV)),
('NORMAL', '<Key-semicolon>', lambda event: exec_region(event.widget, ENV)),
(-1, '<Control-Alt-semicolon>', lambda event: set_target(event.widget)))


