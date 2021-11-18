"""
"""

from os.path import expanduser, join, exists, dirname
from vyapp.statusbar import StatusBar
from vyapp.notebook import NoteVi
from vyapp.plugins import ENV
from shutil import copyfile
from tkinter import Tk, Grid
from os import mkdir
import sys

class App(Tk):
    """
    This class implements the most basic vy editor widget. 
    It holds a NoteViwidget instance and a StatusBar widget instance.
    Plugins that demand accessing the NoteVi instance could use:

    from vyapp.app import root
    area = root.note.create('filename')

    Plugins that demand accessing the StatusBar instance could use.

    from vyapp.app import root
    root.status.set_msg('Message!')
    """

    def __init__(self, *args, **kwargs):
        """
        App class constructor. The arguments are passed
        to Tk class widget.
        """

        Tk.__init__(self, *args, **kwargs)
        self.note   = None
        self.status = None
        self.title('Vy')
        self.create_widgets()
        
    def create_vyrc(self):
        self.dir = join(expanduser('~'), '.vy')
        self.rc  = join(self.dir, 'vyrc')
        
        if not exists(self.dir):
            mkdir(self.dir)
        
        if not exists(self.rc):
            copyfile(join(dirname(__file__), 'vyrc'), self.rc)
        exec(compile(open(self.rc).read(), self.rc, 'exec'), ENV)

    def create_widgets(self):
        self.note = NoteVi(master=self, takefocus=0)
        self.note.grid(row=0, sticky='wens')

        self.status = StatusBar(master=self)
        self.status.grid(row=2, sticky='we')
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

