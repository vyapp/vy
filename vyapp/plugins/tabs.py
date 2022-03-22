"""
Overview
========

Tabs are a great feature when manipulating several files. This plugin implements Key-Commands to create, 
open files, change the focus between opened tabs.

Key-Commands
============

Namespace: tabs

Mode: EXTRA
Event: <Key-comma>
Description: It pops a file selection window to load the contents of a file in a new tab.

Mode: EXTRA
Event: <Key-period>
Description: It creates a new blank tab.

Mode: EXTRA
Event: <Alt-x>
Description: It removes the focused tab.

Mode: Global
Event: <Alt-o>
Description: It changes the focus left from a tab.

Mode: Global
Event: <Alt-p>
Description: It changes the focus right from a tab.

"""

from vyapp.app import root
# from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from vyapp.plugins import Namespace

class TabsNS(Namespace):
    pass

class Tabs:
    def __init__(self, area):
        self.area = area

        area.install(TabsNS, 
        (-1, '<Alt-E>', self.load_tab),
        (-1, '<Alt-R>', self.create_tab),
        (-1, '<Alt-x>', self.remove_tab),
        (-1, '<Alt-o>', self.select_left),
        (-1, '<Alt-p>', self.select_right))

    def load_tab(self, event):
        """
        It pops a askopenfilename window to drop
        the contents of a file into another tab's text area.
        """
    
        filename = askopenfilename()
    
        # If i don't check it ends up cleaning up
        # the text area when one presses cancel.
    
        if not filename: 
            return 'break'
    
        try:
            root.note.load([[filename]])
        except Exception:
            root.status.set_msg('It failed to load.')
        else:
            root.status.set_msg('File loaded.')
        self.area.chmode('NORMAL')
        return 'break'

    def create_tab(self, event):
        root.note.create('none')
        self.area.chmode('NORMAL')
        return 'break'
    
    def remove_tab(self, event):
        """
        It removes the selected tab.
        """
    
        tabs = root.note.tabs() 
        count = len(tabs) 

        if count <= 1: 
            return None

        name = root.note.select()
        wid  = root.note.nametowidget(name)
        wid.destroy()
        root.note.select(0)
        root.note.set_area_focus()
    
        # We don't need to call forget after destroy.
        # It seems the method forget from note doesnt destroy
        # the widget at all consequently the event <Destroy> isn't
        # spreaded.
        # root.note.forget(wid)
        return 'break'
    
    def select_left(self, event):
        """
        """
    
        root.note.select(root.note.index(root.note.select()) - 1)
        root.note.set_area_focus()
        return 'break'
    
    def select_right(self, event):
        """
        """
    
        root.note.select(root.note.index(root.note.select()) + 1)
        root.note.set_area_focus()
        return 'break'
    
install = Tabs