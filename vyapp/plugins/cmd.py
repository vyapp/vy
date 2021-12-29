"""
Overview
========


Key-Commands
============

"""

from traceback import print_exc as debug
from vyapp.plugins import Command
from vyapp.tools import e_stop
from vyapp.ask import Ask
from vyapp.plugins import ENV
from vyapp.app import root
import re
import sys

class Cmd:
    TAGCONF = {'background':'#313131'}

    def __init__(self, area):
        self.area = area

        area.tag_configure('(CODE)', **Cmd.TAGCONF)
        area.install('cmd',
        (-1, '<Alt-semicolon>',  self.exec_cmd),
        (-1, '<Alt-z>',  self.set_target),
        ('NORMAL', '<Key-semicolon>', self.exec_region),
        ('EXTRA', '<Key-x>', self.select_code),
        ('EXTRA', '<Key-X>', self.unselect_code))
        
    @e_stop
    def exec_cmd(self, event):
        ask = Ask()
        Command.set_target(self.area)
        print('\n(cmd) Executed code:\n>>> %s\n' % ask.data)
    
        data = ask.data.encode('utf-8')
        self.runcode(data, ENV)

    def select_code(self, event):
        range = self.area.tag_bounds('(CODE)', 'insert')
        index0 = self.area.index('sel.first')
        index1 = self.area.index('sel.last')

        self.area.clear_selection()
        self.area.tag_add('(CODE)', index0, index1)
        self.area.chmode('NORMAL')

    def unselect_code(self, event):
        range = self.area.tag_bounds('(CODE)', 'insert')
        if range is not None:
            self.area.tag_remove('(CODE)', *range)
        self.area.chmode('NORMAL')

    def runcode(self, data, env):
        """
        """

        # Avoid exception going to sys.stderr.
        tmp = sys.stderr
        sys.stderr = sys.stdout
    
        try:
            exec(data, env)
        except Exception as e:
            debug()
            root.status.set_msg('Error: %s' % e)
        finally:
            sys.stderr = tmp

    def exec_region(self, event):
        range = self.area.tag_bounds('(CODE)', 'insert')
        if range: 
            self.fmtexec(self.area.get(*range))

    def fmtexec(self, data):
        fmtdata = re.sub(r'^|\n', '\n>>> ', data)
        fmtdata = '(cmd) Executed code:\n%s\n' % fmtdata
        sys.stdout.write(fmtdata)
    
        data = data.encode('utf-8')
        self.runcode(data, ENV)
    
    def set_target(self, event):
        Command.set_target(self.area)

        root.status.set_msg('Set command target !')
        return 'break'
    
install = Cmd
