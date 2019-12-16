"""
Overview
========

This module implements a wrapper around python debugger it is possible to easily debug python applications.
It is possible to set breakpoints, run code step by step, remove break points, check variable values etc.

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
        ('PYTHON', '<Key-1>', self.start_debug), 
        ('PYTHON', '<Key-2>', self.start_debug_args), 
        ('PYTHON', '<Key-m>', self.send_dcmd), 
        ('PYTHON', '<Key-Q>', self.quit_db), 
        ('PYTHON', '<Key-c>', self.send_continue), 
        ('PYTHON', '<Control-C>', self.dump_clear_all), 
        ('PYTHON', '<Control-c>', self.remove_breakpoint),
        ('PYTHON', '<Key-B>',  self.send_tbreak),
        ('PYTHON', '<Key-b>', self.send_break))

        self.python = python

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('Pdb Cmd: ', data)

    def send_break(self, event):
        self.send('break %s:%s\r\n' % (event.widget.filename, 
        event.widget.indref('insert')[0]))
        event.widget.chmode('NORMAL')

    def send_tbreak(self, event):
        self.send('tbreak %s:%s\r\n' % (event.widget.filename, 
        event.widget.indref('insert')[0]))
        event.widget.chmode('NORMAL')

    def send_continue(self, event):
        """
        """

        self.send('continue\r\n')

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

        xmap(device, 'LINE', self.handle_line)
        xmap(device, 'DELETED_BREAKPOINT', self.handle_deleted_breakpoint)
        xmap(device, 'BREAKPOINT', self.handle_breakpoint)

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

    def send_dcmd(self, event):
        ask  = Ask()

        if not ask.data: return
        self.send('%s\r\n' % ask.data)
        root.status.set_msg('Pdb: sent cmd!')

pdb     = Pdb()
install = pdb
