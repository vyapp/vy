"""
Overview
========

Used to spawn processes and send/receive data. It is useful to talk with extern processes like interpreters.

Usage
=====

Key-Commands
============

Mode: NORMAL
Event: <F2>
Description: Send the cursor line to the process.

Mode: INSERT
Event: <F2>
Description: Send the cursor line to the process and insert a line down.
"""

from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.network import xmap
from vyapp.ask import Ask
from vyapp.tools import set_status_msg
from vyapp.exe import exec_quiet
from Tkinter import TclError
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

import shlex

class Shell(object):
    def __init__(self, data):
        self.area = AreaVi.ACTIVE

        try:
            self.expect = Expect(*shlex.split(data))
        except Exception as e:
            set_status_msg(e)
        else:
            self.create_output()
        
    def create_output(self):
        """

        """

        self.output = self.area.master.master.create()
    
        # When one of the AreaVi instances are destroyed then
        # the process is killed.
        self.output.hook(-1, '<Destroy>', lambda event: 
        self.terminate_process())
        self.area.hook(-1, '<Destroy>', lambda event: 
        self.terminate_process())

        self.output.hook('NORMAL', '<Control-F2>', lambda event: 
        self.map_commands())

        self.map_commands()
        # When call.terminnate is called it may happen of having still data to be
        # processed. It would attempt to write on an AreaVi instance that no more exist.
        # So, it executes quietly the AreaVi.append method.
        xmap(self.expect, LOAD, lambda expect, data: 
        exec_quiet(self.output.append, data))

        xmap(self.expect, CLOSE, self.handle_close)

    def map_commands(self):
        self.area.hook('NORMAL', '<F2>', lambda event: 
        self.dump_line_and_down(), add=False)

        self.area.hook('INSERT', '<F2>', lambda event: 
        self.dump_line_and_insert_line(), add=False)
        set_status_msg('%s -> %s' % (self.area.filename, self.output.filename))

    def terminate_process(self):
        try:
            self.expect.terminate()
        except Exception:
            pass
        set_status_msg('Killed process!')

    def dump_line_and_down(self):
        self.expect.send(self.area.curline())
        self.area.down()

    def dump_line_and_insert_line(self):
        self.expect.send(self.area.curline())
        self.area.down()

    def handle_close(self, expect):
        set_status_msg('Killed process!')
        expect.destroy()

ENV['Shell']  = Shell




