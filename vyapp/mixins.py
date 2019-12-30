from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.wrappers import xmap
from os.path import abspath
from vyapp.areavi import AreaVi
from vyapp.app import root
import sys

class DAP:
    """
    Debugger adapter pattern.

    This class makes it simple to implement new debuggers in vy.
    It follows a specific approach that is not necessarily strict.

    It makes usage of Untwisted Framework's usage to implement its basic
    logic.
    """
    
    setup={'background':'blue', 'foreground':'yellow'}
    encoding='utf8'

    def __init__(self):
        self.expect  = None

        self.map_index = dict()
        self.map_line  = dict()

    def create_process(self, args):
        self.expect = Expect(*args)

        # Note: The data has to be decoded using the area charset
        # because the area contents would be sometimes printed along
        # the debugging.
        xmap(self.expect, LOAD, lambda con, 
        data: sys.stdout.write(data.decode(self.area.charset)))

        xmap(self.expect, CLOSE, self.on_close)
        self.install_handles(self.expect)
        root.protocol("WM_DELETE_WINDOW", self.on_quit)

    def on_close(self, expect):
        self.expect.terminate()
        root.status.set_msg('Debugger: CLOSED!')

    def on_quit(self):
        self.expect.terminate()
        root.destroy()

    def quit_db(self, event):
        self.kill_process()
        event.widget.chmode('NORMAL')

    def run(self, event):
        """
        To be implemented.
        """

    def run_args(self, event):
        """
        To be implemented.
        """

    def kill_process(self):
        if self.expect:
            self.expect.terminate()

    def install_handles(self, device):
        """
        This method is meant to be implemented. It is supposed to 
        extract necessary attributes from the underlying debugger output
        to be dispatched to these methods: 

        Debugger has hit a given line:

            self.handle_line
    
        """

    def handle_line(self, device, filename, line):
        """
    
        """
        filename = abspath(filename)

        wids = AreaVi.get_opened_files(root)
        area = wids.get(filename)

        if area: root.note.set_line(area, line)
        area.tag_delete('(DebuggerBP)')
        area.tag_add('(DebuggerBP)', '%s.0 linestart' % line, '%s.0 lineend' % line)
        area.tag_config('(DebuggerBP)', **self.setup)
        root.status.set_msg('Debugger  stopped at: %s:%s' % (filename, line))
    

    def send(self, data):
        """
        To implement:

        Example:
            self.expect.send(data.encode(self.encoding))

        """

class Echo:
    """

    """

    def __init__(self, area):
        self.area = area
        self.bind('<BackSpace>', self.on_backspace)
        self.bind('<Key>', self.dispatch)

    def dispatch(self, event):
        if event.char:  
            self.on_char(event.char)

    def on_char(self, char):
        self.area.insert('insert', char)

    def on_backspace(self, event):
        self.area.delete('insert -1c', 'insert')
        self.on_delete(event)

    def on_delete(self, event):
        pass
