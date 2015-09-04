from Tkinter import *
from jedi import Script

class Wordbox(Toplevel):
    def __init__(self, area, *args, **kwargs):
        Toplevel.__init__(self, area, *args, **kwargs)

        self.box = Listbox(self)
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
        self.insert_words()

        self.area.hook(self.area.id, '<Key>', lambda event: self.after(1, self.match_elem))
        self.area.hook(self.area.id, '<Key>', lambda event: self.after(1, self.check_cursor_pos))
        self.area.hook(self.area.id, '<Return>', lambda event: self.do_completion())
        self.area.hook(self.area.id, '<Down>', lambda event: self.down())
        self.area.hook(self.area.id, '<Up>', lambda event: self.up())

    def check_cursor_pos(self):
        """
        """

        if self.area.compare('insert', '<=', self.start_index):
            self.stop_completion()

    def up(self):
        index = self.box.curselection()[0]
        if not index: return
        index = index - 1
        self.set_selection(index)

        return 'break'

    def down(self):
        index = self.box.curselection()[0]
        if not index: return
        index = index + 1
        self.set_selection(index)
        return 'break'

    def insert_word(self):
        index = self.box.curselection()
        word  = self.box.get(index)
        self.area.insert('insert', word)
        self.restore_focus_scheme()

    def restore_focus_scheme(self):
        self.area.focus_set()
        self.destroy()

    def insert_words(self):
        source      = self.area.get('1.0', 'end')
        line        = self.area.indcur()[0]
        size        = len(self.area.get('insert linestart', 'insert'))
        script      = Script(source, line, size, self.area.filename)
        completions = script.completions()

        for ind in completions:
            self.box.insert('end', ind.name)

    def do_completion(self):
        index = self.box.curselection()
        word  = self.box.get(index)
        self.area.delete(self.start_index, 'insert')
        self.area.insert(self.start_index, word)
        self.stop_completion()
        return 'break'

    def stop_completion(self):
        self.area.unhook(self.area.id, '<Key>')
        self.area.unhook(self.area.id, '<Return>')
        self.area.unhook(self.area.id, '<Up>')
        self.area.unhook(self.area.id, '<Down>')
        self.destroy()

    def match_elem(self):
        data = self.area.get(self.start_index, 'insert')
        self.select_elem(data)

    def select_elem(self, data):
        elems = self.box.get(0, 'end')

        for ind in xrange(0, len(elems)):
            if elems[ind].startswith(data): 
                self.set_selection(ind)
                break

    def set_selection(self, index):
        self.box.selection_clear(0, 'end')
        self.box.selection_set(index)
        self.box.see(index)


