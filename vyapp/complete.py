from vyapp.exe import exec_quiet
from vyapp.widgets import MatchBox, FloatingWindow
from Tkinter import *
from vyapp.tools import match_sub_pattern

class Option(object):
    def __init__(self, name, type='', doc=''):
        self.name = name
        self.doc  = doc
        self.type = type

    def docstring(self):
        return '%s\n%s' % (self.type, self.doc)

class CompleteBox(MatchBox):
    def __init__(self, area, completions, *args, **kwargs):
        MatchBox.__init__(self, *args, **kwargs)

        self.completions = completions
        self.area        = area
        self.focus_set()
        # self.grab_set()
        self.feed()

        self.bind('<Key>', lambda event: area.echo_num(event.keysym_num), add=True)
        self.bind('<BackSpace>', lambda event: area.backspace(),  add=True)
        self.bind('<BackSpace>', self.check_cursor_position, add=True)
        self.bind('<Key>', self.update_selection, add=True)
        self.bind('<Return>', self.complete, add=True)
        self.bind('<Escape>', lambda event: self.master.destroy(), add=True)
        self.pattern_index = self.calc_pattern_index()

    def calc_pattern_index(self):
        pattern = self.area.get('%s linestart' % self.master.start_index, 
                                   '%s lineend' % self.master.start_index)
        seq     = match_sub_pattern(str(pattern), self.get(0, 'end'))

        try:
            match, index = next(seq)
        except StopIteration:
            return self.master.start_index
        line = self.area.indint(self.master.start_index)[0]
        return '%s.%s' % (line, index)

    def feed(self):
        for ind in self.completions:
            self.insert('end', ind.name)

    def update_selection(self, event):
        if event.char:
            self.match_elem()

    def match_elem(self):
        data = self.area.get(self.pattern_index, 'insert')
        MatchBox.match_elem(self, data)

    def elem_desc(self):
        item, = self.curselection()
        return self.completions[item].docstring()

    def complete(self, event):
        item = self.curselection()
        word = self.get(item)
        self.area.delete(self.pattern_index, 'insert')
        self.area.insert(self.pattern_index, word)
        self.master.destroy()

    def check_cursor_position(self, event):
        x, y = self.area.indcur()
        m, n = self.area.indint(self.master.start_index)

        if x != m or (m == x and y < n):
            self.master.destroy()

class CompleteWindow(FloatingWindow):
    def __init__(self, area, completions, *args, **kwargs):
        FloatingWindow.__init__(self, area, *args, **kwargs)
        self.bind('<FocusOut>', lambda event: self.destroy(), add=True)

        self.box = CompleteBox(area, completions, self)
        self.box.pack(side=LEFT, fill=BOTH, expand=True)







