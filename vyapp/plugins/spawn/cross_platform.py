"""
Overview
========

Used to spawn processes and send/receive data. It is useful to talk with extern processes like interpreters.

Key-Commands
============

Namespace: shell

Mode: NORMAL
Event: <F1>
Description: Send the cursor line to the process.

Mode: INSERT
Event: <F1>
Description: Send the cursor line to the process and insert a line down.
"""

from untwisted.expect import Expect, LOAD, CLOSE
from vyapp.plugins.spawn.base_spawn import BaseSpawn
from vyapp.plugins import Command
from vyapp.plugins import ENV
from vyapp.app import root
from os import environ 

import shlex

class Spawn(BaseSpawn):
    def __init__(self, cmd):
        self.expect = Expect(*shlex.split(cmd), env=environ)

    def install_events(self):
        super(Spawn, self).install_events()

        # When call.terminnate is called it may happen of having still data to be
        # processed. It would attempt to write on an AreaVi instance that no more exist.
        # So, it executes quietly the AreaVi.append method.
        self.expect.add_map(LOAD, lambda expect, data: self.output.append(data))
        self.expect.add_map(CLOSE, self.handle_close)
        
    def dump_signal(self, num):
        self.expect.child.send_signal(num)

    def terminate_process(self):
        # Exceptions should be written to sys.stdout for default.
        self.expect.terminate()
        root.status.set_msg('Killed process!')

    def dump_line(self):
        data = self.input.get('insert linestart', 'insert +1l linestart')
        data = data.encode(self.input.charset)
        self.expect.send(data)
        self.input.down()

    def handle_close(self, expect):
        root.status.set_msg('Killed process!')
        expect.destroy()

class HSpawn(Spawn):
    def __init__(self, cmd):
        Spawn.__init__(self, cmd)
        BaseSpawn.__init__(self, cmd, Command.area, 
        Command.area.master.master.create())

class VSpawn(Spawn):
    def __init__(self, cmd):
        Spawn.__init__(self, cmd)
        BaseSpawn.__init__(self, cmd, Command.area, 
        Command.area.master.master.master.create())

ENV['hspawn'] = HSpawn
ENV['vspawn'] = VSpawn




