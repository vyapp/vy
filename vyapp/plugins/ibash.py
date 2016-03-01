""" 
Overview
========

This plugin is used to control a bash process. It is possible to run commands 
and start processes through bash and send some unix signals to the child processes.

Usage
=====

This plugin writes to sys.stdout object, in order to read output from the bash interpreter
it is first needed to select an output target by setting the focus to an AreaVi instance
and pressing <Tab> in NORMAL mode. For a better explanation on output targets, check out:

    help(vyapp.plugins.output_scheme)

The most common keycommand that this module implements is the one to drop a code 
line to the bash interpreter. In order to drop a code line, place the cursor at the 
line that should be sent to the bash interpreter then press <F1> in INSERT mode 
or in NORMAL mode. When <F1> is pressed in INSERT mode it drops the cursor line to 
the bash interpreter and it adds a new line down the cursor position.  
When <F1> is pressed in NORMAL mode it drops the code line and places the cursor one line 
down. Sometimes it is useful to merely drop the cursor line but keeping the cursor in the 
current line. In order to drop the cursor line  and not having the cursor placed down, 
press <Return>.

Sometimes it is interesting to drop an entire region of code to the bash interpreter, for such
select the region then press <Control-Return>, all the code that is selected will be dropped.

It is possible to run commands as root, for such it is needed to have 
a ssh-askpass program installed. Once the ssh-askpass program is installed 
it is needed to make the export below.

Conidering your ssh-askpass program is placed in /usr/bin/:

    echo 'export SUDO_ASKPASS=/usr/bin/ssh-askpass' >> ~/.bashrc

After having set properly SUDO_ASKPASS variable, run commands as root using sudo like below:

    sudo some_command

The ssh-askpass program will ask for root password, type it then the command will be executed 
as root. Sometimes it is more useful to have a bash interpreter process running as root so
it is possible to run commands as root without having to retype password, for such, start
a bash process as shown below:

    sudo bash -i

Sometimes it is neeeded to restart the bash process, for such, press <Control-F1>. It is possible
to send a SIGINT by pressing <Control-c>, for sending a SIGQUIT, press <Control-backslash>.

There are times that it is useful to run interpreters through bash, some interpreters would run 
better if started with special arguments. It happens with the python interpreter for example:

    tee >(python -i -u)

Running the python interpreter using the command above would permit to neatly send and receive output.

Key-Commands
============

Mode: NORMAL
Event: <F1>
Description: Send the cursor line to the bash interpreter and place the cursor one line down.

Mode: INSERT
Event: <F1>
Description: Send the cursor line to the bash and insert a new line down the cursor position.

Mode: NORMAL
Event: <Control-c>
Description: Send a SIGINT signal to the bash interpreter.

Mode: NORMAL
Event: <Control-backslash>
Description: Send  SIGQUIT signal to the bash interpreter.

Mode: NORMAL
Event: <Control-F1>
Description: Restart the bash interpreter process.

Mode: NORMAL
Event: Return
Description: Send the cursor line to the bash interpreter.

Mode: NORMAL
Event: <Control-Return>
Description: Send the region of code that is selected to the bash interpreter.

Mode: NORMAL
Event: <Shift-F1>
Description: Send the current line and a Tab character to the bash interpreter,
asking for auto completion of the command.

Mode: NORMAL
Event: <Control-semicolon>
Description: Ask for the user to type a command to be dropped to the bash interpreter.
"""


from untwisted.network import core, xmap, READ, WRITE, Device
from untwisted.tkinter import extern
from untwisted.iofile import *
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





