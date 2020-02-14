"""
Overview
========

This module implements a minimal set of features to use Go Delve debugger in vy.
It implements key-commands to set breakpoints, remove breakpoints and also to send
Delve commands to be executed on the fly. 

The debugger writes output to sys.stdout which
can be redirected to multiple AreaVi instances thus allowing better
inspecting of what is happening in the debugged application.

Key-Commands
============

Namespace: delve

Mode: GOLANG
Event: <Key-1>
Description: It starts debugging the opened  application with no command line arguments.

Mode: GOLANG
Event: <Key-2>
Description: It starts the application with command line arguments that use shlex module to split the arguments.

Mode: GOLANG
Event: <Key-c>
Description: Send a (c)ontinue to the debug process.
Continue execution, only stop when a breakpoint is encountered.

Mode: GOLANG
Event: <Key-b>
Description: Set a break point at the cursor line.

Mode: GOLANG
Event: <Key-r>
Description: Restart the process.

Mode: GOLANG
Event: <Control-C>
Description: Clear all break points.

Mode: GOLANG
Event: <Control-c>
Description: Remove break point that is set at the cursor line.

Mode: GOLANG
Event: <Key-p>
Description: Evaluate selected text.

Mode: GOLANG
Event: <Key-m>
Description: Send a Delve command to be executed.

Mode: GOLANG
Event? <Key-x>
Description: Ask for expression to be sent/evaluated.

Mode: GOLANG
Event: <Key-Q>
Description: Terminate the process.

"""

from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.regutils import RegexEvent
from re import findall
from vyapp.dap import DAP
from vyapp.ask import Ask
from vyapp.app import root
import shlex

class Delve(DAP):
    def __call__(self, area):
        self.area = area
        
        area.install('delve', 
        ('GOLANG', '<Key-p>', self.evaluate_selection),
        ('GOLANG', '<Key-1>', self.run), 
        ('GOLANG', '<Key-r>', self.send_restart), 
        ('GOLANG', '<Key-x>', self.evaluate_expression), 
        ('GOLANG', '<Key-2>', self.run_args), 
        ('GOLANG', '<Key-Q>', self.quit_db), 
        ('GOLANG', '<Key-c>', self.send_continue), 
        ('GOLANG', '<Key-m>', self.send_dcmd), 
        ('GOLANG', '<Control-C>', self.dump_clear_all), 
        ('GOLANG', '<Control-c>', self.remove_breakpoint),
        ('GOLANG', '<Key-b>', self.send_break))

    def evaluate_expression(self, event):
        ask  = Ask()

        self.send("print %s\r\n" % ask.data)
        root.status.set_msg('(delve) Sent expression!')

    def send_restart(self, event):
        self.send('restart\r\n')
        root.status.set_msg('(delve) Sent restart!')

    def send_dcmd(self, event):
        ask  = Ask()
        self.send('%s\r\n' % ask.data)
        root.status.set_msg('(delve) Sent cmd!')

    def evaluate_selection(self, event):
        data = event.widget.join_ranges('sel', sep='\r\n')
        self.send('print %s' % data)
        event.widget.chmode('NORMAL')
        root.status.set_msg('(delve) Sent selection !')

    def install_handles(self, device):
        Terminator(device, delim=b'\n')

        regstr0 = '\> [^ ]* ?[^ ]+ ([^ ]+):([0-9]+).+'
        RegexEvent(device, regstr0, 'LINE', self.encoding)
        xmap(device, 'LINE', self.handle_line)

    def run(self, event):
        self.kill_process()

        self.create_process(['dlv', 'debug', event.widget.filename])
        root.status.set_msg('(delve) Started !')
        event.widget.chmode('NORMAL')

    def run_args(self, event):
        ask  = Ask()

        self.kill_process()

        self.create_process(shlex.split('dlv debug %s %s' % (
            event.widget.filename, ask.data)))
        
        root.status.set_msg('(delve) Started: %s' % ask.data)
        event.widget.chmode('NORMAL')

    def send_break(self, event):
        line, col = event.widget.indexref('insert')

        # Make sure the name will be unique for removing it later.
        bname = findall('[a-zA-Z]+', event.widget.filename)
        bname = '%s%s' % (''.join(bname), line)
        self.send('break %s %s:%s\r\n' % (bname, event.widget.filename, line))

        event.widget.chmode('NORMAL')
        root.status.set_msg('(delve) Sent breakpoint !')

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('Delve Cmd: ', data)

    def send_continue(self, event):
        """
        """

        self.send('continue\r\n')
        root.status.set_msg('(delve) Sent continue !')

    def dump_clear_all(self, event):
        self.send('clearall\r\n')

        event.widget.chmode('NORMAL')
        root.status.set_msg('(delve) Sent clearall !')

    def remove_breakpoint(self, event):
        """
        """

        line, col = event.widget.indexref('insert')
        bname = findall('[a-zA-Z]+', event.widget.filename)
        bname = '%s%s' % (''.join(bname), line)
        self.send('clear %s\r\n' % bname)

        event.widget.chmode('NORMAL')
        root.status.set_msg('(delve) Sent clear !')

delve   = Delve()
install = delve

