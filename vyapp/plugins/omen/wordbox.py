from Tkinter import *
from jedi import Script

class Wordbox(Toplevel):
    def __init__(self, area, *args, **kwargs):
        Toplevel.__init__(self, area, *args, **kwargs)

        self.box = Listbox(self)
        self.area = area

        self.bind('<Return>', lambda event: self.insert_word())
        self.bind('<Escape>', lambda event: self.restore_focus_scheme())
        self.bind('<Key-j>', lambda event: self.box.event_generate('<Down>'))
        self.bind('<Key-k>', lambda event: self.box.event_generate('<Up>'))

        self.wm_overrideredirect(1)
        self.wm_geometry("+10000+10000")
        rootx = self.area.winfo_rootx()
        rooty = self.area.winfo_rooty()
        x, y, width, height = self.area.bbox('insert')
        self.wm_geometry("+%d+%d" % (x+rootx, y+rooty))
        self.box.pack(side=LEFT, fill=BOTH, expand=True)

        self.do_completion()
        self.box.focus_set()
        self.grab_set()
        self.area.wait_window(self)

    def insert_word(self):
        index = self.box.curselection()
        word  = self.box.get(index)
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
            self.box.insert('end', ind.name)
    

