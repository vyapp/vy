"""
Overview
========


Key-Commands
============

Namespace: delve

Mode: GOLANG
Event? <Key-1>
Description: 

Mode: GOLANG
Event: <Key-2>
Description: 

Mode: GOLANG
Event? <Key-c>
Description: 

Mode: GOLANG
Event: <Key-e>
Description: 

Mode: GOLANG
Event: <Key-w>
Description: 

Mode: GOLANG
Event: <Key-a>
Description: 

Mode: GOLANG
Event: <Key-b>
Description: 

Mode: GOLANG
Event: <Key-B>
Description: 

Mode: GOLANG
Event: <Control-C>
Description: 

Mode: GOLANG
Event: <Control-c>
Description: 

Mode: GOLANG
Event: <Control-s>
Description: 

Mode: GOLANG
Event: <Key-x>
Description: 

Mode: GOLANG
Event: <Key-r>
Description: 

Mode: GOLANG
Event: <Key-q>
Description: 

"""

from untwisted.network import Device
from subprocess import Popen, PIPE, STDOUT
from untwisted.iofile import Stdin, Stdout, CLOSE
from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from untwisted.network import spawn, xmap
from untwisted.splits import Terminator
from re import search
from vyapp.ask import Ask
from vyapp.areavi import AreaVi
from vyapp.app import root
import shlex
import sys

class Delve:
    setup={'background':'blue', 'foreground':'yellow'}
    encoding='utf8'

    def __call__(self, area):
        self.area = area
        
        area.install('delve', 
        ('GOLANG', '<Key-p>', self.send_print),
        ('GOLANG', '<Key-x>', self.evaluate_expression), 
        ('GOLANG', '<Key-r>', self.execute_statement), 
        ('GOLANG', '<Key-1>', self.start_debug), 
        ('GOLANG', '<Key-2>', self.start_debug_args), 
        ('GOLANG', '<Key-q>', self.quit_delve), 
        ('GOLANG', '<Key-c>', self.send_continue), 
        ('GOLANG', '<Key-e>', self.evaluate_selection), 
        ('GOLANG', '<Key-w>', self.send_where), 
        ('GOLANG', '<Key-a>', self.send_args), 
        ('GOLANG', '<Key-s>', self.send_step), 
        ('GOLANG', '<Control-C>', self.dump_clear_all), 
        ('GOLANG', '<Control-c>', self.remove_breakpoint),
        ('GOLANG', '<Key-B>',  self.send_tbreak),
        ('GOLANG', '<Key-b>', self.send_break))


    def __init__(self):
        pass

delve     = Delve()
install = delve




