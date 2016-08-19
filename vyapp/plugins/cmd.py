"""
Overview
========

It implements functionalities to execute python code that affects vy state. 

Usage
=====

In order to use the functionalities of this module it is needed to introduce the concept of target that is implemented
in vy. It is possible to instantiate more than an AreaVi instance at the same time, along tabs, panels etc. Each one
of these AreaVi instances can be set as a target for commands. It means that commands should affect the AreaVi instance that was
set as target. 

Consider the following scenary where there are two vy panes.


----------------------
| HELLO | CPPaste()  |
----------------------

CPPaste is a python function that posts code onto codepad.org. In order to set as target the pane that has the string
HELLO written on, move the focus to that AreaVi instance then press <Control-Alt-semicolon>, it will appear the msg 'Target set!'
at the statusbar. Once the target is set then it is possible to execute CPPaste() by selecting it then dropping
it to the python interpreter by switching to NORMAL mode then pressing <Key-semicolon>. You will notice
your default browser being opened and the string HELLO being posted at codepad.org. Try setting
the pane that has the string CPPaste() written on as target then executing it, you'll notice that CPPaste()
posted onto codepad.org the string CPPaste(). It is possible to have only one target set for commands.

There is another important key command implemented in this module, such a key command permits
to execute inline python code. There is no need to set a target when using <Alt-semicolon> in Global mode
because it uses the AreaVi instance that has focus as target for the commands.

It is important to notice that the python code is executed inside vyapp.plugins.ENV dictionary.

Key-Commands
============

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


from vyapp.tools import set_status_msg
from vyapp.exe import exc
from vyapp.ask import Ask
from vyapp.plugins import ENV

import sys

def exec_cmd(area, env):
    ask    = Ask(area)
    area.active()
    exc(ask.data, env)
    return 'break'

def exec_region(area, env):
    data = area.join_ranges('sel')
    data = data.encode('utf-8')
    exc(data, env)
    area.clear_selection()

def exec_all_data(area, env):
    data = area.get('1.0', 'end')
    data = data.encode('utf-8')
    exc(data, env)
    return 'break'

def set_target(area):
    area.active()
    set_status_msg('Target set !')
    return 'break'

install = lambda area: area.install(
(-1, '<Alt-semicolon>', lambda event: exec_cmd(event.widget, ENV)), 
(-1, '<Alt-colon>', lambda event: exec_all_data(event.widget, ENV)),
('NORMAL', '<Key-semicolon>', lambda event: exec_region(event.widget, ENV)),
(-1, '<Control-Alt-semicolon>', lambda event: set_target(event.widget)))



