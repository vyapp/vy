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
Event: <Alt-z>
Description: Set an AreaVi instance as target for commands.

Mode: NORMAL
Event: <Key-semicolon>
Description: Executes a sequence of python code that is selected.

Mode: Global
Event: <Alt-semicolon>
Description: Open an input box in order to type inline python code to be executed.

"""

from vyapp.plugins import Command
from traceback import print_exc as debug
from vyapp.tools import exec_pipe
from vyapp.ask import Ask
from vyapp.plugins import ENV
from vyapp.app import root
import sys

class Cmd:
    def __init__(self, area):
        self.area = area

        area.install('cmd',
        (-1, '<Alt-semicolon>',  self.exec_cmd),
        ('NORMAL', '<Key-semicolon>', self.exec_region),
        (-1, '<Alt-z>',  self.set_target))
        
    def exec_cmd(self, event):
        ask = Ask()
        self.area.active()
        Command.set_target(self.area)
        sys.stdout.write('\nLine executed:\n%s\n>>>\n' % ask.data)
    
        data = ask.data.encode('utf-8')
        exec_pipe(data, ENV)
        return 'break'
    
    def exec_region(self, event):
        data = self.area.join_ranges('sel')
        sys.stdout.write('\nRegion executed:\n%s\n>>>\n' % data)
    
        data = data.encode('utf-8')
        exec_pipe(data, ENV)
        self.area.clear_selection()
    
    def set_target(self, event):
        Command.set_target(self.area)

        self.area.active()
        root.status.set_msg('Set command target !')
        return 'break'
    

install = Cmd