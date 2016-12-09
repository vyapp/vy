from vyapp.widgets import FloatingWindow, MatchBox
from vyapp.tools import match_sub_pattern
from Tkinter import LEFT, BOTH

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
        self.feed()

        self.bind('<BackSpace>', self.on_delete)
        self.bind('<Key>', self.update_selection)
        self.bind('<Return>', self.complete)
        self.bind('<Escape>', lambda event: 
        self.master.destroy())

        # Shortcut.
        self.bind('<Alt-p>', lambda event: 
        event.widget.event_generate('<Key-Down>'))
        self.bind('<Alt-o>', lambda event: 

        event.widget.event_generate('<Key-Up>'))
        self.pattern_index = self.calc_pattern_index()

    def calc_pattern_index(self):
        pattern = str(self.area.get(
        '%s linestart' % self.master.start_index, 
        '%s lineend' % self.master.start_index))

        seq = match_sub_pattern(pattern, 
        self.get(0, 'end'))

        try:
            match, index = next(seq)
        except StopIteration:
            return self.master.start_index
        line = self.area.indint(
            self.master.start_index)[0]
        return '%s.%s' % (line, index)

    def feed(self):
        for ind in self.completions:
            self.insert('end', ind.name)

    def update_selection(self, event):
        if not event.char: return
        # Just insert the character on the areavi.
        self.area.echo_num(event.keysym_num)
        data = self.area.get(self.pattern_index, 'insert')
        self.match_elem(data)

    def selection_docs(self):
        item, = self.curselection()
        return self.completions[item].docstring()

    def complete(self, event):
        item = self.curselection()
        word = self.get(item)
        self.area.delete(self.pattern_index, 'insert')
        self.area.insert(self.pattern_index, word)
        self.master.destroy()

    def on_delete(self, event):
        self.area.backspace()
        # Check for cursor position.
        x, y = self.area.indcur()
        m, n = self.area.indint(self.master.start_index)

        if x != m or (m == x and y < n): self.master.destroy()

class CompletionWindow(FloatingWindow):
    def __init__(self, area, completions, *args, **kwargs):
        FloatingWindow.__init__(self, area, *args, **kwargs)
        self.bind('<FocusOut>', lambda event: self.destroy(), add=True)

        self.box = CompleteBox(area, completions, self)
        self.box.pack(side=LEFT, fill=BOTH, expand=True)




