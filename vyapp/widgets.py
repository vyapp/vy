from Tkinter import Listbox, Toplevel

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


