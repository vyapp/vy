from Tkinter import *
from areavi import *
from ttk import Notebook

class Note(Notebook):
    def __init__(self, max_tabs, *args, **kwargs):
        Notebook.__init__(self, *args, **kwargs)
        self.max_tabs = max_tabs

        self.posX = 0

    def get_visible_tabs(self):
        return map(lambda ind: self.tab(ind)['state'] != 'hidden', 
                   self.tabs())


    def is_visible_tab(self, tab_id):
        return self.tab(tab_id)['state'] != 'hidden'

    def add(self, child, **kwargs):
        Notebook.add(self, child, **kwargs)
        self.render_tabs()


    def render_tabs(self):
        for ind in range(0, self.posX):
            self.tab(ind, state='hidden')

        for ind in range(self.posX + self.max_tabs, len(self.tabs())):
            self.tab(ind, state='hidden')

        for ind in range(self.posX, self.posX + self.max_tabs):
            try:
                self.tab(ind, state='normal')
            except TclError:
                pass
        
    def forget(self, child):
        Notebook.forget(self, child)
        if self.posX > 0: self.posX = self.posX - 1
        self.render_tabs()


    def scroll_right(self):
        if self.posX + self.max_tabs >= len(self.tabs()): return

        self.posX = self.posX + 1
        self.render_tabs()

    def scroll_left(self):
        if self.posX <= 0: return

        self.posX = self.posX - 1
        self.render_tabs()

class NoteVi(Note):
    def __init__(self, *args, **kwargs):
        Note.__init__(self, *args, **kwargs)

    def create(self, filename):
        base = PanedVerticalWindow(master=self)
        base.create()
        self.add(base, text=filename)
        return base

    def load(self, *args):
        for indi in args:
            base = PanedVerticalWindow(master=self)
            base.pack(side='left', expand=True, fill=BOTH)

            self.add(base)        
            for indj in indi:
                base.load(*indj)


class PanedHorizontalWindow(PanedWindow):
    def __init__(self, *args, **kwargs):
        PanedWindow.__init__(self, orient=HORIZONTAL, *args, **kwargs)

    def create_area(self):
        frame     = Frame(master=self)
        scrollbar = Scrollbar(master=frame)
        area      = AreaVi('none', frame , border=3, relief=RAISED, 
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

    def create(self):
        area = self.create_area()
        self.add(area.master)
        return area

    def load(self, filename):
        area = self.create_area()
        self.add(area.master)
        area.load_data(filename)
        return area

class PanedVerticalWindow(PanedWindow):
    def __init__(self, *args, **kwargs):
        PanedWindow.__init__(self, orient=VERTICAL, *args, **kwargs)

    def create(self):
        base = PanedHorizontalWindow(master=self)
        self.add(base)
        base.create()
        return base

    def load(self, *args):
        base = PanedHorizontalWindow(master=self)
        self.add(base)

        for ind in args:
            base.load(ind)
        return base


class Manager(object):
    def __init__(self, *args, **kwargs):
        self.tab_lst = []
        self.index   = -1
        self.args    = args
        self.kwargs  = kwargs

    def create(self):
        base = PanedVerticalWindow(*self.args, **self.kwargs)
        base.create()
        base.pack(side='left', expand=True, fill=BOTH)

        self.tab_lst.append(base)
        return base

    def load(self, *args):
        """ (1, ((1, ("file1", "file2")), )) """

        for _, indi in args:
            base = PanedVerticalWindow(*self.args, **self.kwargs)
            base.pack(side='left', expand=True, fill=BOTH)
            self.tab_lst.append(base)

            for _, indj in indi:
                base.load(*indj)













