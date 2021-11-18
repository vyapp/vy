"""
Overview
========


Commands
========


"""


class PaneResize:
    def __init__(self, area):
        self.area = area
        
        area.install('pane-resize', 
        ('EXTRA', '<Control-h>', self.dec_vsash),
        ('EXTRA', '<Control-l>', self.inc_vsash),
        ('EXTRA', '<Control-k>', self.dec_hsash),
        ('EXTRA', '<Control-j>', self.inc_hsash))


    def dec_vsash(self, event):
        wids  = self.area.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master))
        count = count - 1 if count > 0 else 0

        pos = self.area.master.master.sash_coord(count)
        self.area.master.master.sash_place(count, pos[0] - 15, 0)

    def inc_vsash(self, event):
        wids  = self.area.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master))
        count = count - 1 if count > 0 else 0

        pos = self.area.master.master.sash_coord(count)
        self.area.master.master.sash_place(count, pos[0] + 15, 0)

    def dec_hsash(self, event):
        wids  = self.area.master.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master.master))
        count = count - 1 if count > 0 else 0
        pos = self.area.master.master.master.sash_coord(count)
        self.area.master.master.master.sash_place(count, 0, pos[1] - 15)

    def inc_hsash(self, event):
        wids  = self.area.master.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master.master))
        count = count - 1 if count > 0 else 0

        pos = self.area.master.master.master.sash_coord(count)
        self.area.master.master.master.sash_place(count, 0, pos[1] + 15)


install = PaneResize