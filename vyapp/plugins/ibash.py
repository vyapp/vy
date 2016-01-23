""" To be able to run commands as root you can use sudo. You need to specify
export SUDO_ASKPASS=/usr/bin/ssh-askpass in your .bashrc file.

To log on as root.
sudo bash -i
"""


from untwisted.network import core, xmap, cmap, READ, WRITE, Device
from untwisted.tkinter import extern
from untwisted.utils.iofd import *
from vyapp.app import root
from vyapp.tools import set_status_msg
from vyapp.ask import Ask

from subprocess import Popen, PIPE, STDOUT
from os import environ, setsid, killpg
import sys

class Process(object):
    def __call__(self, area):
        area.install(('NORMAL', '<Control-Return>', lambda event: self.dump_region(event.widget)),
                   ('NORMAL', '<Return>', lambda event: self.dump_line(event.widget)), 
                   ('INSERT', '<F1>', lambda event: self.dump_line_and_insert_line(event.widget)),
                   ('INSERT', '<Shift-F1>', lambda event: self.dump_line_and_tab(event.widget)),
                   ('NORMAL', '<F1>', lambda event: self.dump_line_and_down(event.widget)),
                   ('NORMAL', '<Control-F1>', lambda event: self.restart()),
                   ('NORMAL', '<Control-semicolon>', lambda event: self.ask_data_and_dump(event.widget)),
                   ('NORMAL', '<Control-backslash>', lambda event: self.dump_signal(3)),
                   ('NORMAL', '<Control-c>', lambda event: self.dump_signal(2)))


    def __init__(self, cmd=['bash', '-i']):
        self.cmd = cmd
        self.start()

    def start(self):
        self.child   = Popen(self.cmd, shell=0, stdout=PIPE, stdin=PIPE, 
                             preexec_fn=setsid, stderr=STDOUT,  env=environ)
        

        self.stdout  = Device(self.child.stdout)
        self.stdin   = Device(self.child.stdin)

        Stdout(self.stdout)
        Stdin(self.stdin)

        xmap(self.stdout, LOAD, lambda con, data: sys.stdout.write(data))
        xmap(self.stdin, CLOSE, lambda dev, err: lose(dev))
        xmap(self.stdout, CLOSE, lambda dev, err: lose(dev))

    def restart(self):
        self.child.kill()
        self.start()

        set_status_msg('Process killed and started !')

    def dump_line_and_tab(self, area):
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

    def dump_line_and_down(self, area):
        data = area.get('insert linestart', 'insert +1l linestart')
        data = data.encode('utf-8')
        self.stdin.dump(data)
        area.down()
    
    def dump_line_and_insert_line(self, area):
        data = area.get('insert linestart', 'insert +1l linestart')
        data = data.encode('utf-8')

        self.stdin.dump(data)
        area.insert_line_down()

    def ask_data_and_dump(self, area):
        ask  = Ask(area)
        data = ask.data.encode('utf-8')
        self.stdin.dump('%s\n' %  data)

    def dump_signal(self, signal):
        killpg(self.child.pid, signal)
    
extern(root)
process = Process()
install = process











