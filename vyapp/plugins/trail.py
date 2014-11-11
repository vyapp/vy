from Tkinter import *

class Trail(Toplevel):
    def __init__(self, area, region, *args, **kwargs):
        self.area = area
        self.region = region
        Toplevel.__init__(self, area, *args, **kwargs)

        self.protocol("WM_DELETE_WINDOW", self.finish_search)
        self.bind('<Escape>', lambda event: self.finish_search())
        
        self.title('Trail')

        self.frame1 = Frame(self, relief='raised', border=1,  padx=3, pady=3)
        self.frame2 = Frame(self, relief='raised', border=1, padx=3, pady=3)
        self.frame3 = Frame(self)
        
        self.label1 = Label(self.frame1, text='STR')
        self.entry1 = Entry(self.frame1)

        self.label2 = Label(self.frame2, text='REP')
        self.entry2 = Entry(self.frame2)
        
        self.frame1.pack(side='top', expand=True, fill=BOTH)
        self.frame2.pack(side='top', expand=True, fill=BOTH)
        self.frame3.pack(side='top', expand=True, fill=BOTH)

        self.label1.pack(side='left')
        self.entry1.pack(side='left', expand=True, fill=BOTH)

        self.label2.pack(side='left')
        self.entry2.pack(side='left', expand=True, fill=BOTH)

    
        self.button1 = Button(self.frame3, command=self.do_search)
        self.button2 = Button(self.frame3, text='Replace on')

        self.button1.pack(side='left', expand=True, fill=BOTH)
        self.button2.pack(side='left', expand=True, fill=BOTH)

        self.button3 = Button(self.frame3, command=self.replace_all_up)
        self.button3.pack(side='left', expand=True, fill=BOTH)

        self.button4 = Button(self.frame3, command=self.replace_all_down)
        self.button4.pack(side='left', expand=True, fill=BOTH)

        self.button5 = Button(self.frame3, command=self.replace_all)
        self.button5.pack(side='left', expand=True, fill=BOTH)

        self.button6 = Button(self.frame3, command=self.go_prev_found)
        self.button6.pack(side='left', expand=True, fill=BOTH)

        self.button6 = Button(self.frame3, command=self.go_next_found)
        self.button6.pack(side='left', expand=True, fill=BOTH)

        self.resizable(width=False, height=False)
        self.entry1.focus_set()

    def do_search(self):
        data = self.entry1.get()
    
    def replace_all_up(self):
        data = self.entry2.get()
    
    def replace_all_down(self):
        data = self.entry2.get()
    
    def replace_all(self):
        data = self.entry2.get()
    
    def replace_on(self):
        data = self.entry2.get()
    
    def finish_search(self):
        self.area.tag_delete('found')
        self.destroy()
    
    def go_next_found(self):
        self.area.mark_set_next('found', 'insert')
        self.area.see('insert')
    
    def go_prev_found(self):
        self.area.mark_set_prev('found', 'insert')
        self.area.see('insert')
    
if __name__ == '__main__':
    area = Tk()
    search_dialog = Search(area)
    area.mainloop()









