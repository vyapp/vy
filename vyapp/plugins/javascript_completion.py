from vyapp.complete import CompleteWindow
from subprocess import Popen
import requests
import sys

class Tern(object):
    def __init__(self, area, port, path):
        self.port = port
        self.path = path

    def completions(self, data, line, col, filename):
        pass

class JavascriptCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        source      = self.area.get('1.0', 'end')
        line        = self.area.indcur()[0]
        size        = len(self.area.get('insert linestart', 'insert'))

        script      = Script(source, line, size, self.area.filename)
        completions = script.completions()

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)
        self.area.wait_window(self)

    def build(self, data):
        pass

    def make_request(self):
        pass

class JavascriptCompletion(object):
    def __init__(self, area, port, path):
        self.port = port
        self.path = path

        x = lambda event: area.hook('INSERT', '<Control-Key-period>', show_window, add=False)
        area.hook(-1, '<<Load-text/x-python>>', x, add=False)
        area.hook(-1, '<<Save-text/x-python>>', x, add=False)
        area.hook(-1, '<<LoadData>>', lambda event: area.unhook('INSERT', '<Control-Key-period>'))

    def show_window(event):
        event.widget.after(100, lambda: JavascriptCompleteWindow(event.widget))

install = Tern


