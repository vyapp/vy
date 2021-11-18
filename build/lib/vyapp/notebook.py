from vyapp.panel import PanedVerticalWindow
from os.path import abspath, exists
from vyapp.areavi import AreaVi
from tkinter.ttk import Notebook
from os.path import exists
from tkinter import BOTH
import sys

class NoteVi(Notebook):
    """
    This class implements vy tabs.
    """

    def __init__(self, *args, **kwargs):
        Notebook.__init__(self, *args, **kwargs)
        self.bindtags((self, '.', 'all'))

    def create(self, filename):
        """
        This method creates a new tab whose title is the string
        passed as filename.
        """

        base = PanedVerticalWindow(master=self)
        area = base.create(filename)
        self.add(base, text=filename)
        return area

    def open(self, filename):
        base = PanedVerticalWindow(master=self)
        self.add(base)
        area = base.open(filename)
        return area

    def load(self, *args):
        """
        This method opens the files that are specified in args into new tabs and panes.
        The structure of args is like:

        args = ((('file1', 'file2'), ('file3', 'file4')), (('file5', 'file6'), ))

        It would create two tabs, the first tab would have four panes, the second tab
        would be two panes.
        """

        for indi in args:
            base = PanedVerticalWindow(master=self)
            base.pack(side='left', expand=True, fill=BOTH)
            self.add(base)        
            for indj in indi:
                base.load(*indj)

    def next(self, func):
        """
        """

        tabs  = self.tabs()
        index = self.index(self.select())

        for ind in tabs[index + 1:]:
            if func(self.tab(ind, 'text')): 
                yield ind
    
    def back(self, func):
        """
        """

        tabs  = self.tabs()
        index = self.index(self.select())
        tabs  = tabs[:index]

        for ind in reversed(tabs):
            if func(self.tab(ind, 'text')): 
                yield ind

    def find(self, func):
        for ind in self.tabs():
            if func(self.tab(ind, 'text')):
                yield ind

    def set_area_focus(self):
        wid  = self.nametowidget(self.select())
        wid.focused_area.focus_set()

    def restore_area_focus(self):
        """
        When an AreaVi is destroyed, the focused_area
        is a dead widget, so it gives focus to the first AreaVi
        in the active tab.
        """

        wid  = self.nametowidget(self.select())
        seq  = AreaVi.areavi_widgets(wid)
        area = next(seq)
        area.focus_set()

    def on(self, *args):
        """
        When the method Notebook.select is called it sets the application
        focus to the last visible widget in the selected tab. This method
        calls select then restores the focus. It may sound like a bug in tkinter.
        """

        wid=self.focus_get()
        self.select(*args)
        self.after(30, lambda : wid.focus_set())

    def find_area(self, filename, auto_open=False):
        filename = abspath(filename)
        wids = AreaVi.get_opened_files(self)
        area = wids.get(filename)

        if area is None:
            if exists(filename) and auto_open:
                return self.open(filename)
        return area

    def find_line(self, filename, line, col=0, auto_open=False):
        """
        """

        area = self.find_area(filename, auto_open)
        if area is not None:
            self.focus_line(area, line)
        return area

    def focus_line(self, area, line):
        self.select(area.master.master.master)
        area.focus()
        area.setcur(line, 0)

