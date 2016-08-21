from vyapp.exe import exec_quiet
from Tkinter import *
from vyapp.tools import match_sub_pattern

class MatchBox(Listbox):
    def __init__(self, *args, **kwargs):
        Listbox.__init__(self, *args, **kwargs)

    def startswith(self, data):
        elems = self.get(0, 'end')

        for ind in xrange(0, self.size()):
            if elems[ind].startswith(data): 
                return ind
        else:
            raise ValueError
                
    def match_elem(self, data):
        try:
            index = self.startswith(data)
        except ValueError:
            self.selection_clear(0, 'end')
        else:
            self.single_selection_set(index)

    def single_selection_set(self, index):
        self.activate(index)
        self.selection_clear(0, 'end')
        self.selection_set(index)
        self.see(index)

class FloatingWindow(Toplevel):
    """
    """

    def __init__(self, area, *args, **kwargs):
        Toplevel.__init__(self, area, *args, **kwargs)
        self.area = area
        self.wm_overrideredirect(1)
        self.wm_geometry("+10000+10000")
        self.bind('<Configure>', lambda event: self.update())
        self.update()

    def update(self):
        Toplevel.update(self)

        rootx                = self.area.winfo_rootx()
        rooty                = self.area.winfo_rooty()
        self.start_index     = self.area.index('insert')
        x, y, width, height  = self.area.bbox('insert')
        info                 = self.area.dlineinfo('insert')
        line_x               = info[0]
        line_y               = info[1]
        line_width           = info[2]
        line_height          = info[3]
        baseline             = info[4]
        win_height           = self.winfo_height()
        area_height          = self.area.winfo_height()
        win_width            = self.winfo_width()
        area_width           = self.area.winfo_width()
        vpos                 = self.calculate_vertical_position(y, rooty, 
                                                    line_height, win_height, area_height)
        hpos                 = self.calculate_horizontal_position(x, rootx, win_width, area_width)


        self.wm_geometry("+%d+%d" % (hpos, vpos))

    def calculate_vertical_position(self, y, rooty, line_height, win_height, area_height):
        if rooty + y + win_height + line_height > rooty + area_height:
            return rooty + y - win_height
        else:
            return rooty + y + line_height

    def calculate_horizontal_position(self, x, rootx, win_width, area_width):
        if x + rootx + win_width > rootx + area_width:
            return rootx + area_width - win_width
        else:
            return rootx + x

    def destroy(self):
        self.area.focus_set()
        Toplevel.destroy(self)


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



