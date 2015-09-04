from Tkinter import Listbox
from jedi import Script

class Wordbox(Listbox):
    def __init__(self, area, *args, **kwargs):
        Listbox.__init__(self, area, *args, **kwargs)
        self.area = area
        self.bind('<Return>', lambda event: self.insert_word())
        self.bind('<Escape>', lambda event: self.restore_focus_scheme())

        self.do_completion()
        self.focus_set()
        # self.grab_set()
        # self.area.wait_window(self)

    def insert_word(self):
        index = self.curselection()
        word  = self.get(index)
        self.area.insert('insert', word)
        self.restore_focus_scheme()

    def restore_focus_scheme(self):
        self.area.focus_set()
        self.destroy()

    def do_completion(self):
        source = self.area.get('1.0', 'end')
        line   = self.area.indcur()[0]
        size   = len(self.area.get('insert linestart', 'insert'))
        script = Script(source, line, size, self.area.filename)
        completions = script.completions()

        for ind in completions:
            self.insert('end', ind.name)
    

