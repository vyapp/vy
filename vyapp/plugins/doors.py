"""
Overview
========

Usage
=====


Key-Commands
============

"""

from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.usual import xmap
from vyapp.ask import Ask
from vyapp.tools import set_status_msg
from Tkinter import TclError
import shlex

class Command(object):
    def __init__(self, area):
        """

        """

        area.hook('NORMAL', '<Control-F4>', 
                        lambda event: self.start_process(event.widget))

    def start_process(self, area):
        """

        """

        ask = Ask(area)
        if not ask.data: 
            return
        try:
            call = Expect(*shlex.split(ask.data))
        except Exception as e:
            set_status_msg(e)
        else:
            self.create_output_area(area, call)

    def kill_process(self, call):
        """

        """
        # Kill the process regardless whether it is the
        # output area or not.
        try:
            call.destroy()
        except OSError:
            pass

        # The <Destroy> is spawned after the statusbar has been
        # destroyed.
        try:
            set_status_msg('Killed process!')
        except TclError:
            pass
    
    def create_output_area(self, area, call):
        """

        """

        output = area.master.master.create()
    
        # When one of the AreaVi instances are destroyed then
        # the process is killed.
        output.hook(-1, '<Destroy>', lambda event: self.kill_process(call))
        area.hook(-1, '<Destroy>', lambda event: self.kill_process(call))

        xmap(call, LOAD, lambda expect, data: self.handle_read(output, data))
        xmap(call, CLOSE, self.handle_close)

        area.hook('NORMAL', '<F9>', lambda event: self.dump_line(event.widget, call))

    def handle_close(self, expect):
        print 'closed'


    def dump_line(self, area, call):
        """

        """

        line = area.get('insert linestart', 'insert +1l linestart')
        call.send(line)

    def handle_read(self, area, data):
        """

        """
        area.insert('end', data)
        area.mark_set('insert', 'end')
        area.see('end')

install = Command




