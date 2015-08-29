from Tkinter import *
from vyapp.app import root

class Ask():
    def __init__(self, area, title='', default_data =''):
        self.area = area

        self.frame = Frame(root.read_data, border=1, padx=3, pady=3)
        self.frame.pack(expand=True, fill=X)
        
        self.entry = Entry(self.frame)
        self.entry.config(background='grey')

        self.entry.pack(side='left', expand=True, fill=BOTH)
        self.entry.focus_set()

        self.entry.bind('<Escape>', lambda event: self.restore_focus_scheme())
        self.entry.bind('<Return>', lambda event: self.ok())

        # It seems that if i put self.data = default_data
        # after self.area.wait_window(self) it sets self.data
        # after it has being set in self.ok then i get
        # the insert mark being reset to insert again.

        self.entry.insert('end', default_data)

        self.data = default_data

        root.read_data.pack(fill=X)

        # It has to wait for self.frame otherwise it seems the marks
        # added by Stdout, the code_mark stuff disappear.
        # this was insanely crazy to find.
        self.frame.grab_set()
        self.area.wait_window(self.frame)


    def ok(self):
        self.data = self.entry.get()
        self.restore_focus_scheme()

    def restore_focus_scheme(self):
        self.frame.destroy()
        root.read_data.pack_forget()
        self.area.focus_set()

if __name__ == '__main__':
    area = Tk()
    search_dialog = Ask(area, 'Ask')
    area.mainloop()








