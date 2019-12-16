"""
Overview
========


Key-Commands
============

Namespace: delve

Mode: GOLANG
Event? <Key-1>
Description: It starts debugging the opened  application with no command line arguments.

Mode: GOLANG
Event: <Key-2>
Description: It starts the application with command line arguments that use shlex module to split the arguments.

Mode: GOLANG
Event? <Key-c>
Description: Send a (c)ontinue to the debug process.
Continue execution, only stop when a breakpoint is encountered.

Mode: GOLANG
Event: <Key-b>
Description: Set a break point at the cursor line.

Mode: GOLANG
Event: <Control-C>
Description: Clear all break points.

Mode: GOLANG
Event: <Control-c>
Description: Remove break point that is set at the cursor line.

Mode: PYTHON
Event: <Key-p>
Description: Evaluate selected text.

Mode: PYTHON
Event: <Key-m>
Description: Send a Delve command to be executed.

Mode: GOLANG
Event: <Key-Q>
Description: Terminate the process.

"""

from subprocess import Popen, PIPE, STDOUT
from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.regutils import RegexEvent
from vyapp.mixins import DAP
from vyapp.ask import Ask
from vyapp.areavi import AreaVi
from vyapp.app import root
import shlex
import sys
import os

class Delve(DAP):
    setup={'background':'blue', 'foreground':'yellow'}
    encoding='utf8'

    def __call__(self, area):
        self.area = area
        
        area.install('delve', 
        ('GOLANG', '<Key-p>', self.send_print),
        ('GOLANG', '<Key-1>', self.start_debug), 
        ('GOLANG', '<Key-2>', self.start_debug_args), 
        ('GOLANG', '<Key-Q>', self.quit_db), 
        ('GOLANG', '<Key-c>', self.send_continue), 
        ('GOLANG', '<Key-m>', self.send_dcmd), 
        ('GOLANG', '<Control-C>', self.dump_clear_all), 
        ('GOLANG', '<Control-c>', self.remove_breakpoint),
        ('GOLANG', '<Key-b>', self.send_break))

    def __init__(self):
        super(Delve, self).__init__()
        self.expect = None

    def create_process(self, args):
        self.expect = Expect(*args)

        xmap(self.expect, CLOSE, self.on_close)
        self.install_handles(self.expect)
        root.protocol("WM_DELETE_WINDOW", self.on_quit)

    def send_dcmd(self, event):
        ask  = Ask()
        self.send('%s\r\n' % ask.data)
        root.status.set_msg('Delve: sent cmd!')

    def on_close(self, expect):
        self.expect.terminate()
        root.status.set_msg('Delve: CLOSED!')

    def on_quit(self):
        self.expect.terminate()
        print('Delve process killed!')
        root.destroy()

    def send_print(self, event):
        data = event.widget.join_ranges('sel', sep='\r\n')
        self.send('print %s' % data)
        event.widget.chmode('NORMAL')
        root.status.set_msg('Delve: Selected text evaluated !')

    def install_handles(self, device):
        Terminator(device, delim=b'\n')
        # Breakpoint 1 set at 0x4aa3b8 for main.feedSeq() ./problem-10.go:8
        # > main.feedSeq() ./problem-10.go:8 (hits goroutine(1):1 total:1) (PC: 0x4aa3b8)
        # > [ler5] main.feedSeq() ./problem-10.go:9 (hits goroutine(1):1 total:1) (PC: 0x4aa3e6)
        # Breakpoint delvebreak10 cleared at 0x4aa400 for main.feedSeq() ./.go/src/problem-10/problem-10.go:1

        regstr0 = '\> [^ ]* ?[^ ]+ ([^ ]+):([0-9]+).+'
        regstr1 = 'Breakpoint ([^ ]+) cleared at [^ ]+ for [^ ]+ .+\:[0-9]+'
        regstr2 = 'Breakpoint ([a-zA-Z0-9]+) set at [^ ]+ for [^ ]+ (.+)\:([0-9]+)'

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

    def kill_process(self):
        if self.expect:
            self.expect.terminate()
        self.clear_breakpoints_map()

    def start_debug(self, event):
        self.kill_process()

        self.create_process(['dlv', 'debug', event.widget.filename])
        root.status.set_msg('Delve debug started !')
        event.widget.chmode('NORMAL')

    def start_debug_args(self, event):
        ask  = Ask()

        if not ask.data: return
        self.kill_process()

        self.create_process(shlex.split('dlv debug %s %s' % (
            event.widget.filename, ask.data)))
        
        root.status.set_msg('Delve debug started: %s' % ask.data)
        event.widget.chmode('NORMAL')

    def send_break(self, event):
        line, col = event.widget.indref('insert')
        self.send('break %s %s:%s\r\n' % ('delvebreak%s' % line, 
        event.widget.filename, line))
        event.widget.chmode('NORMAL')

        root.status.set_msg('Delve: Sent breakpoint !')

    def send_continue(self, event):
        """
        """

        self.send('continue\r\n')
        root.status.set_msg('Continue sent to Delve !')

    def dump_clear_all(self, event):
        self.send('clearall\r\n')
        # self.clear_breakpoints_map()

        event.widget.chmode('NORMAL')
        root.status.set_msg('Delve cleared breakpoints!')

    def remove_breakpoint(self, event):
        """
        """

        name = self.get_breakpoint_name(event.widget.filename, 
        str(event.widget.indref('insert')[0]))

        self.send('clear %s\r\n' % name)
        event.widget.chmode('NORMAL')
        root.status.set_msg('Delve: Remove breakpoint sent!')

    def quit_db(self, event):
        self.kill_process()
        event.widget.chmode('NORMAL')
        root.status.set_msg('Quitting Delve!')

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('Dlv Cmd: ', data)

delve     = Delve()
install = delve

