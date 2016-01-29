from vyapp.tools import set_status_mode
from vyapp.tools import set_status_line
from vyapp.tools import set_status_col
from vyapp.tools import set_status_msg
from vyapp.tools import get_area_tab_index
from vyapp.app import root
from os.path import basename

TIME = 1000

def update_mode(area):
    """
    It is used to update the mode status bar 
    in TIME interval.
    """

    def cave():
        if not cave.keep: return
        set_status_mode(area.id)
        area.after(TIME, cave)

    """
    The cave function is used
    to update the status bar.

    When the AreaVi loses focus it sets cave.keep to False then
    cave no more calls after.
    It may be interesting to call 
    
    area.after_idle.
    """

    cave.keep = True
    cave()
    def stop(): cave.keep = False
    area.hook(-1, '<FocusOut>', lambda event: stop())
    
def update_cursor_pos(area):
    """
    It is used to update the line and col statusbar 
    in TIME interval.
    """

    def cave():
        if not cave.keep: return
        row, col = area.indref('insert')
        set_status_line(row)
        set_status_col(col)
        area.after(TIME, cave) 

    """
    The scheme is basically the same as in 
    update_mode.
    It may be interesting to call 
    
    area.after_idle.
    """

    cave.keep = True
    cave()
    def stop(): cave.keep = False
    area.hook(-1, '<FocusOut>', lambda event: stop())


def install(area):
    area.install((-1, '<FocusIn>', lambda event: update_mode(event.widget)),
           (-1, '<FocusIn>', lambda event: update_cursor_pos(event.widget)),
           (-1, '<Control-F9>', lambda event: root.status.switch()),
           (-1, '<Escape>', lambda event: set_status_msg('')),

           (-1, '<<SaveData>>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<<LoadData>>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<<ClearData>>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<FocusIn>', lambda event: root.title('Vy %s' % event.widget.filename)),

           (-1, '<<SaveData>>', lambda event: root.note.tab(get_area_tab_index(event.widget), text=basename(event.widget.filename))),
           (-1, '<<LoadData>>', lambda event: root.note.tab(get_area_tab_index(event.widget), text=basename(event.widget.filename))),
           (-1, '<<ClearData>>', lambda event: root.note.tab(get_area_tab_index(event.widget), text=basename(event.widget.filename))),
           (-1, '<FocusIn>', lambda event: root.note.tab(root.note.select(), text=basename(event.widget.filename))))



