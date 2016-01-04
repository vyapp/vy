"""
Overview
========

This module implements PDB mode that is a mode where it is possible to easily debug python applications.
It is possible to set breakpoints, run code step by step, remove break points, check variable values etc.

Usage
=====

Key-Commands
============


""""""

"""
from untwisted.network import core, cmap, READ, Device
from untwisted.tkinter import extern
from subprocess import Popen, PIPE, STDOUT
from untwisted.utils.iofd import *
from untwisted.utils.shrug import *
from vyapp.plugins.pdb import event
from vyapp.tools import set_status_msg, set_line
from vyapp.ask import Ask
from vyapp.areavi import AreaVi
from vyapp.app import root
from os import environ, setsid, killpg
import shlex
import sys

class Pdb(object):
    def __call__(self, area, setup={'background':'blue', 'foreground':'yellow'}):
        area.add_mode('PDB')

        area.install(('BETA', '<Key-p>', lambda event: event.widget.chmode('PDB')),
                    ('PDB', '<Key-p>', lambda event: self.stdin.dump('print %s' % event.widget.tag_get_ranges('sel', sep='\r\n'))), 
                    ('PDB', '<Key-1>', lambda event: self.start_debug(event.widget)), 
                    ('PDB', '<Key-2>', lambda event: self.start_debug_args(event.widget)), 
                    ('PDB', '<Key-q>', lambda event: self.terminate_process()), 
                    ('PDB', '<Key-c>', lambda event: self.stdin.dump('continue\r\n')), 
                    ('PDB', '<Key-e>', lambda event: self.stdin.dump('!%s' % event.widget.tag_get_ranges('sel', sep='\r\n'))), 
                    ('PDB', '<Key-w>', lambda event: self.stdin.dump('where\r\n')), 
                    ('PDB', '<Key-a>', lambda event: self.stdin.dump('args\r\n')), 
                    ('PDB', '<Key-s>', lambda event: self.stdin.dump('step\r\n')), 
                    ('PDB', '<Control-C>', lambda event: self.dump_clear_all()), 
                    ('PDB', '<Control-c>', lambda event: self.stdin.dump('clear %s\r\n' % self.map_line[(event.widget.filename, str(event.widget.indref('insert')[0]))])),
                    ('PDB', '<Key-B>', lambda event: self.stdin.dump('tbreak %s:%s\r\n' % (event.widget.filename, event.widget.indref('insert')[0]))),
                    ('PDB', '<Key-b>', lambda event: self.stdin.dump('break %s:%s\r\n' % (event.widget.filename, event.widget.indref('insert')[0]))))

        self.setup = setup

    def __init__(self):
        self.child = None
        self.map_index  = dict()
        self.map_line   = dict()

    def create_process(self, args):
        self.child  = Popen(args, shell=0, stdout=PIPE, stdin=PIPE, preexec_fn=setsid, 
                            stderr=STDOUT,  env=environ)
    
        self.stdout = Device(self.child.stdout)
        self.stdin  = Device(self.child.stdin)
    
        Stdout(self.stdout)
        Shrug(self.stdout, delim='\n')
        Stdin(self.stdin)
        event.install(self.stdout)

        xmap(self.stdout, LOAD, lambda con, data: sys.stdout.write(data))

        xmap(self.stdout, 'LINE', self.handle_line)
        xmap(self.stdout, 'DELETED_BREAKPOINT', self.handle_deleted_breakpoint)
        xmap(self.stdout, 'BREAKPOINT', self.handle_breakpoint)

        xmap(self.stdin, CLOSE, lambda dev, err: lose(dev))
        xmap(self.stdout, CLOSE, lambda dev, err: lose(dev))

    def kill_debug_process(self):
        try:
            self.child.kill()
        except AttributeError:
            return

        self.delete_all_breakpoints()
        self.clear_breakpoint_map()

    def terminate_process(self):
        self.kill_debug_process()
        set_status_msg('Debug finished !')

    def start_debug(self, area):
        self.kill_debug_process()
        self.create_process(['python', '-u', '-m', 'pdb', area.filename])

        set_status_msg('Debug started !')

    def start_debug_args(self, area):
        ask  = Ask(area)
        ARGS = 'python -u -m pdb %s %s' % (area.filename, ask.data)
        ARGS = shlex.split(ARGS)

        self.kill_debug_process()
        self.create_process(ARGS)
        
        set_status_msg('Debug started ! Args: %s' % ask.data)

    def clear_breakpoint_map(self):
        self.map_index.clear()
        self.map_line.clear()

    def dump_clear_all(self):
        self.stdin.dump('clear\r\nyes\r\n')
        self.delete_all_breakpoints()
        self.clear_breakpoint_map()

    def delete_all_breakpoints(self):
        """
        It deletes all added breakpoint tags.
        It is useful when restarting pdb as a different process.
        """
    
        for index, (filename, line) in self.map_index.iteritems():
            try:
                area = AreaVi.get_opened_files(root)[filename]
            except KeyError:
                pass
            else:
                NAME = '_breakpoint_%s' % index
                area.tag_delete(NAME)        

    def handle_line(self, device, filename, line, args):
    
        """
    
        """
        try:
            area = AreaVi.get_opened_files(root)[filename]
        except  KeyError:
            pass
        else:
            set_line(area, line)
    
    def handle_deleted_breakpoint(self, device, index):
        """
        When a break point is removed.
        """

        filename, line = self.map_index[index]
        NAME           = '_breakpoint_%s' % index
        area           = None

        try:
            area = AreaVi.get_opened_files(root)[filename]
        except KeyError:
            return

        area.tag_delete(NAME)

    def handle_breakpoint(self, device, index, filename, line):
        """
        When a break point is added.
        """

        self.map_index[index]           = (filename, line)
        self.map_line[(filename, line)] = index
        map                             = get_opened_files()

        area = map[filename]
        
        NAME = '_breakpoint_%s' % index
        area.tag_add(NAME, '%s.0 linestart' % line, 
                     '%s.0 lineend' % line)
    
        area.tag_config(NAME, **self.setup)

    def dump_sigint(self, area):
        killpg(child.pid, 2)


pdb     = Pdb()
install = pdb










