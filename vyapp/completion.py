from vyapp.widgets import FloatingWindow, MatchBox, Echo
from vyapp.tools import match_sub_pattern
from Tkinter import LEFT, BOTH

class Option(object):
    def __init__(self, name, type='', doc=''):
        self.name = name
        self.doc  = doc
        self.type = type

    def docstring(self):
        return '%s\n%s' % (self.type, self.doc)

class CompleteBox(MatchBox, Echo):
    """
    """

    def __init__(self, area, completions, *args, **kwargs):
        MatchBox.__init__(self, *args, **kwargs)
        Echo.__init__(self, area)

        self.completions = completions
        self.area        = area
        self.focus_set()
        self.feed()

        self.bind('<Return>', self.complete)
        self.bind('<Escape>', lambda event: 
        self.master.destroy())

        # Shortcut.
        self.bind('<Alt-p>', lambda event: 
        event.widget.event_generate('<Key-Down>'))
        self.bind('<Alt-o>', lambda event: 
        event.widget.event_generate('<Key-Up>'))

        self.index = self.calc_index()

    def calc_index(self):
        pattern = str(self.area.get(
        '%s linestart' % self.master.start_index, 
        '%s lineend' % self.master.start_index)).lower()

        seq = match_sub_pattern(pattern,
        map(lambda ind: ind.lower(), self.get(0, 'end')))
        line, col = self.area.indint(self.master.start_index)

        _, index = next(seq, (None, col))
        return '%s.%s' % (line, index)

    def on_delete(self, event):
        m, n = self.area.indint(self.master.start_index)
        x, y = self.area.indcur()
        if x != m or (m == x and y < n): 
            self.master.destroy()

    def complete(self, event):
        self.area.swap(self.get(
        self.curselection()), self.index, 'insert')
        self.master.destroy()

    def selection_docs(self):
        item, = self.curselection()
        return self.completions[item].docstring()

    def on_char(self, event):
        self.selection_item(self.area.get(
        self.index, 'insert'))

    def feed(self):
        for ind in self.completions:
            self.insert('end', ind.name)

class CompletionWindow(FloatingWindow):
    def __init__(self, area, completions, *args, **kwargs):
        FloatingWindow.__init__(self, area, *args, **kwargs)
        self.bind('<FocusOut>', lambda event: self.destroy(), add=True)

        self.box = CompleteBox(area, completions, self)
        self.box.pack(side=LEFT, fill=BOTH, expand=True)




