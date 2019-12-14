from vyapp.plugins.pdb import unix_platform
from untwisted.expect import Expect, LOAD, CLOSE
from untwisted.network import xmap
from vyapp.app import root
import sys

__doc__ = unix_platform.__doc__

class Pdb(unix_platform.Pdb):
    def create_process(self, args):
        self.expect = Expect(*args)
        xmap(self.expect, CLOSE, lambda expect: expect.destroy())
        self.install_handles(self.expect)

        def on_quit():
            self.kill_process()
            root.destroy()
        root.protocol("WM_DELETE_WINDOW", on_quit)

    def kill_process(self):
        try:
            self.expect.terminate()
        except Exception:
            pass

        self.clear_breakpoints_map()

    def send(self, data):
        self.expect.send(data.encode(self.encoding))

pdb = Pdb()
install = pdb






