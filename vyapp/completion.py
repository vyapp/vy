from vyapp.widgets import FloatingWindow, MatchBox
from vyapp.regutils import match_sub_pattern
from tkinter import LEFT, BOTH, Text, SCROLL
from vyapp.mixins import Echo

class Option:
    def __init__(self, name, type='', doc=''):
        self.name = name
        self.doc  = doc
        self.type = type

    def docstring(self):
        return '%s\n%s' % (self.type, self.doc)

class CompleteBox(MatchBox, Echo):
    """
    Abstraction of a complete box widget to be used anywhere.
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
        lba0 = lambda e: e.widget.event_generate('<Key-Down>')
        lba1 = lambda e: e.widget.event_generate('<Key-Up>')

        self.bind('<Alt-p>', lba0)
        self.bind('<Alt-o>', lba1)
        self.index = self.calc_index()

    def calc_index(self):
        """
        Calculate the correct starting index to be swaped.
        Consider the example below:
            ls = []
            ls.app<Complete>

        The correct starting index would be 2 not 5.
        """

        start     = '%s linestart' % self.master.start_index
        end       = '%s lineend' % self.master.start_index
        pattern   = str(self.area.get(start, end))
        pattern   = pattern.lower()
        lst       = [ind.lower() for ind in self.get(0, 'end')]
        seq       = match_sub_pattern(pattern, lst)
        line, col = self.area.indexsplit(self.master.start_index)

        _, index = next(seq, (None, col))
        return '%s.%s' % (line, index)

    def on_delete(self, event):
        m, n = self.area.indexsplit(self.master.start_index)
        x, y = self.area.indexref()
        if x != m or (m == x and y < n): self.master.destroy()

    def complete(self, event):
        """
        Grab the selected item and swap it with the areavi cursor
        string. It completes the cursor word.
        """

        self.area.swap(self.get(
        self.curselection()), self.index, 'insert')
        self.master.destroy()

    def selection_docs(self):
        """
        Grab the item docs and return it.
        """

        item, = self.curselection()
        return self.completions[item].docstring()

    def on_char(self, char):
        super(CompleteBox, self).on_char(char)
        self.selection_item(self.area.get(self.index, 'insert'))

    def feed(self):
        for ind in self.completions:
            self.insert('end', ind.name)

class FloatingText(FloatingWindow):
    def __init__(self, area, data, *args, **kwargs):
        FloatingWindow.__init__(self, area, *args, **kwargs)

        self.text = Text(master=self)
        self.text.insert('1.0', data)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        self.text.focus_set()

class CompletionWindow(FloatingWindow):
    def __init__(self, area, completions, *args, **kwargs):
        FloatingWindow.__init__(self, area, *args, **kwargs)
        self.box = CompleteBox(area, completions, self)
        self.box.pack(side=LEFT, fill=BOTH, expand=True)

        self.text = Text(master=self, 
        blockcursor=True, insertbackground='black', )

        # self.text.bindtags((self.text,  '.'))
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        self.text.pack_forget()
        self.update()

        # We need this otherwise it propagates the event
        # and the window gets destroyed in the wrong situation.
        self.box.bind('<FocusOut>', lambda event: 'break', add=True)
        self.text.bind('<FocusOut>', lambda event: 'break', add=True)

        self.text.bind('<Escape>', self.options_window, add=True)

        self.text.bind('<Alt-p>', lambda event: 
        self.text.yview(SCROLL, 1, 'page'), add=True)

        self.text.bind('<Alt-o>', lambda evenet: 
        self.text.yview(SCROLL, -1, 'page'), add=True)

        self.box.bind('<F1>', lambda event: self.docs_window())

    def options_window(self, event):
        self.text.pack_forget()
        self.box.pack(side=LEFT, fill=BOTH, expand=True)
        self.update()

        self.box.focus_set()
        return 'break'

    def docs_window(self):
        docs = self.box.selection_docs()
        self.box.pack_forget()

        self.text.delete('1.0', 'end')
        self.text.insert('1.0', docs)

        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        self.text.focus_set()
        self.update()


