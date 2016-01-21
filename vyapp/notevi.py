"""

"""

from Tkinter import *
from areavi import AreaVi
from ttk import Notebook

class PanedHorizontalWindow(PanedWindow):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        """

        PanedWindow.__init__(self, orient=HORIZONTAL, *args, **kwargs)

    def create_area(self, filename='none'):
        """

        """

        frame     = Frame(master=self)
        scrollbar = Scrollbar(master=frame)
        area      = AreaVi(filename, frame , border=3, relief=RAISED, 
                           yscrollcommand=scrollbar.set)
        scrollbar.config(command=area.yview)
        scrollbar.pack(side='right', fill=Y)

        from vyapp.plugins import INSTALL, HANDLE

        for plugin, args, kwargs in INSTALL:
            plugin.install(area, *args, **kwargs)

        for handle, args, kwargs in HANDLE:
            handle(area, *args, **kwargs)

        area.pack(expand=True, side='left', fill=BOTH)
        area.focus_set()

        self.add(frame)

        return area

    def create(self, filename='none'):
        """

        """

        area = self.create_area(filename)
        self.add(area.master)
        return area

    def load(self, filename):
        """

        """

        area = self.create_area()
        self.add(area.master)
        area.load_data(filename)
        return area

class PanedVerticalWindow(PanedWindow):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        """

        PanedWindow.__init__(self, orient=VERTICAL, *args, **kwargs)

    def create(self, filename='none'):
        """

        """

        base = PanedHorizontalWindow(master=self)
        self.add(base)
        area = base.create(filename)
        return area

    def load(self, *args):
        """

        """

        base = PanedHorizontalWindow(master=self)
        self.add(base)

        for ind in args:
            base.load(ind)
        return base

class NoteVi(Notebook):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        """

        Notebook.__init__(self, *args, **kwargs)

    def create(self, filename):
        """

        """

        base = PanedVerticalWindow(master=self)
        area = base.create(filename)
        self.add(base, text=filename)
        return area

    def load(self, *args):
        """

        """

        for indi in args:
            base = PanedVerticalWindow(master=self)
            base.pack(side='left', expand=True, fill=BOTH)
            self.add(base)        
            for indj in indi:
                base.load(*indj)








