"""
Overview
========

This module implements a wrapper around python debugger it is possible to easily debug python applications.
It is possible to set breakpoints, run code step by step, remove break points, check variable values etc.

Usage
=====

First of all, it is needed to have a python program currently opened and having an output areavi instance. For such, open a python file
then create a horizontal/vertical areavi by pressing <F5> or <F4> in NORMAL mode. After having opened a horizontal/vertical areavi
instance then make it an output target by switching the focus to the horizontal/vertical areavi instance and press <Tab> in NORMAL mode.

Once having set an output target on an areavi instance then it is time to switch to PYTHON mode
by pressing <Key-exclam> in NORMAL mode. 

There are two ways to execute the program that was opened, the first one is without command line arguments, the second one
is with command line arguments. When in PYTHON mode and having one or more python files currently opened it is possible to start the debug process by
pressing <Key-1> with no command line arguments. When it is needed to pass arguments to the python application then it is used
the key-command <Key-2>. Once the debug process was started then output will go to the areavi instance that was set as target.

It is possible to set break points by placing the cursor over the desired line and pressing <Key-b> or <Key-N> for temporary
break points. In order to clear all break points, press <Control-C>, to remove a given break point, place the cursor
over the desired line then press <Control-c>. The line in which the break point was added is shaded.
Once break points were set then it is possible to send a '(c)ontinue' by pressing <Key-c>, '(s)tep' by pressing <Key-s>.
It is interesting to inspect the arguments that were passed to a function, for such, press <Key-a> that would send
an '(a)args' to the python debugger process.

Sometimes it is important to eval some expressions in the current frame, for such it is needed to select the text expression
then press <Key-p> that would send a '(p)rint', so the corresponding selected text will be evaluated in the currrent frame. 
The same occurs with statements that should be executed, select the text then press <Key-e> it would send a '!statement'.
It is useful to inject code through <Key-r> to be executed and <Key-x> to be evaluated .

Notice that when debugging a python application that does imports and if the import files are opened in vy
then when setting break points over multiple files would make vy set the focus to the tab whose file is being executed.


Key-Commands
============

Namespace: pdb

Mode: PYTHON
Event? <Key-1>
Description: It starts debugging the opened python application with no command line arguments.

Mode: PYTHON
Event: <Key-2>
Description: It starts the python application with command line arguments that use shlex module to split the arguments.

Mode: PYTHON
Event? <Key-c>
Description: Send a (c)ontinue to the debug process.
Continue execution, only stop when a breakpoint is encountered.

Mode: PYTHON
Event: <Key-e>
Description: Send selected text to the debug to be executed.

Mode: PYTHON
Event: <Key-w>
Description: Send a (w)here to the debug.
Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands.

Mode: PYTHON
Event: <Key-a>
Description: Send a (a)rgs to the debug to show the list of arguments passed to the current function.

Mode: PYTHON
Event: <Key-b>
Description: Set a break point at the cursor line.

Mode: PYTHON
Event: <Key-B>
Description: Set a temporary break point at the cursor line.

Mode: PYTHON
Event: <Control-C>
Description: Clear all break points.

Mode: PYTHON
Event: <Control-c>
Description: Remove break point that is set at the cursor line.

Mode: PYTHON
Event: <Control-s>
Description: Send a (s)tep to the debug it means execute the current line, stop at the first possible
occasion (either in a function that is called or on the next line in the current function).

Mode: PYTHON
Event: <Key-x>
Description: Inject python code to be evaluated in the current context.

Mode: PYTHON
Event: <Key-r>
Description: Inject python code to be executed in the current context.

Mode: PYTHON
Event: <Key-q>
Description: Terminate the process.

"""

from untwisted.network import core, READ, Device
from untwisted.tkinter import extern
from subprocess import Popen, PIPE, STDOUT
from untwisted.iofile import *
from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.plugins.pdb.event import PdbEvents
from vyapp.tools import set_line
from vyapp.ask import Ask
from vyapp.areavi import AreaVi
from vyapp.app import root
import shlex
import sys

