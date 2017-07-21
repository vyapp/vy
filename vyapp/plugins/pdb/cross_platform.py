import vyapp.plugins.pdb.unix_platform
from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.network import xmap
from vyapp.plugins.pdb import event
from vyapp.app import root
import sys

__doc__ = vyapp.plugins.pdb.unix_platform.__doc__

class PdbEvents(event.PdbEvents):
    def __init__(self, dev, encoding='utf8'):
        xmap(dev, LOAD, self.handle_found)
        self.encoding = encoding

class Pdb(vyapp.plugins.pdb.unix_platform.Pdb):
    def __init__(self):
        vyapp.plugins.pdb.unix_platform.Pdb.__init__(self)

    def create_process(self, args):
        self.expect = Expect(*args)
        PdbEvents(self.expect, self.encoding)
        xmap(self.expect, LOAD, lambda con, data: sys.stdout.write(data))

        xmap(self.expect, 'LINE', self.handle_line)
        xmap(self.expect, 'DELETED_BREAKPOINT', self.handle_deleted_breakpoint)
        xmap(self.expect, 'BREAKPOINT', self.handle_breakpoint)
        xmap(self.expect, CLOSE, lambda expect: expect.destroy())

        def on_quit():
            self.kill_debug_process()
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_quit)

    def kill_debug_process(self):
        try:
            self.expect.terminate()
        except Exception:
            return

    def send(self, data):
        self.expect.send(data.encode(self.encoding))

pdb = Pdb()
install = pdb






