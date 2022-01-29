from vyapp.app import root
from vyapp.plugins import Namespace

class CursorStatusNS(Namespace):
    pass

class CursorStatus:
    def __init__(self, area, timeout=1000):
        self.area    = area
        self.timeout = timeout
        self.funcid  = None
        area.install(CursorStatusNS, 
        (-1, '<FocusIn>', lambda event: self.update()),
        (-1, '<FocusOut>', lambda event: self.area.after_cancel(self.funcid)))

    def update(self):
        """
        It is used to update the line and col statusbar 
        in TIME interval.
        """
    
        row, col = self.area.indexsplit('insert')
        root.status.set_line(row)
        root.status.set_column(col)
        self.funcid = self.area.after(self.timeout, self.update)

install = CursorStatus