class Pdb(object):
    setup={'background':'blue', 'foreground':'yellow'}
    encoding='utf8'

    def __call__(self, area, python='python2'):
        self.area = area
        area.add_mode('PYTHON')
        
        area.install('pdb', ('PYTHON', '<Key-p>', 
        lambda event: self.send('print %s' % event.widget.join_ranges(
        'sel', sep='\r\n'))), 
        ('PYTHON', '<Key-x>', lambda event: self.evaluate_expression()), 
        ('PYTHON', '<Key-r>', lambda event: self.execute_statement()), 
        ('PYTHON', '<Key-1>', lambda event: self.start_debug(event.widget)), 
        ('PYTHON', '<Key-2>', lambda event: self.start_debug_args(event.widget)), 
        ('PYTHON', '<Key-q>', lambda event: self.terminate_process()), 
        ('PYTHON', '<Key-c>', lambda event: self.send('continue\r\n')), 
        ('PYTHON', '<Key-e>', lambda event: self.send(
        '!%s' % event.widget.join_ranges('sel', sep='\r\n'))), 
        ('PYTHON', '<Key-w>', lambda event: self.send('where\r\n')), 
        ('PYTHON', '<Key-a>', lambda event: self.send('args\r\n')), 
        ('PYTHON', '<Key-s>', lambda event: self.send('step\r\n')), 
        ('PYTHON', '<Control-C>', lambda event: self.dump_clear_all()), 
        ('PYTHON', '<Control-c>', self.remove_breakpoint),
        ('PYTHON', '<Key-B>', lambda event: self.send(
        'tbreak %s:%s\r\n' % (event.widget.filename, 
        event.widget.indref('insert')[0]))),
        ('PYTHON', '<Key-b>', lambda event: self.send(
        'break %s:%s\r\n' % (event.widget.filename, 
        event.widget.indref('insert')[0]))))

        self.python = python

    def __init__(self):
        self.child = None
        self.map_index  = dict()
        self.map_line   = dict()

    def create_process(self, args):
        from os import environ, setsid
        self.child  = Popen(args, shell=0, stdout=PIPE, stdin=PIPE, preexec_fn=setsid, 
                            stderr=STDOUT,  env=environ)
    
        self.stdout = Device(self.child.stdout)
        self.stdin  = Device(self.child.stdin)
    
        Stdout(self.stdout)
        Terminator(self.stdout, delim=b'\n')
        Stdin(self.stdin)
        PdbEvents(self.stdout, self.encoding)

        xmap(self.stdout, LOAD, lambda con, data: sys.stdout.write(data))

        xmap(self.stdout, 'LINE', self.handle_line)
        xmap(self.stdout, 'DELETED_BREAKPOINT', self.handle_deleted_breakpoint)
        xmap(self.stdout, 'BREAKPOINT', self.handle_breakpoint)

        xmap(self.stdin, CLOSE, lambda dev, err: lose(dev))
        xmap(self.stdout, CLOSE, lambda dev, err: lose(dev))

    def kill_debug_process(self):
        try:
            self.child.kill()
        except AttributeError:
            return

    def terminate_process(self):
        self.kill_debug_process()
        self.delete_all_breakpoints()
        self.clear_breakpoint_map()
        root.status.set_msg('Debug finished !')

    def start_debug(self, area):
        self.kill_debug_process()
        self.delete_all_breakpoints()
        self.clear_breakpoint_map()
        self.create_process([self.python, '-u', 
        '-m', 'pdb', area.filename])

        root.status.set_msg('Debug started !')

    def start_debug_args(self, area):
        ask  = Ask()
        ARGS = '%s -u -m pdb %s %s' % (self.python, 
        area.filename, ask.data)

        ARGS = shlex.split(ARGS)
        self.kill_debug_process()
        self.delete_all_breakpoints()
        self.clear_breakpoint_map()

        self.create_process(ARGS)
        
        root.status.set_msg('Debug started ! Args: %s' % ask.data)

    def evaluate_expression(self):
        ask  = Ask()
        self.send('print %s\r\n' % ask.data)

    def execute_statement(self):
        ask  = Ask()
        self.send('!%s\r\n' % ask.data)

    def clear_breakpoint_map(self):
        self.map_index.clear()
        self.map_line.clear()

    def dump_clear_all(self):
        self.send('clear\r\nyes\r\n')
        self.delete_all_breakpoints()
        self.clear_breakpoint_map()

    def remove_breakpoint(self, event):
        self.send('clear %s\r\n' % self.map_line[(
        event.widget.filename, str(event.widget.indref('insert')[0]))])

    def delete_all_breakpoints(self):
        """
        It deletes all added breakpoint tags.
        It is useful when restarting pdb as a different process.
        """
    
        wids = AreaVi.get_opened_files(root)
        for index, (filename, line) in self.map_index.items():
            try:
                area = wids[filename]
            except KeyError:
                pass
            else:
                area.tag_delete(
                  '_breakpoint_%s' % index)        

    def handle_line(self, device, filename, line, args):
        """
    
        """

        wids = AreaVi.get_opened_files(root)
        try:
            area = wids[filename]
        except  KeyError:
            pass
        else:
            set_line(area, line)
    
    def handle_deleted_breakpoint(self, device, index):
        """
        When a break point is removed.
        """

        filename, line = self.map_index[index]
        NAME           = '_breakpoint_%s' % index
        area           = None

        try:
            area = AreaVi.get_opened_files(root)[filename]
        except KeyError:
            return

        area.tag_delete(NAME)

    def handle_breakpoint(self, device, index, filename, line):
        """
        When a break point is added.
        """

        self.map_index[index]           = (filename, line)
        self.map_line[(filename, line)] = index
        map                             = AreaVi.get_opened_files(root)

        area = map[filename]
        
        NAME = '_breakpoint_%s' % index
        area.tag_add(NAME, '%s.0 linestart' % line, 
                     '%s.0 lineend' % line)
    
        area.tag_config(NAME, **self.setup)

    def dump_sigint(self, area):
        from os import killpg
        killpg(child.pid, 2)


    def send(self, data):
        self.stdin.dump(data.encode(self.encoding))

pdb     = Pdb()
install = pdb


