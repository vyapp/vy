from tkinter import PanedWindow, RAISED, BOTH, HORIZONTAL
from tkinter import Frame, Scrollbar, Y, VERTICAL
from vyapp.areavi import AreaVi

class PanedHorizontalWindow(PanedWindow):
    """
    This widget is used to create horizontal panes.
    """

    def __init__(self, *args, **kwargs):
        PanedWindow.__init__(self, orient=HORIZONTAL, *args, **kwargs)

    def create(self, filename='none'):
        """
        This method creates a horizontal AreaVi widget. It returns the
        AreaVi widget that was created. It as well installs the plugins
        that appear in the vyrc file in the AreaVi widget.
        """
        frame     = Frame(master=self)
        scrollbar = Scrollbar(master=frame)
        area      = AreaVi(filename, frame , border=3, relief=RAISED, 
                           yscrollcommand=scrollbar.set)
        scrollbar.config(command=area.yview)
        scrollbar.pack(side='right', fill=Y)

        from vyapp.plugins import HANDLE

        for handle, args, kwargs in HANDLE:
            handle(area, *args, **kwargs)

        area.focus_set()
        area.pack(expand=True, side='left', fill=BOTH)
        self.add(frame)

        def save_focus(event):
            self.master.focused_area = area

        self.master.focused_area = area
        area.bind('<FocusIn>', save_focus)
        return area

    def load(self, filename):
        """
        It creates a horizontal split and loads the content of filename
        into the new AreaVi instance. It returns the AreaVi widget that
        was created.
        """

        area = self.create()
        area.load_data(filename)
        return area

class PanedVerticalWindow(PanedWindow):
    """
    This widget implements vertical panes.
    """

    def __init__(self, *args, **kwargs):
        PanedWindow.__init__(self, orient=VERTICAL, *args, **kwargs)
        self.focused_area = None

    def create(self, filename='none'):
        """
        This method creates a new horizontal window in which
        it is possible to create new horizontal splits. The argument filename
        is set as attribute for the new AreaVi widget.
        """

        base = PanedHorizontalWindow(master=self)
        self.add(base)
        area = base.create(filename)
        return area

    def open(self, filename):
        base = PanedHorizontalWindow(master=self)
        self.add(base)
        area = base.load(filename)
        return area

    def load(self, *args):
        """
        This method adds a new horizontal window and loads
        the content of the files passed as args in the new AreaVi

        widgets.
        """

        base = PanedHorizontalWindow(master=self)
        self.add(base)

        for ind in args:
            base.load(ind)
        return base

