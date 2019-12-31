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

    def create_process(self, args):
        self.expect = Expect(*args)

        # Note: The data has to be decoded using the area charset
        # because the area contents would be sometimes printed along
        # the debugging.
        xmap(self.expect, LOAD, lambda con, 
        data: sys.stdout.write(data.decode(self.area.charset)))

        # The expect has to be passed here otherwise when 
        # starting the new one gets terminated.

        xmap(self.expect, CLOSE, self.on_bkpipe)

        self.install_handles(self.expect)
        root.protocol("WM_DELETE_WINDOW", self.on_tk_quit)

    def on_bkpipe(self, expect):
        """
        On broken pipe.
        """
        expect.terminate()
        root.status.set_msg('Debugger: CLOSED!')

    def on_tk_quit(self):
        """
        Necessary otherwise the thread hangs.
        """
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
