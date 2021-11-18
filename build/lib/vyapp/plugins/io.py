"""
Overview
========

This plugin implements basic Key-Commands to open/save files.

Key-Commands
============

Namespace: io

Mode: EXTRA
Event: <Key-c>
Description: It pops a file selection window to load the contents of a file.

Mode: EXTRA
Event: <Key-s>
Description: It saves the content of the AreaVi instance into the opened file.

Mode: EXTRA
Event: <Key-a>
Description: It pops a save file dialog to save the contents of the active AreaVi
instance with a different filename.

Mode: EXTRA
Event: <Key-n>
Description: Rename the current AreaVi file.

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
        (-1, '<Alt-S>', self.save),
        (-1, '<Alt-A>', self.save_as),
        (-1, '<Alt-D>', self.ask_and_load),
        ('EXTRA', '<Key-n>', self.rename))
    
    def save_as(self, event):
        """
        It pops a asksaveasfilename window to save the contents of
        the text area.
        """
    
        filename = asksaveasfilename()
    
        if not filename: 
            return 'break'

        try:
            self.area.save_data_as(filename)
        except Exception:
            root.status.set_msg('It failed to save data.')
        else:
            root.status.set_msg('Data saved.')
        self.area.chmode('NORMAL')
        return 'break'
        
    def ask_and_load(self, event):
        """
        It pops a askopenfilename to find a file to drop
        the contents in the focused text area.
        """
    
        filename = askopenfilename()
    
        # If i don't check it ends up cleaning up
        # the text area when one presses cancel.
    
        if not filename: 
            return 'break'
    
        try:
            self.area.load_data(filename)
        except Exception:
            root.status.set_msg('It failed to load.')
        else:
            root.status.set_msg('File loaded.')
        return 'break'
    
    
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
        self.area.chmode('NORMAL')
        return 'break'
    
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
        self.area.chmode('NORMAL')
        return 'break'
    

install = IO