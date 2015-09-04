from Tkinter import *
from jedi import Script

class MatchBox(Listbox):
    def __init__(self, *args, **kwargs):
        Listbox.__init__(self, *args, **kwargs)

    def match_elem(self, data):
        elems = self.get(0, 'end')

        for ind in xrange(0, self.size()):
            if elems[ind].startswith(data): 
                return ind
                            
    def set_single_selection(self, index):
        self.activate(index)
        self.selection_clear(0, 'end')
        self.selection_set(index)
        self.see(index)

class CompleteBox(MatchBox):
    def __init__(self, area, *args, **kwargs):
        MatchBox.__init__(self, *args, **kwargs)
        self.area = area


        self.bind('<Key>', self.insert_area_char, add=True)
        self.bind('<BackSpace>', self.delete_area_char, add=True)

        self.bind('<Key>', self.find_word, add=True)
        self.bind('<Return>', self.complete, add=True)
        self.bind('<Escape>', lambda event: self.restore_focus_scheme(), add=True)

    def delete_area_char(self, event):
        self.area.delete('insert -1c', 'insert')
        self.check_char_pos()

    def check_char_pos(self):
        x, y = self.area.indcur()
        m, n = self.area.indint(self.master.start_index)

        if x != m or (m == x and y < n):
            self.restore_focus_scheme()

    def numchar(self, num):
        try:
            char = chr(num)
        except ValueError:
            pass
        else:
            return char

    def insert_area_char(self, event):
        char = self.numchar(event.keysym_num)
        if char: self.area.insert('insert', char)

    def find_word(self, event):
        if not self.numchar(event.keysym_num): return

        data   = self.area.get(self.master.start_index, 'insert')
        index  = self.match_elem(data)

        if index: self.set_single_selection(index)
        else: self.selection_clear(0, 'end')

    def complete(self, event):
        item = self.curselection()

        if not item: 
            self.restore_focus_scheme()
            return

        word = self.get(item)
        self.area.delete(self.master.start_index, 'insert')
        self.area.insert(self.master.start_index, word)
        self.restore_focus_scheme()

    def restore_focus_scheme(self):
        self.area.focus_set()
        self.master.destroy()

class PythonCompleteBox(CompleteBox):
    def __init__(self, area, *args, **kwargs):
        CompleteBox.__init__(self, area, *args, **kwargs)

        source      = self.area.get('1.0', 'end')
        line        = self.area.indcur()[0]
        size        = len(self.area.get('insert linestart', 'insert'))
        script      = Script(source, line, size, self.area.filename)
        completions = script.completions()

        for ind in completions:
            self.insert('end', ind.name)

class PythonCompleteWindow(Toplevel):
    def __init__(self, area, *args, **kwargs):
        Toplevel.__init__(self, area, *args, **kwargs)

        self.box = PythonCompleteBox(area, self)
        self.area = area
        self.wm_overrideredirect(1)
        self.wm_geometry("+10000+10000")

        rootx                                              = self.area.winfo_rootx()
        rooty                                              = self.area.winfo_rooty()
        self.start_index                                   = self.area.index('insert')
        x, y, width, height                                = self.area.bbox('insert')
        line_x, line_y, line_width, line_height, baseline  = self.area.dlineinfo('insert')

        self.wm_geometry("+%d+%d" % (x+rootx, y+rooty + line_height))
        self.box.pack(side=LEFT, fill=BOTH, expand=True)

        self.box.focus_set()
        self.box.grab_set()
        self.area.wait_window(self)

    


