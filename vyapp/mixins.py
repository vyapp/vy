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

    def start_debug(self, event):
        """
        To be implemented.
        """

    def start_debug_args(self, event):
        """
        To be implemented.
        """

    def kill_process(self):
        if self.expect:
            self.expect.terminate()
        self.clear_breakpoints_map()

    def install_handles(self, device):
        """
        This method is meant to be implemented. It is supposed to 
        extract necessary attributes from the underlying debugger output
        to be dispatched to these methods: 

        Debugger has hit a given line:

            self.handle_line
    
        A given breakpoint was removed:

            self.handle_deleted_breakpoint 

        A breakpoint was added:

            self.handle_breakpoint.
        """

    def clear_breakpoints_map(self):
        """
        It deletes all added breakpoint tags.
        It is useful when restarting pdb as a different process.
        """

        items = self.map_index.items()
        for index, (filename, line) in items:
            self.del_breakpoint(filename, index)

        self.map_index.clear()
        self.map_line.clear()

    def get_breakpoint_name(self, filename, line):
        filename = abspath(filename)
        return self.map_line[(filename, line)]

    def del_breakpoint(self, filename, index):
        filename = abspath(filename)
        widgets = AreaVi.get_opened_files(root)
        area    = widgets.get(filename)
        if area: area.tag_delete('_breakpoint_%s' % index)

    def handle_line(self, device, filename, line):
        """
    
        """
        filename = abspath(filename)

        wids = AreaVi.get_opened_files(root)
        area = wids.get(filename)

        if area: root.note.set_line(area, line)
    
    def handle_deleted_breakpoint(self, device, index):
        """
        When a break point is removed.
        """

        filename, line = self.map_index[index]
        self.del_breakpoint(filename, index)

    def handle_breakpoint(self, device, index, filename, line):
        """
        When a break point is added.
        """
        filename = abspath(filename)
        self.map_index[index]           = (filename, line)
        self.map_line[(filename, line)] = index

        map  = AreaVi.get_opened_files(root)
        area = map[filename]
        NAME = '_breakpoint_%s' % index

        area.tag_add(NAME, '%s.0 linestart' % line, '%s.0 lineend' % line)
        area.tag_config(NAME, **self.setup)

    def send(self, data):
        """
        To implement:

        Example:
            self.expect.send(data.encode(self.encoding))

        """