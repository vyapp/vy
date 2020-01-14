"""
Overview
========

This module implements a wrapper around python debugger it is possible 
to easily debug python applications. It is possible to set breakpoints, run 
code step by step, remove break points, check variable values etc.

Key-Commands
============

Namespace: pdb

Mode: PYTHON
Event: <Key-1>
Description: It starts debugging the opened python application with 
no command line arguments.

Mode: PYTHON
Event: <Key-2>
Description: It starts the python application with command line arguments 
that use shlex module to split the arguments.

Mode: PYTHON
Event: <Key-x>
Description: Ask for expression to be sent/evaluated.

Mode: PYTHON
Event: <Key-c>
Description: Send a (c)ontinue to the debug process.
Continue execution, only stop when a breakpoint is encountered.

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
Event: <Key-p>
Description: Evaluate selected text.

Mode: PYTHON
Event: <Key-m>
Description: Send a PDB command to be executed.

Mode: PYTHON
Event: <Key-r>
Description: Send restart.

Mode: PYTHON
Event: <Key-Q>
Description: Terminate the process.

"""
from vyapp.regutils import RegexEvent
from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.ask import Ask
from vyapp.dap import DAP
from vyapp.app import root
import shlex

class Pdb(DAP):
    def __call__(self, area, python='python2'):
        self.area = area
        
        area.install('pdb', 
        ('PYTHON', '<Key-p>', self.evaluate_selection),
        ('PYTHON', '<Key-x>', self.evaluate_expression),
        ('PYTHON', '<Key-1>', self.run), 
        ('PYTHON', '<Key-2>', self.run_args), 
        ('PYTHON', '<Key-r>', self.send_restart), 
        ('PYTHON', '<Key-m>', self.send_dcmd), 
        ('PYTHON', '<Key-Q>', self.quit_db), 
        ('PYTHON', '<Key-c>', self.send_continue), 
        ('PYTHON', '<Control-C>', self.dump_clear_all), 
        ('PYTHON', '<Control-c>', self.remove_breakpoint),
        ('PYTHON', '<Key-B>',  self.send_tbreak),
        ('PYTHON', '<Key-b>', self.send_break))

        self.python = python

    def evaluate_expression(self, event):
        ask  = Ask()

        self.send("p %s\r\n" % ask.data)
        root.status.set_msg('(pdb) Sent expression!')

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('Pdb Cmd: ', data)

    def send_break(self, event):
        self.send('break %s:%s\r\n' % (event.widget.filename, 
        event.widget.indexref('insert')[0]))
        event.widget.chmode('NORMAL')
        root.status.set_msg('(pdb) Command break sent !')

    def send_tbreak(self, event):
        self.send('tbreak %s:%s\r\n' % (event.widget.filename, 
        event.widget.indexref('insert')[0]))
        event.widget.chmode('NORMAL')
        root.status.set_msg('(pdb) Command tbreak sent !')

    def send_continue(self, event):
        """
        """

        self.send('continue\r\n')
        root.status.set_msg('(pdb) Command continue sent !')

    def send_restart(self, event):
        """
        """

        self.send('restart\r\n')
        root.status.set_msg('(pdb) Sent restart !')

    def evaluate_selection(self, event):
        data = event.widget.join_ranges('sel', sep='\r\n')
        self.send('p %s' % data)
        event.widget.chmode('NORMAL')
        root.status.set_msg('(pdb) Sent text selection!')

    def install_handles(self, device):
        Terminator(device, delim=b'\n')

        regstr0 = '\> (.+)\(([0-9]+)\).+'

        RegexEvent(device, regstr0, 'LINE', self.encoding)
        xmap(device, 'LINE', self.handle_line)

    def run(self, event):
        self.kill_process()
        self.create_process([self.python, '-u', 
        '-m', 'pdb', event.widget.filename])

        root.status.set_msg('(pdb) Started !')
        event.widget.chmode('NORMAL')

    def run_args(self, event):
        ask  = Ask()
        ARGS = '%s -u -m pdb %s %s' % (self.python, 
        event.widget.filename, ask.data)
        self.kill_process()

        ARGS = shlex.split(ARGS)
        self.create_process(ARGS)
        
        root.status.set_msg('(pdb) Started with Args: %s' % ask.data)
        event.widget.chmode('NORMAL')

    def dump_clear_all(self, event):
        self.send('clear\r\nyes\r\n')
        event.widget.chmode('NORMAL')
        root.status.set_msg('(pdb) Command clearall sent!')

    def remove_breakpoint(self, event):
        """
        """
        line, col = event.widget.indexref('insert')
        self.send('clear %s:%s\r\n' % (event.widget.filename, line))
        event.widget.chmode('NORMAL')
        root.status.set_msg('(pdb) Command clear sent!')

    def send_dcmd(self, event):
        ask  = Ask()

        self.send('%s\r\n' % ask.data)
        root.status.set_msg('(pdb) Sent cmd!')

pdb     = Pdb()
install = pdb
