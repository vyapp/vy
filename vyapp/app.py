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

    """

    def __init__(self, *args, **kwargs):
        """

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
        self.status = StatusBar(self)
        self.status.pack(side=BOTTOM, fill=X)

# Just stdout is set. stderr remains original.
# So, some exceptions that are natural and occur along
# the application will not show up on text areas.
sys.stdout = Transmitter(sys.__stdout__)














