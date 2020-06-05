"""
Overview
========


Commands
========


"""
from vyapp.areavi import AreaVi
from vyapp.app import root


class PaneJumps:
    def __init__(self, area):
        self.area = area

        area.install('splits', 
        (-1, '<Control-Alt-h>', self.jump_left),
        (-1, '<Control-Alt-l>', self.jump_right),
        (-1, '<Control-Alt-k>', self.jump_down),
        (-1, '<Control-Alt-j>', self.jump_up))

    def jump_left(self, event):
        wids  = self.area.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master))
        count = count - 1
        wid   = self.area.nametowidget(wids[count])
        wid   = [ind for ind in wid.winfo_children() 
            if isinstance(ind, AreaVi)]
        
        # as there is only one.
        wid[0].focus_set()
        return 'break'
    
    def jump_right(self, event):
        wids   = self.area.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master))
        count = (count + 1) % len(wids)
        wid   = self.area.nametowidget(wids[count])
        wid   = [ind for ind in wid.winfo_children() 
        if isinstance(ind, AreaVi)]
        
        # as there is only one.
        wid[0].focus_set()
        return 'break'
    
    def jump_down(self, event):
        wids   = self.area.master.master.panes()
        wids  = [str(item) for item in wids]
        index = wids.index(str(self.area.master))
    
        wids  = self.area.master.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master.master))
        count = (count + 1) % len(wids)
    
        wid   = self.area.nametowidget(wids[count])
        size  = len(wid.panes())
        wid   = self.area.nametowidget(wid.panes()[
            index if index < size else (size - 1)])
    
        wid   = [ind for ind in wid.winfo_children() 
        if isinstance(ind, AreaVi)]
    
        # as there is only one.
        wid[0].focus_set()
        return 'break'
    
    def jump_up(self, event):
        wids   = self.area.master.master.panes()
        wids  = [str(item) for item in wids]
        index = wids.index(str(self.area.master))
    
        wids  = self.area.master.master.master.panes()
        wids  = [str(item) for item in wids]
        count = wids.index(str(self.area.master.master))
        count = count - 1
    
        wid   = self.area.nametowidget(wids[count])
        size  = len(wid.panes())
        wid   = self.area.nametowidget(wid.panes()[
        index if index < size else (size - 1)])

        wid = [ind for ind in wid.winfo_children() 
        if isinstance(ind, AreaVi)]
    
        # as there is only one.
        wid[0].focus_set()
        return 'break'
    
install = PaneJumps
