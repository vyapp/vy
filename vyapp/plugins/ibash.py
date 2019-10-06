""" 
Overview
========

This plugin is used to control a bash process. It is possible to run commands 
and start processes through bash and send some unix signals to the child processes.

Key-Commands
============

Namespace: ibash

Mode: NORMAL
Event: <Control-C>
Description: Send a SIGINT signal to the bash interpreter.

Mode: NORMAL
Event: <Shift-Return>
Description: Send the cursor line to the bash interpreter.

Mode: NORMAL
Event: <Control-F9>
Description: Send the region of code that is selected to the bash interpreter.

Mode: NORMAL
Event: <F9>
Description: Ask for the user to type a command to be dropped to the bash interpreter.

Commands
========

Command: lsh
Description: Restart the underlying bash process.

"""


from untwisted.network import core, xmap, READ, WRITE, Device
from vyapp.app import root
from vyapp.base import printd
from untwisted.iofile import *
from vyapp.ask import Ask
from subprocess import Popen, PIPE, STDOUT
from os import environ, setsid, killpg
from vyapp.tools import error
from vyapp.plugins import ENV
import sys

class Process(object):
    def __call__(self, area):
        area.install('ibash', 
        ('NORMAL', '<Control-F9>', lambda event: self.dump_region(event.widget)),
        ('NORMAL', '<Shift-Return>', lambda event: self.dump_line(event.widget)),
        ('NORMAL', '<F9>', lambda event: self.ask_data_and_dump(event.widget)),
        ('NORMAL', '<Control-C>', self.dump_signal))
        ENV['lsh'] = self.restart

    def __init__(self, cmd=['bash', '-i']):
        self.cmd = cmd
        self.start()

    def start(self):
        print('Ibash - Bash process started...')
        self.child  = Popen(self.cmd, shell=0, stdout=PIPE, stdin=PIPE, 
                            preexec_fn=setsid, stderr=STDOUT,  env=environ)
        

        self.stdout = Device(self.child.stdout)
        self.stdin  = Device(self.child.stdin)

        Stdout(self.stdout)
        Stdin(self.stdin)

        xmap(self.stdout, LOAD, lambda con, data: sys.stdout.write(data.decode('utf8')))
        xmap(self.stdin, CLOSE, lambda dev, err: lose(dev))
        xmap(self.stdout, CLOSE, lambda dev, err: lose(dev))

    def restart(self):
        """
        Restart ibash process.
        """

        self.child.kill()
        self.start()

        root.status.set_msg('Process killed and started !')

    def dump_tab(self, area):
        data = area.get('insert linestart', 'insert -1c lineend')
        data = data.encode('utf-8')
        self.stdin.dump('%s\t\t' % data)

    def dump_region(self, area):
        data = area.join_ranges('sel')
        data = data.encode('utf-8')
        self.stdin.dump(data)

    def dump_line(self, area):
        data = area.get('insert linestart', 'insert +1l linestart')
        data = data.encode('utf-8')
        self.stdin.dump(data)
        area.down()

    def ask_data_and_dump(self, area):
        ask = Ask()

        if ask.data:
            self.stdin.dump(b'%s\n' %  ask.data.encode('utf-8'))

    def dump_signal(self, event):
        root.status.set_msg('(ibash) Signal number SIGINT(2)/SIGQUIT(3):')
        ask    = Ask()
        signal = None

        try:
            signal = int(ask.data)
        except ValueError as e:
            root.status.set_msg('(ibash) Invalid signal')
        killpg(self.child.pid, signal)

process = Process()
install = process



