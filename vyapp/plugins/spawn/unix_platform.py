"""
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
import shlex

class Spawn(BaseSpawn):
    def __init__(self, cmd):
        self.child   = Popen(shlex.split(cmd), 
        shell=0, stdout=PIPE, stdin=PIPE, preexec_fn=setsid, 
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
        data = self.input.curline().encode(self.input.charset)
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

ENV['hspawn'] = HSpawn
ENV['vspawn'] = VSpawn

ENV['vbash']  = lambda : VSpawn('bash -i')
ENV['hbash'] = lambda : HSpawn('bash -i')




