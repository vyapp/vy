"""
Overview
========

Used to spawn new processes, this module works only on unix-like
platforms.

Commands
========

Command: hbash
Description: Start a new bash process whose output
is directed to a horizontal pane.

Command: vbash
Description: Start a new bash process whose output
is directed to a vertical pane.

Command: vpy
Description: Start a python interpreter process
in a vertical pane.

Command: hpy
Description: Start a python interpreter process
in a horizontal pane.

Command: vrb
Description: Start a ruby interpreter process
in a vertical pane.

Command: hrb
Description: Start a ruby interpreter process
in a horizontal pane.

Notes
=====

**Run python from your bash process**

tee -i >(stdbuf -o 0 python -i -u)

**Run ruby from your bash process**

stdbuf -o 0 irb --inf-ruby-mode

The above commands could be slightly modified
to work with other interpreters. 

"""

from untwisted.iofile import Stdout, Stdin, LOAD, CLOSE
from untwisted.network import Device
from vyapp.plugins import ENV
from vyapp.ask import Ask

from subprocess import Popen, PIPE, STDOUT
from os import environ, setsid, killpg
from vyapp.plugins.spawn.base_spawn import BaseSpawn
from vyapp.areavi import AreaVi
from vyapp.app import root
from os import environ 

class Spawn(BaseSpawn):
    def __init__(self, cmd):
        self.child   = Popen(cmd, 
        shell=True, stdout=PIPE, stdin=PIPE, preexec_fn=setsid, 
        stderr=STDOUT,  env=environ)
        

        self.stdout  = Device(self.child.stdout)
        self.stdin   = Device(self.child.stdin)

    def install_events(self):
        super(Spawn, self).install_events()

        Stdout(self.stdout)
        Stdin(self.stdin)

        self.stdout.add_map(LOAD, lambda con, data: \
        self.output.append(data))

        self.stdin.add_map(CLOSE, self.handle_close)
        self.stdout.add_map(CLOSE, self.handle_close)

    def dump_signal(self, num):
        killpg(self.child.pid, num)

    def terminate_process(self):
        self.child.kill()
        root.status.set_msg('Killed process!')

    def dump_line(self):
        data = self.input.get('insert linestart', 'insert +1l linestart')
        data = data.encode(self.input.charset)
        self.stdin.dump(data)
        self.input.down()

    def handle_close(self, dev, err):
        root.status.set_msg('Killed process!')
        self.stdout.destroy()
        self.stdin.destroy()

class HSpawn(Spawn):
    def __init__(self, cmd):
        Spawn.__init__(self, cmd)
        BaseSpawn.__init__(self, cmd, AreaVi.ACTIVE, 
        AreaVi.ACTIVE.master.master.create())

class VSpawn(Spawn):
    def __init__(self, cmd):
        Spawn.__init__(self, cmd)
        BaseSpawn.__init__(self, cmd, AreaVi.ACTIVE, 
        AreaVi.ACTIVE.master.master.master.create())

ENV['hspawn']  = HSpawn
ENV['vspawn']  = VSpawn
ENV['vbash']   = lambda : VSpawn('bash -i')
ENV['hbash']   = lambda : HSpawn('bash -i')
ENV['hpy'] = lambda : HSpawn('bash -c "tee -i >(stdbuf -o 0 python -i -u)"')
ENV['vpy'] = lambda : VSpawn('bash -c "tee -i >(stdbuf -o 0 python -i -u)"')

ENV['hrb'] = lambda : HSpawn('bash -c "stdbuf -o 0 irb --inf-ruby-mode"')
ENV['vrb'] = lambda : VSpawn('bash -c "stdbuf -o 0 irb --inf-ruby-mode"')






