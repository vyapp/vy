from vyapp.tools.misc import Transmitter
from Tkinter import *
from notebook import *
from statusbar import *
import sys

# It points to the root toplevel window of vy. It is the one whose AreaVi instances
# are placed on. 
root = None

# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
ENV  = dict()

# A special dict used to execute on the fly python code.
DEV  = dict()


class App(Tk):
    """

    """

    def __init__(self, max_tabs, *args, **kwargs):
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
        rc  = join(dir, '.vyrc')
        
        if not exists(dir):
            mkdir(dir)
        
        if not exists(rc):
            copyfile(join(dirname(__file__), 'vyrc'), rc)
        
        execfile(rc, ENV)

        self.note = NoteVi(max_tabs, master=self)
        self.note.pack(expand=True, fill=BOTH)
        self.status = StatusBar(self)
        self.status.pack(side=BOTTOM, fill=X)

# Just stdout is set. stderr remains original.
# So, some exceptions that are natural and occur along
# the application will not show up on text areas.
sys.stdout = Transmitter(sys.__stdout__)








