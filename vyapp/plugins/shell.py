"""
Overview
========

Used to spawn processes and send/receive data. It is useful to talk with extern processes like interpreters.

Usage
=====

Press <Control-F4> in NORMAL mode to open a vertical panel that will be used as output area.
It will show an entry text to type the name of the command/program then press enter after specifying
the sequence to run the process.

Once the process is running then use <F2> in NORMAL mode or INSERT mode to dump the cursor line
to the process. The process output will appear in the new AreaVi instance that was created.

Key-Commands
============

Mode: NORMAL
Event: <Control-F4>
Description: Instantiates an extern process.

Mode: NORMAL
Event: <F2>
Description: Send the cursor line to the process.

Mode: INSERT
Event: <F2>
Description: Send the cursor line to the process and insert a line down.
"""

from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.network import xmap
from vyapp.ask import Ask
from vyapp.tools import set_status_msg
from vyapp.exe import exec_quiet
from Tkinter import TclError
import shlex

class Pool(object):
    def __init__(self):
        self.base = []

    def create(self, *args, **kwargs):
        call = Expect(*args, **kwargs)
        self.base.append(call)
        return call

    def send(self, data):
        for ind in self.base:
            ind.send(data)

    def remove(self, call):
        self.base.remove(call)

class Command(object):
    def __init__(self, area):
        """

        """

        area.hook('NORMAL', '<Control-F4>', 
                        lambda event: self.start_process(event.widget))
        area.hook('NORMAL', '<F2>', lambda event: self.dump_line_and_down(event.widget))
        area.hook('INSERT', '<F2>', lambda event: self.dump_line_and_insert_line(event.widget))
        self.pool = Pool()

    def start_process(self, area):
        """

        """

        ask = Ask(area)
        if not ask.data: 
            return

        try:
            call = self.pool.create(*shlex.split(ask.data))
        except Exception as e:
            set_status_msg(e)
        else:
            self.create_output_area(area, call)

    def create_output_area(self, area, call):
        """

        """

        output = area.master.master.create()
    
        # When one of the AreaVi instances are destroyed then
        # the process is killed.
        output.hook(-1, '<Destroy>', lambda event: exec_quiet(call.terminate))
        area.hook(-1, '<Destroy>', lambda event: exec_quiet(call.terminate))

        # When call.terminnate is called it may happen of having still data to be
        # processed. It would attempt to write on an AreaVi instance that no more exist.
        # So, it executes quietly the AreaVi.append method.
        xmap(call, LOAD, lambda expect, data: exec_quiet(output.append, data))
        xmap(call, CLOSE, self.handle_close)

    def dump_line_and_down(self, area):
        self.pool.send(area.curline())
        area.down()

    def dump_line_and_insert_line(self, area):
        self.pool.send(area.curline())
        area.down()

    def handle_close(self, expect):
        set_status_msg('Killed process!')
        self.pool.remove(expect)
        expect.destroy()

install = Command







