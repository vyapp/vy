"""
Overview
========

Vy has a lot of modes that implement several kind of functionalities, like debuggers etc.
The python debugger has a lot of Key-Commands to set break points, make code run and other cool stuff.

Sometimes you will want to move the cursor around while in a mode that doesn't implement cursor movements, 
it is when this plugin will be useful.

Usage
=====

The NORMAL mode is in which a lot of useful Key-Commands are implemented.
There are tons of shortcuts to make the cursor jump around etc. Suppose
you are debugging a python application with pdb plugin, there are Key-Commands
to set break points, run code etc. 

The cursor movements aren't implemented in this pdb mode, one may need to move 
the cursor around while in the pdb mode that is when you generate the event <KeyPress-space> 
then vy will go to NORMAL mode as long you keep the key pressed.  Once you release 
it will go back to the previous mode in which it was in.

Switch to ALPHA mode by pressing <Key-3> in NORMAL mode, you will notice the ALPHA mode
being shown in the statusbar mode field. Then generate the event <KeyPress-space>
you will notice the statusbar mode field changing to NORMAL.
Once you release the key space it will change back to ALPHA mode.


Key-Commands
============

Mode: ALPHA, BETA, GAMMA, DELTA
Event: <KeyPress-space>
Description: Switch to one of the modes specified in modes.

Mode: NORMAL
Event: <KeyRelease-space>
Description: Goes back to the previous mode.

"""

class ToggleMode(object):    
    def __init__(self, area, target_mode='NORMAL', modes=['ALPHA', 'BETA', 'GAMMA', 'DELTA', 'PDB']):
        for ind in modes:
            area.hook(ind, '<KeyPress-space>', lambda event: self.switch_standard_mode(event.widget))
        area.hook(target_mode, '<KeyRelease-space>', lambda event: self.switch_previous_mode(event.widget))

        # It seems tkinter generates KeyRelease events together with KeyPress events.
        self.id = 1
        self.target_mode = target_mode

    def switch_standard_mode(self, area):
        self.id = area.id
        area.chmode(self.target_mode)

    def switch_previous_mode(self, area):
        area.chmode(self.id)

install = ToggleMode







