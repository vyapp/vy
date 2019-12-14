"""
Overview
========


Key-Commands
============

Namespace: delve

Mode: GOLANG
Event? <Key-1>
Description: 

Mode: GOLANG
Event: <Key-2>
Description: 

Mode: GOLANG
Event? <Key-c>
Description: 

Mode: GOLANG
Event: <Key-e>
Description: 

Mode: GOLANG
Event: <Key-w>
Description: 

Mode: GOLANG
Event: <Key-a>
Description: 

Mode: GOLANG
Event: <Key-b>
Description: 

Mode: GOLANG
Event: <Key-B>
Description: 

Mode: GOLANG
Event: <Control-C>
Description: 

Mode: GOLANG
Event: <Control-c>
Description: 

Mode: GOLANG
Event: <Control-s>
Description: 

Mode: GOLANG
Event: <Key-x>
Description: 

Mode: GOLANG
Event: <Key-r>
Description: 

Mode: GOLANG
Event: <Key-q>
Description: 

"""

from subprocess import Popen, PIPE, STDOUT
from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.wrappers import xmap
from untwisted.splits import Terminator
from vyapp.regutils import RegexEvent
from vyapp.ask import Ask
from vyapp.areavi import AreaVi
from vyapp.app import root
import shlex
import sys
import os

class Delve:
    setup={'background':'blue', 'foreground':'yellow'}
    encoding='utf8'

    def __call__(self, area):
        self.area = area
        
        area.install('delve', 
        ('GOLANG', '<Key-p>', self.send_print),
        ('GOLANG', '<Key-x>', self.evaluate_expression), 
        ('GOLANG', '<Key-1>', self.start_debug), 
        # ('GOLANG', '<Key-2>', self.start_debug_args), 
        ('GOLANG', '<Key-q>', self.quit_db), 
        ('GOLANG', '<Key-c>', self.send_continue), 
        ('GOLANG', '<Key-a>', self.send_args), 
        ('GOLANG', '<Key-s>', self.send_step), 
        ('GOLANG', '<Control-C>', self.dump_clear_all), 
        ('GOLANG', '<Control-c>', self.remove_breakpoint),
        ('GOLANG', '<Key-b>', self.send_break))

    def __init__(self):
        self.expect = None

    def create_process(self, args):
        self.expect = Expect(*args)

        xmap(self.expect, CLOSE, lambda expect: expect.destroy())
        self.install_handles(self.expect)
        root.protocol("WM_DELETE_WINDOW", self.on_quit)

    def on_quit(self):
        self.expect.terminate()
        print('Delve process killed!')
        root.destroy()

    def send_args(self, event):
        """
        """

        self.send('args\r\n')
        event.widget.chmode('NORMAL')
        root.status.set_msg('Delve: Sent args !')

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

        regstr0 = '\> [^ ]* ?[^ ]+ ([^ ]+):([0-9]+) .+'
        # regstr1 = '\(Pdb\) Deleted breakpoint ([0-9]+)'
        regstr1 = 'Breakpoint ([^ ]+) cleared at [^ ]+ for [^ ]+ (.+)\:([0-9]+)'

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

    def start_debug(self, event):
        if self.expect: self.expect.terminate()
        self.clear_breakpoints_map()

        self.create_process(['dlv', 'debug', event.widget.filename])
        root.status.set_msg('Delve debug started !')
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

    def send_step(self, event):
        """
        """

        self.send('step\r\n')
        root.status.set_msg('Step sent to Delve !')

    def clear_breakpoints_map(self):
        """
        """

        wids  = AreaVi.get_opened_files(root)
        for filename, area in wids.items():
            area.tag_delete('DELVE_BREAKPOINT')

    def dump_clear_all(self, event):
        self.send('clearall\r\n')
        self.clear_breakpoints_map()

        event.widget.chmode('NORMAL')
        root.status.set_msg('Delve cleared breakpoints!')

    def remove_breakpoint(self, event):
        """
        """

        line, col = event.widget.indref('insert')
        self.send('clear delvebreak%s\r\n' % line)
        event.widget.chmode('NORMAL')
        root.status.set_msg('Delve: Remove breakpoint sent!')

    def evaluate_expression(self, event):
        ask  = Ask()
        self.send('print %s\r\n' % ask.data)
        root.status.set_msg('Sent expression to Delve!')

    def handle_deleted_breakpoint(self, device, index, filename, line):
        """
        When a break point is removed.
        """
        filename = os.path.abspath(filename)
        widgets  = AreaVi.get_opened_files(root)
        area     = widgets.get(filename)

        if area: area.tag_remove('DELVE_BREAKPOINT', 
            '%s.0 linestart' % line, '%s.0 lineend' % line)

    def handle_line(self, device, filename, line):
        """
    
        """
        # Need to be factored off.
        filename = os.path.abspath(filename)

        wids = AreaVi.get_opened_files(root)
        area = wids.get(filename)

        if area: root.note.set_line(area, line)
    
    def handle_breakpoint(self, device, index, filename, line):
        """
        When a break point is added.
        """

        filename = os.path.abspath(filename)
        map  = AreaVi.get_opened_files(root)
        area = map[filename]

        area.tag_add('DELVE_BREAKPOINT', '%s.0 linestart' % line, '%s.0 lineend' % line)
        area.tag_config('DELVE_BREAKPOINT', **self.setup)

    def quit_db(self, event):
        self.clear_breakpoints_map()
        self.expect.terminate()

        root.status.set_msg('Delve stopped !')
        event.widget.chmode('NORMAL')

    def send(self, data):
        self.expect.send(data.encode(self.encoding))
        print('Dlv Cmd: ', data)

delve     = Delve()
install = delve

