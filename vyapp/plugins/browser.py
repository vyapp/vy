from vyapp.app import root
from vyapp.areavi import AreaVi
from Tkinter import Frame

def go_left_area(area):
    map   = area.master.master.panes()
    count = map.index(str(area.master))
    count = count - 1
    wid   = area.nametowidget(map[count])
    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())
    
    # as there is only one.
    wid[0].focus_set()

def go_right_area(area):
    map   = area.master.master.panes()
    count = map.index(str(area.master))
    count = (count + 1) % len(map)
    wid   = area.nametowidget(map[count])
    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())
    
    # as there is only one.
    wid[0].focus_set()



def go_down_area(area):
    map   = area.master.master.panes()
    index = map.index(str(area.master))

    map   = area.master.master.master.panes()
    count = map.index(str(area.master.master))
    count = (count + 1) % len(map)

    wid   = area.nametowidget(map[count])
    size  = len(wid.panes())
    wid   = area.nametowidget(wid.panes()[index if index < size else (size - 1)])

    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())

    # as there is only one.
    wid[0].focus_set()



def go_up_area(area):
    map   = area.master.master.panes()
    index = map.index(str(area.master))

    map   = area.master.master.master.panes()
    count = map.index(str(area.master.master))
    count = count - 1

    wid   = area.nametowidget(map[count])
    size  = len(wid.panes())
    wid   = area.nametowidget(wid.panes()[index if index < size else (size - 1)])
    wid   = filter(lambda ind: isinstance(ind, AreaVi), wid.winfo_children())

    # as there is only one.
    wid[0].focus_set()




INSTALL =  [(-1, '<Shift-F9>', lambda event: root.note.scroll_left()),
            (-1, '<Shift-F10>', lambda event: root.note.scroll_right()),
            (-1, '<Left>', lambda event: go_left_area(event.widget)),
            (-1, '<Right>', lambda event: go_right_area(event.widget)),
            (-1, '<Up>', lambda event: go_up_area(event.widget)),
            (-1, '<Down>', lambda event: go_down_area(event.widget)),

            (-1, '<F9>', lambda event: root.note.select(root.note.index(root.note.select()) - 1)),
            (-1, '<F10>', lambda event: root.note.select(root.note.index(root.note.select()) + 1))]

def install(area):
    area.install(*INSTALL)

