"""
Overview
========

Key-Commands
============

Namespace: fstmt

Mode: NORMAL
Event: 
Description: 

"""

from subprocess import Popen, STDOUT, PIPE
from os.path import exists, dirname, join, relpath
from tkinter import Toplevel, Listbox, BOTH, END, TOP, ACTIVE
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.tools import set_line
from vyapp.app import root
from vyapp.ask import Ask
from re import findall
import sys

def get_sentinel_file(path, filename):
    """
    """

    tmp = path
    while True:
        tmp = dirname(tmp)
        if exists(join(tmp, filename)):
            return tmp
        elif tmp == dirname(tmp):
            return path
        path = tmp

class OptionWindow(Toplevel):
    def  __init__(self, area, options):
        Toplevel.__init__(self, master=root)
        self.area    = area
        self.options = options
        self.title('Matches')

        self.listbox = Listbox(master=self)

        for filename, line, msg in options:
            self.listbox.insert(END, '%s - %s %s' % (
                relpath(filename), line, msg))

        self.listbox.pack(expand=True, fill=BOTH, side=TOP)
        self.listbox.focus_set()
        self.listbox.activate(0)
        self.listbox.selection_set(0)

        self.listbox.config(width=50)

        self.listbox.bind('<Key-h>', lambda event:
        self.listbox.event_generate('<Left>'))

        self.listbox.bind('<Key-l>', lambda event:
        self.listbox.event_generate('<Right>'))

        self.listbox.bind('<Key-k>', lambda event:
        self.listbox.event_generate('<Up>'))

        self.listbox.bind('<Key-j>', lambda event:
        self.listbox.event_generate('<Down>'))

        self.listbox.bind('<Escape>', lambda event: self.close())
        self.listbox.bind('<Return>', lambda event: self.match())

        self.transient(root)
        self.grab_set()
        self.wait_window(self)

    def match(self):
        index = self.listbox.index(ACTIVE)
        item  = self.options[index]
        files = self.area.get_opened_files(root)

        try:
            area = files[item[0]]
        except KeyError:
            area = root.note.open(item[0])
        else:
            pass
        finally:
            set_line(area, item[1])
        self.close()

    def close(self):
        self.grab_release()
        # When calling destroy without 
        # self.deoiconify it doesnt give back 
        # the focus to the parent window.
        self.deiconify()
        self.destroy()


class Fstmt(object):
    def  __init__(self, area):
        area.install('fstmt', 
        ('NORMAL', '<Key-backslash>', lambda event: self.picker()),
        ('NORMAL', '<Key-bar>', lambda event: self.set_search_path()))
        self.area = area
        self.search_path = ''

    def set_search_path(self):
        ask              = Ask()
        self.search_path = ask.data
   
    def picker(self):
        pattern = self.area.join_ranges('sel')

        if not pattern: return

        search_path = self.search_path if self.search_path else \
        get_sentinel_file(self.area.filename, '.git')

        child = Popen(['ack', '--nogroup', pattern, search_path],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]
        regex  = '(.+):([0-9]+):(.+)' 
        ranges = findall(regex, output)

        if ranges:
            OptionWindow(self.area, ranges)

install = Fstmt




