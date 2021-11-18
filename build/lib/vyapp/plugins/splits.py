"""
Overview
========

Panels are a cool way to perform some tasks. This plugin implements Key-Commands to create horizontal/vertical
panes.

Key-Commands
============

Namespace: splits

Mode: Global
Event: <Alt-less>
Description: Add a vertical pane.

Mode: Global
Event: <Alt-greater>
Description: Add a horizontal pane.

Mode: Global
Event: <Alt-X> 
Description: Remove a pane.

"""

from vyapp.app import root

class Splits:
    def __init__(self, area):
        self.area = area

        area.install('splits', 
        (-1, '<Alt-V>',  self.add_horizontal_area),
        (-1, '<Alt-C>', self.add_vertical_area),
        (-1, '<Alt-X>', self.remove_area))
    
    def add_vertical_area(self, event):
        """
        It opens a vertical area.
        """
    
        vpane = self.area.master.master.master
        vpane.create()
    
        wids  = vpane.panes()
        height = root.winfo_height()//(len(wids) + 1)
        root.update()
    
        for ind in range(0, len(wids) - 1):
            vpane.sash_place(ind,  0,  (ind + 1) * height)
        # self.area.chmode('EXTRA')
        return 'break'

    def add_horizontal_area(self, event):
        """
        It creates a new horizontal area.
        """
    
        hpane = self.area.master.master
        hpane.create()
    
        wids  = hpane.panes()
        width = root.winfo_width()//(len(wids) + 1)
        root.update()
    
        for ind in range(0, len(wids) - 1):
            hpane.sash_place(ind,  (ind + 1) * width,  0)
        # self.area.chmode('EXTRA')
        return 'break'
    
    def remove_area(self, event):
        """
        It removes the focused area.
        """
    
        vpanes = len(self.area.master.master.master.panes())
        hpanes = len(self.area.master.master.panes())
    
        if vpanes == 1 and hpanes == 1: return
        self.area.master.destroy()
    
        if not self.area.master.master.panes(): 
            self.area.master.master.destroy()
    
        root.note.restore_area_focus()
        # self.area.chmode('EXTRA')
        return 'break'
    
install = Splits