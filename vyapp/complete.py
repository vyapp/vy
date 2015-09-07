from Tkinter import *

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

class CompleteWindow(Toplevel):
    """
    This class should be inherited by plugins that implement auto completion.

    The method CompleteWindow.feed should be implemented to feed the window
    with possible completions.

    Example:

    class PythonCompleteWindow(CompleteWindow):
        def __init__(self, area, *args, **kwargs):
            self.area = area
            CompleteWindow.__init__(self, area, *args, **kwargs)
    
        def feed(self):
            source      = self.area.get('1.0', 'end')
            line        = self.area.indcur()[0]
            size        = len(self.area.get('insert linestart', 'insert'))
            script      = Script(source, line, size, self.area.filename)
            completions = script.completions()
    
            for ind in completions:
                self.box.insert('end', ind.name)


    In the above example it would display a python window completion.    
    """

    def __init__(self, area, *args, **kwargs):
        Toplevel.__init__(self, area, *args, **kwargs)

        self.box = CompleteBox(area, self)
        self.feed()
        self.box.pack(side=LEFT, fill=BOTH, expand=True)

        self.area = area
        self.wm_overrideredirect(1)
        self.wm_geometry("+10000+10000")
        self.update()

        rootx                                              = self.area.winfo_rootx()
        rooty                                              = self.area.winfo_rooty()
        self.start_index                                   = self.area.index('insert')
        x, y, width, height                                = self.area.bbox('insert')
        line_x, line_y, line_width, line_height, baseline  = self.area.dlineinfo('insert')

        win_height = self.winfo_height()
        area_height = self.area.winfo_height()
        win_width  = self.winfo_width()
        area_width = self.area.winfo_width()

        vpos = self.calculate_vertical_position(y, rooty, line_height, win_height, area_height)
        hpos = self.calculate_horizontal_position(x, rootx, win_width, area_width)

        self.wm_geometry("+%d+%d" % (hpos, vpos))


        self.box.focus_set()
        self.box.grab_set()
        self.area.wait_window(self)

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

    def feed(self):
        pass

