from vyapp.app import root
from vyapp.areavi import AreaVi


def get_area_tab_index(area):
    return area.master.master.master

def set_line(area, line):
    from vyapp.app import root
    import sys
    sys.stderr.write(area.filename + '\n')
    root.note.select(get_area_tab_index(area))
    area.focus()
    area.inset('%s.0' % int(line))
    area.seecur()

def set_status_msg(msg):
    from vyapp.app import root
    root.status.set_msg(msg)

def set_status_line(line):
    from vyapp.app import root
    root.status.set_line(line)

def set_status_col(col):
    from vyapp.app import root
    root.status.set_column(col)

def set_status_mode(mode):
    from vyapp.app import root
    root.status.set_mode(mode)




