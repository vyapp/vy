from tkinter import Listbox, Toplevel,  BOTH, END, TOP, ACTIVE
from os.path import exists, dirname, join, relpath
from vyapp.tools import findline
from vyapp.areavi import AreaVi
from vyapp.app import root

class MatchBox(Listbox):
    def __init__(self, *args, **kwargs):
        Listbox.__init__(self, *args, **kwargs)

    def startswith(self, data):
        """
        """

        elems = self.get(0, 'end')

        for ind in range(0, self.size()):
            if elems[ind].startswith(data): 
                return ind
        else:
            raise ValueError
                
    def selection_item(self, data):
        """
        """

        self.selection_clear(0, 'end')
        index = self.startswith(data)
        self.activate(index)
        self.selection_set(index)
        self.see(index)

class Echo(object):
    """

    """

    def __init__(self, area):
        self.area = area
        self.bind('<BackSpace>', self.on_backspace)
        self.bind('<Key>', self.dispatch)

    def dispatch(self, event):
        if event.char:  self.on_char(event.char)

    def on_char(self, char):
        self.area.echo(char)

    def on_backspace(self, event):
        self.area.backspace()
        self.on_delete(event)

    def on_delete(self, event):
        pass

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


class OptionWindow(Toplevel):
    def  __call__(self, options=[]):
        self.options = options

        self.listbox.delete(0, END)
        for key, value in options:
            self.listbox.insert(END, key)
        return self.display()

    def  __init__(self):
        Toplevel.__init__(self, master=root)
        self.options = None
        self.title('Matches')

        self.listbox = Listbox(master=self)

        self.listbox.pack(expand=True, fill=BOTH, side=TOP)
        self.listbox.focus_set()
        self.listbox.activate(0)
        self.listbox.selection_set(0)

        self.listbox.config(width=50)

        self.listbox.bind('<Key-h>', lambda event:
        self.listbox.event_generate('<Left>'))

        self.listbox.bind('<Key-l>', lambda event:
        self.listbox.event_generate('<Right>'))

        self.listbox.bind('<Key-k>', lambda event:
        self.listbox.event_generate('<Up>'))

        self.listbox.bind('<Key-j>', lambda event:
        self.listbox.event_generate('<Down>'))

        self.listbox.bind('<Escape>', lambda event: self.close())
        self.listbox.bind('<Return>', lambda event: self.on_selection())
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.transient(root)
        self.withdraw()

    def on_selection(self):
        pass

    def display(self):
        self.grab_set()
        self.deiconify()
        self.listbox.focus_set()
        # self.wait_window(self)

    def close(self):
        # When calling destroy or withdraw without 
        # self.deoiconify it doesnt give back 
        # the focus to the parent window.

        self.deiconify()
        self.grab_release()
        self.withdraw()

class LinePicker(OptionWindow):
    def  __call__(self, options=[]):
        options = zip(('%s - %s %s' % (relpath(filename), line, msg)
        for filename, line, msg in options), options)
        super(LinePicker, self).__call__(list(options))

    def on_selection(self):
        index = self.listbox.index(ACTIVE)
        findline(*self.options[index][1])
        self.close()



