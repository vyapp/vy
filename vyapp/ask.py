from Tkinter import *
from vyapp.app import root

class Ask(Entry):
    def __init__(self, area, default_data ='', wait=True):
        self.area  = area
        self.data  = '' 
        self.frame = Frame(root.read_data, border=1, padx=3, pady=3)
        self.frame.pack(expand=True, fill=X)
        
        Entry.__init__(self, self.frame)
        self.config(background='grey')

        self.pack(side='left', expand=True, fill=BOTH)
        self.focus_set()

        self.bind('<Escape>', lambda event: self.restore_focus_scheme())
        self.bind('<Return>', lambda event: self.on_success())

        # It seems that if i put self.data = default_data
        # after self.area.wait_window(self) it sets self.data
        # after it has being set in self.ok then i get
        # the insert mark being reset to insert again.

        self.insert('end', default_data)
        root.read_data.pack(fill=X)

        # It has to wait for self.frame otherwise it seems the marks
        # added by Stdout, the code_mark stuff disappear.
        # this was insanely crazy to find.
        self.frame.grab_set()
        if wait: self.area.wait_window(self.frame)

    def on_success(self):
        self.data = self.get()
        self.restore_focus_scheme()

    def restore_focus_scheme(self):
        self.frame.destroy()
        root.read_data.pack_forget()
        self.area.focus_set()

if __name__ == '__main__':
    area = Tk()
    search_dialog = Ask(area, 'Ask')
    area.mainloop()












