from Tkinter import *

class Ask(Toplevel):
    def __init__(self, area, title, default_data ='', *args, **kwargs):
        self.area = area
        Toplevel.__init__(self, area, *args, **kwargs)

        # self.protocol("WM_DELETE_WINDOW", self.destroy())
        self.bind('<Escape>', lambda event: self.destroy())
        self.bind('<Return>', lambda event: self.ok())
        
        self.title(title)
        self.transient(area)
        self.resizable(width=False, height=False)
        self.frame = Frame(self, relief='raised', border=1,  padx=3, pady=3)
        
        self.entry = Entry(self.frame)

        self.frame.pack(side='top', expand=True, fill=BOTH)
        self.entry.pack(side='left', expand=True, fill=BOTH)

        self.entry.focus_set()

        # It seems that if i put self.data = default_data
        # after self.area.wait_window(self) it sets self.data
        # after it has being set in self.ok then i get
        # the insert mark being reset to insert again.

        self.entry.insert('end', default_data)
        self.data = default_data

        self.grab_set()
        self.area.wait_window(self)

    def ok(self):
        self.data = self.entry.get()
        self.destroy()
    
if __name__ == '__main__':
    area = Tk()
    search_dialog = Ask(area, 'Ask')
    area.mainloop()






