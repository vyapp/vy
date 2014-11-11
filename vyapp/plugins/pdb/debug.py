"""

"""
from untwisted.network import core, cmap, READ, Device
from untwisted.tkinter import extern
from subprocess import Popen, PIPE, STDOUT
from untwisted.utils.iofd import *
from untwisted.utils.shrug import *
from vyapp.plugins.pdb import event
from vyapp.tools.misc import set_status_msg
from vyapp.tools.misc import get_opened_files, set_line, get_all_areavi_instances

import sys
from os import environ, setsid, killpg


class Pdb(object):
    def __call__(self, area, setup={'background':'blue', 'foreground':'yellow'}):

        INSTALL = ((3, '<Key-p>', lambda event: self.stdin.dump('print %s' % event.widget.tag_get_ranges('sel', sep='\r\n'))), 
                   (3, '<Key-1>', lambda event: self.start_debug(event.widget)), 
                   (3, '<Key-c>', lambda event: self.stdin.dump('continue\r\n')), 
                   (3, '<Key-e>', lambda event: self.stdin.dump('!%s' % event.widget.tag_get_ranges('sel', sep='\r\n'))), 
                   (3, '<Key-w>', lambda event: self.stdin.dump('where\r\n')), 
                   (3, '<Key-a>', lambda event: self.stdin.dump('args\r\n')), 
                   (3, '<Key-s>', lambda event: self.stdin.dump('step\r\n')), 
                   (3, '<Control-c>', lambda event: self.stdin.dump('clear %s:%s\r\n' % (event.widget.filename, event.widget.indref('insert')[0]))),
                   (3, '<Key-B>', lambda event: self.stdin.dump('tbreak %s:%s\r\n' % (event.widget.filename, event.widget.indref('insert')[0]))),
                   (3, '<Key-b>', lambda event: self.stdin.dump('break %s:%s\r\n' % (event.widget.filename, event.widget.indref('insert')[0]))))

        area.install(*INSTALL)
        self.setup = setup

    def __init__(self):
        self.child = None
        
    def start_debug(self, area):
        self.child  = Popen(['python', '-u', '-m', 'pdb',  area.filename], shell=0, 
                            stdout=PIPE, stdin=PIPE, preexec_fn=setsid, 
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

        set_status_msg('Debug process started !')
    
    def dump_sigint(self, area):
        killpg(child.pid, 2)
    
    def handle_line(self, device, filename, line, args):
    
        """
    
        """
        try:
            area = get_opened_files()[filename]
        except  KeyError:
            pass
        else:
            set_line(area, line)
    
    def handle_deleted_breakpoint(self, device, index):
        """

        """

        name = '_breakpoint_%s' % index

        for ind in get_all_areavi_instances():
            map = ind.tag_ranges(name)
            if not map: 
                continue

            ind.tag_delete(name)
            break

    def handle_breakpoint(self, device, index, filename, line):
        """

        """

        map  = get_opened_files()
        area = map[filename]
    
        name = '_breakpoint_%s' % index
        area.tag_add(name, '%s.0 linestart' % line, 
                     '%s.0 lineend' % line)
    
        area.tag_config(name, **self.setup)



pdb     = Pdb()
install = pdb











