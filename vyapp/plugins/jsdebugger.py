"""
Overview
========

This module implements basic functionalities of nodejs inspect debugger. It allows
one to sent debug commands and also settting and removing breakpoints with keystrokes.
When a given breakpoint is hit then the cursor is set accordingly.

Key-Commands
============

Namespace: jsdebugger

Mode: JAVASCRIPT
Event: <Key-1>
Description: It starts debugging the opened  application with no command line arguments.

Mode: JAVASCRIPT
Event: <Key-2>
Description: It starts the application with command line arguments that use shlex module to split the arguments.

Mode: JAVASCRIPT
Event: <Key-c>
Description: Send a (c)ontinue to the debug process.
Continue execution, only stop when a breakpoint is encountered.

Mode: JAVASCRIPT
Event: <Key-b>
Description: Set a break point at the cursor line.

Mode: JAVASCRIPT
Event: <Control-c>
Description: Remove break point that is set at the cursor line.

Mode: JAVASCRIPT
Event: <Key-p>
Description: Evaluate selected text.

Mode: JAVASCRIPT
Event: <Key-x>
Description: Ask for expression to be sent/evaluated.

Mode: JAVASCRIPT
Event: <Key-m>
Description: Send a JSDebugger command to be executed.

Mode: JAVASCRIPT
Event: <Key-r>
Description: Send restart command.

Mode: JAVASCRIPT
Event: <Key-Q>
Description: Terminate the process.

"""

from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.regutils import RegexEvent
from vyapp.dap import DAP
from vyapp.ask import Ask
from vyapp.app import root
import shlex

class JSDebugger(DAP):
    def __call__(self, area):
        self.area = area
        
        area.install('jsdebugger', 
        ('JAVASCRIPT', '<Key-p>', self.evaluate_selection),
        ('JAVASCRIPT', '<Key-r>', self.send_restart),
        ('JAVASCRIPT', '<Key-x>', self.send_exec),
        ('JAVASCRIPT', '<Key-1>', self.run), 
        ('JAVASCRIPT', '<Key-2>', self.run_args), 
        ('JAVASCRIPT', '<Key-Q>', self.quit_db), 
        ('JAVASCRIPT', '<Key-c>', self.send_continue), 
        ('JAVASCRIPT', '<Key-m>', self.send_dcmd), 
        ('JAVASCRIPT', '<Control-c>', self.remove_breakpoint),
        ('JAVASCRIPT', '<Key-b>', self.send_break))

    def send_restart(self, event):
        self.send('restart\r\n')
        root.status.set_msg('JSDebugger: sent restart!')

    def send_dcmd(self, event):
        ask  = Ask()
    
        self.send('%s\r\n' % ask.data)
        root.status.set_msg('JSDebugger: sent cmd!')

    def send_exec(self, event):
        ask  = Ask()

        self.send("exec('%s')\r\n" % ask.data)
        root.status.set_msg('JSDebugger: sent exec cmd!')

    def evaluate_selection(self, event):
        data = event.widget.join_ranges('sel')
        self.send("exec('%s')\r\n" % data)
        event.widget.chmode('NORMAL')
        root.status.set_msg('JSDebugger: Sent selection!')

    def install_handles(self, device):
        Terminator(device, delim=b'\n')

        regstr0 = 'break in (.+):([0-9]+)'
        RegexEvent(device, regstr0, 'LINE', self.encoding)
        xmap(device, 'LINE', self.handle_line)

        # Should be case insensitive.
        regstr1 = 'Break on .+ in (.+):([0-9]+)'
        RegexEvent(device, regstr1, 'LINE', self.encoding)
        xmap(device, 'LINE', self.handle_line)

    def run(self, event):
        self.kill_process()

        self.create_process(['node', 'inspect', event.widget.filename])
        root.status.set_msg('JSDebugger debug started !')
        event.widget.chmode('NORMAL')

    def run_args(self, event):
        ask  = Ask()

        self.kill_process()

        self.create_process(shlex.split('node inspect %s %s' % (
            event.widget.filename, ask.data)))
        
        root.status.set_msg('JSDebugger debug started: %s' % ask.data)
        event.widget.chmode('NORMAL')

    def send_break(self, event):
        line, col = event.widget.indexref('insert')
        self.send('sb("%s", %s)\r\n' % ( event.widget.filename, line))
        event.widget.chmode('NORMAL')

        root.status.set_msg('JSDebugger: Sent breakpoint !')

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('JSDebugger Cmd: ', data)

    def send_continue(self, event):
        """
        """

        self.send('cont\r\n')
        root.status.set_msg('Continue sent to JSDebugger !')

    def remove_breakpoint(self, event):
        """
        """

        line, col = event.widget.indexref('insert')
        self.send('cb("%s", %s)\r\n' % (event.widget.filename, line))
        event.widget.chmode('NORMAL')
        root.status.set_msg('JSDebugger: Remove breakpoint sent!')

install = JSDebugger()


