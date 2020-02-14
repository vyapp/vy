"""
Overview
========

This plugin implements basic Key-Commands to open/save files.

Key-Commands
============

Namespace: io

Mode: NORMAL
Event: <Control-d>
Description: It pops a file selection window to load the contents of a file.

Mode: NORMAL
Event: <Control-s>
Description: It saves the content of the AreaVi instance into the opened file.

Mode: NORMAL
Event: <Shift-S>
Description: It pops a save file dialog to save the contents of the active AreaVi
instance with a different filename.

Mode: NORMAL
Event: <Key-I>
Description: Dump the contents of a file whose path is under the cursor line.

Mode: NORMAL
Event: <Key-N>
Description: Rename the current AreaVi file.

Mode: NORMAL
Event: <Control-Escape>
Description: Save and quit.

"""

# from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from vyapp.app import root
from vyapp.ask import Ask
import os

class IO:
    def __init__(self, area):
        self.area = area

        area.install('io', 
        ('NORMAL', '<Control-s>', self.save),
        ('NORMAL', '<Shift-S>', self.save_as),
        ('NORMAL', '<Control-d>', self.ask_and_load),
        ('NORMAL', '<Key-N>', self.rename),
        ('NORMAL', '<Key-I>', self.load_path),
        ('NORMAL', '<Control-Escape>', self.save_quit))
    
    def save_as(self, event):
        """
        It pops a asksaveasfilename window to save the contents of
        the text area.
        """
    
        filename = asksaveasfilename()
    
        if not filename: 
            return

        try:
            self.area.save_data_as(filename)
        except Exception:
            root.status.set_msg('It failed to save data.')
        else:
            root.status.set_msg('Data saved.')
            
    
    def save_quit(self, event):
        """
        It saves the contents of the text area then quits.
        """
    
        try:
            self.area.save_data()
        except Exception:
            root.status.set_msg('It failed to save data.')
        else:
            self.area.quit()
    
    def ask_and_load(self, event):
        """
        It pops a askopenfilename to find a file to drop
        the contents in the focused text area.
        """
    
        filename = askopenfilename()
    
        # If i don't check it ends up cleaning up
        # the text area when one presses cancel.
    
        if not filename: 
            return
    
        try:
            self.area.load_data(filename)
        except Exception:
            root.status.set_msg('It failed to load.')
        else:
            root.status.set_msg('File loaded.')
    
    
    def save(self, event):
        """
        It just saves the text area contents into the    
        actual opened file.
        """
    
        try:
            self.area.save_data()
        except Exception:
            root.status.set_msg('It failed to save data.')
        else:
            root.status.set_msg('Data saved.')
    
    def rename(self, event):
        """
        Rename the current AreaVi instance file.
        """

        root.status.set_msg('Type a filename:')
    
        ask = Ask()
        dir = os.path.dirname(self.area.filename)
        dst = os.path.join(dir, ask.data)
    
        try:
            os.rename(self.area.filename, dst)
        except OSError:
            root.status.set_msg('Failed to rename!')
        else:
            self.area.filename = dst
            root.status.set_msg('File renamed')
    
    def load_path(self, event):
        """
        Dump the contents of the file whose path is under the cursor.
        """
    
        filename = self.area.get_line()
        root.note.load([[filename]])
    

install = IO