"""
This module implements basic input data scheme.
"""

from Tkinter import *
from vyapp.app import root

class Ask(Entry):
    """
    This class implements vy default input text scheme. Plugins that demand user input
    could use this class to retrieve user's data in a consistent way. When this class constructor
    is called it shows an entry widget at the bottom of the vy editor.

    This widget takes the focus when the constructor is called. It is a useful
    behavior in the common scenaries of vy editor.

    When user presses <Escape> the widget is destroyed and the focus scheme
    is restored. The same occurs when <Return> is pressed while the widget has focus.

    Consider:
    
    def handle(area):
        ask = Ask(area)
        if ask.data:
            print 'Success!'
        else:
            print 'Failure!'

    In case of success it is if the user pressed <Return> then ask.data will be the user data
    that was inputed otherwise it is ''.
    """

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


