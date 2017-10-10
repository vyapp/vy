"""
Overview
========

Find where patterns are found, this plugin uses ack to search
for word patterns. It is useful to find where functions/methods
are used over multiple files.

Key-Commands
============

Namespace: fstmt

Mode: NORMAL
Event: <Control-backslash>
Description: 

Mode: NORMAL
Event: <Key-backslash>
Description: 

Mode: NORMAL
Event: <Key-bar>
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
    def  __call__(self, options=[]):
        self.options = options

        self.listbox.delete(0, END)
        for filename, line, msg in options:
            self.listbox.insert(END, '%s - %s %s' % (
                relpath(filename), line, msg))

        self.show()

    def  __init__(self, options=[]):
        Toplevel.__init__(self, master=root)
        self.options = options
        self.title('Matches')

        self.listbox = Listbox(master=self)

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
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.transient(root)
        self.withdraw()

    def match(self):
        index = self.listbox.index(ACTIVE)
        item  = self.options[index]
        files = AreaVi.get_opened_files(root)

        try:
            area = files[item[0]]
        except KeyError:
            area = root.note.open(item[0])
        else:
            pass
        finally:
            set_line(area, item[1])
        self.close()

    def show(self):
        self.grab_set()
        self.deiconify()
        root.wait_window(self)
        # Could return the option here,
        # for reusability futurely.

    def close(self):
        # When calling destroy or withdraw without 
        # self.deoiconify it doesnt give back 
        # the focus to the parent window.

        self.deiconify()
        self.grab_release()
        self.withdraw()


class Fstmt(object):
    pattern = ''
    dir     = ''
    options = OptionWindow()

    def  __init__(self, area):
        self.area    = area

        area.install('fstmt', 
        ('NORMAL', '<Key-backslash>', 
        lambda event: self.find()),
        ('NORMAL', '<Key-bar>', 
        lambda event: self.set_dir()),
        ('NORMAL', '<Control-backslash>', 
        lambda event: self.catch_pattern()))

    def set_dir(self):
        ask       = Ask()
        Fstmt.dir = ask.data
   
    def catch_pattern(self):
        pattern = self.area.join_ranges('sel')
        pattern = pattern if pattern else self.area.get_word()
        Fstmt.pattern = pattern

        if not Fstmt.pattern:
            root.status.set_msg('No pattern found!')
        else:
            self.picker()

    def find(self):
        if Fstmt.pattern:
            self.options.show()
        else:
            root.status.set_msg('No pattern set!')

    def picker(self):
        dir = self.dir if Fstmt.dir else \
        get_sentinel_file(self.area.filename, '.git')

        child = Popen(['ack', '--nogroup', self.pattern, dir],
        stdout=PIPE, stderr=STDOUT, encoding=self.area.charset)
        output = child.communicate()[0]
        regex  = '(.+):([0-9]+):(.+)' 
        ranges = findall(regex, output)
    
        if ranges:
            self.options(ranges)

install = Fstmt






