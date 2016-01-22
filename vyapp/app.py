"""
This module implements the App class widget widget which is one of the most important vy
editor's widgets.

This module exposes the vyapp.app.root attribute that is a variable pointing
to the App class instance. The App class instance holds all vy editor's widgets.
"""

from vyapp.stdout import Transmitter
from Tkinter import *
from vyapp.notevi import NoteVi
from vyapp.statusbar import *
from vyapp.plugins import ENV
import sys

# It points to the root toplevel window of vy. It is the one whose AreaVi instances
# are placed on. 
root = None

class App(Tk):
    """
    This class implements the most basic vy editor widget. It holds a NoteVi
    widget instance and a StatusBar widget instance. Plugins that demand
    accessing the NoteVi instance could use:

    from vyapp.app import root
    area = root.note.create('filename')

    Plugins that demand accessing the StatusBar instance could use.

    from vyapp.app import root
    root.status.set_msg('Message!')
    """

    def __init__(self, *args, **kwargs):
        """
        App class constructor. The arguments are passed to Tk class widget.
        """

        Tk.__init__(self, *args, **kwargs)
        self.title('Vy')

        global root
        root      = self

        from os.path import expanduser, join, exists, dirname
        from os import mkdir
        from shutil import copyfile
        
        dir = join(expanduser('~'), '.vy')
        rc  = join(dir, 'vyrc')
        
        if not exists(dir):
            mkdir(dir)
        
        if not exists(rc):
            copyfile(join(dirname(__file__), 'vyrc'), rc)
        
        execfile(rc, ENV)

        self.note = NoteVi(master=self)
        self.note.pack(expand=True, fill=BOTH)
        self.read_data = Frame()

        self.status = StatusBar(self)
        self.status.pack(side=BOTTOM, fill=X)

# Just stdout is set. stderr remains original.
# So, some exceptions that are natural and occur along
# the application will not show up on text areas.
sys.stdout = Transmitter(sys.__stdout__)

