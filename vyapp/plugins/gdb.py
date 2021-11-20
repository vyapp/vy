"""
Overview
========

This module provides functionalities to work with GDB. It allows
watching the flow of the application being debugged, setting breakpoints, 
removing breakpoints with keystrokes.

Key-Commands
============

Namespace: GDB

Mode: C
Event: <Key-R>
Description: Ask for a compiled file to be debugged. It is necessary to have it compiled with -g flag.
Example:

    gcc -g filename.c -o filename.out

Mode: C
Event: <Key-c>
Description: Send a (c)ontinue to the debug process.
Continue execution, only stop when a breakpoint is encountered.

Mode: C
Event: <Key-b>
Description: Set a break point at the cursor line.

Mode: C
Event: <Key-r>
Description: Send a run to start/restart from the beginning.
For running with arguments just use:

    <Key-x>

Then:
    
    run arg0 arg1 ...

Mode: C
Event: <Control-c>
Description: Remove break point that is set at the cursor line.

Mode: C
Event: <Key-p>
Description: Evaluate selected text.

Mode: C
Event: <Key-m>
Description: Send a GDB command to be executed.

Mode: C
Event? <Key-x>
Description: Ask for expression to be sent/evaluated.

Mode: C
Event: <Key-Q>
Description: Terminate the process.

"""

from tkinter.filedialog import askopenfilename
from untwisted.splits import Terminator
from vyapp.regutils import RegexEvent
from vyapp.dap import DAP
from vyapp.ask import Ask
from vyapp.app import root
import shlex

class GDB(DAP):
    def __call__(self, area):
        self.area = area
        
        area.install('GDB', 
        ('C', '<Key-p>', self.evaluate_selection),
        ('C', '<Key-R>', self.ask_gdb_exec), 
        ('C', '<Key-r>', self.run), 
        ('C', '<Key-x>', self.evaluate_expression), 
        ('C', '<Key-Q>', self.quit_db), 
        ('C', '<Key-c>', self.send_continue), 
        ('C', '<Key-m>', self.send_dcmd), 
        ('C', '<Key-s>',  self.send_step),
        ('C', '<Key-S>',  self.set_auto_open),
        ('C', '<Control-c>', self.clear_breakpoint),
        ('C', '<Key-b>', self.send_break))

    def __init__(self):
        self.expect  = None
        self.auto_open = False

    def send_step(self, event):
        self.send('step\r\n')
        root.status.set_msg('(GDB) Command step sent !')

    def set_auto_open(self, event):
        self.auto_open = False if self.auto_open else True
        root.status.set_msg('(GDB) Auto open files: %s!' % self.auto_open)

    def evaluate_expression(self, event):
        ask  = Ask()

        self.send("print %s\r\n" % ask.data)
        root.status.set_msg('(GDB) Sent expression!')

    def run(self, event):
        self.send('run\r\n')
        root.status.set_msg('(GDB) Sent run!')

    def send_dcmd(self, event):
        ask  = Ask()
        self.send('%s\r\n' % ask.data)
        root.status.set_msg('(GDB) Sent cmd!')

    def evaluate_selection(self, event):
        data = event.widget.tag_xjoin('sel', sep='\r\n')
        self.send('print %s' % data)
        event.widget.chmode('NORMAL')
        root.status.set_msg('(GDB) Sent selection !')

    def install_handles(self, expect):
        Terminator(expect, delim=b'\n')

        regstr0 = '\032\032(.+):([0-9]+):[0-9]+:.+:.+'
        RegexEvent(expect, regstr0, 'LINE', self.encoding)
        expect.add_map('LINE', self.handle_line)

    def ask_gdb_exec(self, event):
        root.status.set_msg('(GDB) Select a compiled file:')
        filename = askopenfilename()
        if filename: 
            self.init_gdb(filename)
        event.widget.chmode('NORMAL')

    def init_gdb(self, filename):
        self.kill_process()
        self.create_process(shlex.split('gdb -f %s' % filename))
        root.status.set_msg('(GDB) Started: %s' % filename)

    def send_break(self, event):
        line, col = event.widget.indexsplit('insert')

        # Make sure the name will be unique for removing it later.
        self.send('break %s:%s\r\n' % (event.widget.filename, line))

        event.widget.chmode('NORMAL')
        root.status.set_msg('(GDB) Sent breakpoint !')

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('GDB Cmd: ', data)

    def send_continue(self, event):
        """
        """

        self.send('continue\r\n')
        root.status.set_msg('(GDB) Sent continue !')

    def clear_breakpoint(self, event):
        """
        """

        line, col = event.widget.indexsplit('insert')
        self.send('clear %s:%s\r\n' % (event.widget.filename, line))

        event.widget.chmode('NORMAL')
        root.status.set_msg('(GDB) Sent clear !')

    def quit_db(self, event):
        self.kill_process()
        event.widget.chmode('NORMAL')
        sys.stdout.write('(GDB) Sent quit!')

GDB   = GDB()
install = GDB
