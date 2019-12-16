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
Event: <Key-s>
Description: Send a (s)tep to the debug it means execute the current line, stop at the first possible
occasion (either in a function that is called or on the next line in the current function).

Mode: PYTHON
Event: <Key-x>
Description: Inject python code to be evaluated in the current context.

Mode: PYTHON
Event: <Key-r>
Description: Inject python code to be executed in the current context.

Mode: PYTHON
Event: <Key-Q>
Description: Terminate the process.

"""
from untwisted.expect import Expect, LOAD, CLOSE
from vyapp.regutils import RegexEvent
from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.ask import Ask
from vyapp.mixins import DAP
from vyapp.areavi import AreaVi
from vyapp.app import root
import shlex
import sys

class Pdb(DAP):
    def __call__(self, area, python='python2'):
        self.area = area
        
        area.install('pdb', 
        ('PYTHON', '<Key-p>', self.send_print),
        ('PYTHON', '<Key-x>', self.evaluate_expression), 
        ('PYTHON', '<Key-r>', self.execute_statement), 
        ('PYTHON', '<Key-1>', self.start_debug), 
        ('PYTHON', '<Key-2>', self.start_debug_args), 
        ('PYTHON', '<Key-m>', self.send_dcmd), 
        ('PYTHON', '<Key-Q>', self.quit_db), 
        ('PYTHON', '<Key-c>', self.send_continue), 
        ('PYTHON', '<Key-w>', self.send_where), 
        ('PYTHON', '<Key-a>', self.send_args), 
        ('PYTHON', '<Key-s>', self.send_step), 
        ('PYTHON', '<Control-C>', self.dump_clear_all), 
        ('PYTHON', '<Control-c>', self.remove_breakpoint),
        ('PYTHON', '<Key-B>',  self.send_tbreak),
        ('PYTHON', '<Key-b>', self.send_break))

        self.python = python

    def __init__(self):
        super(Pdb, self).__init__()
        self.expect  = None

    def on_close(self, expect):
        self.expect.terminate()
        root.status.set_msg('PDB: CLOSED!')

    def send_break(self, event):
        self.send('break %s:%s\r\n' % (event.widget.filename, 
        event.widget.indref('insert')[0]))
        event.widget.chmode('NORMAL')

    def send_tbreak(self, event):
        self.send('tbreak %s:%s\r\n' % (event.widget.filename, 
        event.widget.indref('insert')[0]))
        event.widget.chmode('NORMAL')

    def send_step(self, event):
        """
        """

        self.send('step\r\n')

    def send_args(self, event):
        self.send('args\r\n')
        event.widget.chmode('NORMAL')

    def send_where(self, event):
        """
        """

        self.send('where\r\n')
        event.widget.chmode('NORMAL')
        
    def send_continue(self, event):
        """
        """

        self.send('continue\r\n')
        # event.widget.chmode('NORMAL')

    def send_print(self, event):
        data = event.widget.join_ranges('sel', sep='\r\n')
        self.send('print %s' % data)
        event.widget.chmode('NORMAL')

    def install_handles(self, device):
        Terminator(device, delim=b'\n')

        regstr0 = '\> (.+)\(([0-9]+)\).+'
        regstr1 = 'Deleted breakpoint ([0-9]+)'
        regstr2 = 'Breakpoint ([0-9]+) at (.+)\:([0-9]+)'

        RegexEvent(device, regstr0, 'LINE', self.encoding)
        RegexEvent(device, regstr1, 'DELETED_BREAKPOINT', self.encoding)
        RegexEvent(device, regstr2, 'BREAKPOINT', self.encoding)

        # Note: The data has to be decoded using the area charset
        # because the area contents would be sometimes printed along
        # the debugging.
        xmap(device, LOAD, lambda con, 
        data: sys.stdout.write(data.decode(self.area.charset)))

        xmap(device, 'LINE', self.handle_line)
        xmap(device, 'DELETED_BREAKPOINT', self.handle_deleted_breakpoint)
        xmap(device, 'BREAKPOINT', self.handle_breakpoint)

    def create_process(self, args):
        self.expect = Expect(*args)
        xmap(self.expect, CLOSE, self.on_close)
        self.install_handles(self.expect)

        root.protocol("WM_DELETE_WINDOW", self.on_quit)

    def on_quit(self):
        self.expect.terminate()
        print('PDB process killed!')
        root.destroy()

    def kill_process(self):
        if self.expect:
            self.expect.terminate()
        self.clear_breakpoints_map()

    def quit_db(self, event):
        self.kill_process()
        event.widget.chmode('NORMAL')

    def start_debug(self, event):
        self.kill_process()
        self.create_process([self.python, '-u', 
        '-m', 'pdb', event.widget.filename])

        root.status.set_msg('Debug started !')
        event.widget.chmode('NORMAL')

    def start_debug_args(self, event):
        ask  = Ask()
        ARGS = '%s -u -m pdb %s %s' % (self.python, 
        event.widget.filename, ask.data)
        self.kill_process()

        ARGS = shlex.split(ARGS)
        self.create_process(ARGS)
        
        root.status.set_msg('Debug started ! Args: %s' % ask.data)
        event.widget.chmode('NORMAL')

    def evaluate_expression(self, event):
        ask  = Ask()
        self.send('print(%s)\r\n' % ask.data)

    def execute_statement(self, event):
        ask  = Ask()
        self.send('!%s\r\n' % ask.data)

    def dump_clear_all(self, event):
        self.send('clear\r\nyes\r\n')
        # self.clear_breakpoints_map()
        event.widget.chmode('NORMAL')

    def remove_breakpoint(self, event):
        """
        """

        name = self.get_breakpoint_name(event.widget.filename, 
        str(event.widget.indref('insert')[0]))

        self.send('clear %s\r\n' % name)
        event.widget.chmode('NORMAL')
        root.status.set_msg('PDB: Remove breakpoint sent!')

    def dump_sigint(self, area):
        from os import killpg
        killpg(child.pid, 2)

    def send(self, data):
        self.expect.send(data.encode(self.encoding))

    def send_dcmd(self, event):
        ask  = Ask()

        if not ask.data: return
        self.send('%s\r\n' % ask.data)
        root.status.set_msg('Pdb: sent cmd!')

pdb     = Pdb()
install = pdb
