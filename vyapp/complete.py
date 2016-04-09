from vyapp.exe import exec_quiet
from vyapp.widgets import MatchBox, FloatingWindow
from Tkinter import *

class CompleteBox(MatchBox):
    def __init__(self, area, completions, *args, **kwargs):
        MatchBox.__init__(self, *args, **kwargs)
        self.completions = completions
        self.area        = area
        self.focus_set()
        self.grab_set()
        self.feed()

        self.bind('<Key>', lambda event: area.echo_num(event.keysym_num), add=True)
        self.bind('<BackSpace>', lambda event: area.backspace(),  add=True)
        self.bind('<BackSpace>', self.check_cursor_position, add=True)
        self.bind('<Key>', self.update_selection, add=True)
        self.bind('<Return>', self.complete, add=True)
        self.bind('<Escape>', lambda event: self.master.destroy(), add=True)

    def feed(self):
        for ind in self.completions:
            self.insert('end', ind.name)

    def update_selection(self, event):
        if event.char:
            self.match_elem()

    def match_elem(self):
        data = self.area.get(self.master.start_index, 'insert')
        MatchBox.match_elem(self, data)

    def elem_desc(self):
        item, = self.curselection()
        return self.completions[item].docstring()

    def complete(self, event):
        item = self.curselection()
        word = self.get(item)
        self.area.delete(self.master.start_index, 'insert')
        self.area.insert(self.master.start_index, word)
        self.master.destroy()

    def check_cursor_position(self, event):
        x, y = self.area.indcur()
        m, n = self.area.indint(self.master.start_index)

        if x != m or (m == x and y < n):
            self.master.destroy()

class CompleteWindow(FloatingWindow):
    def __init__(self, area, completions, *args, **kwargs):
        FloatingWindow.__init__(self, area, *args, **kwargs)

        self.box = CompleteBox(area, completions, self)
        self.box.pack(side=LEFT, fill=BOTH, expand=True)




