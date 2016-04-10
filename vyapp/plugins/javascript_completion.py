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

    def build(self, data):
        pass

class JavascriptCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, tern, area, *args, **kwargs):
        source      = self.area.get('1.0', 'end')
        line        = self.area.indcur()[0]
        size        = len(self.area.get('insert linestart', 'insert'))
        completions = tern.completions(source, line, size, area.filename)

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)

class JavascriptCompletion(object):
    def __init__(self, area, port, path):
        self.tern = Tern(port, path)

        trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                  lambda event: JavascriptCompleteWindow(self.tern, event.widget), add=False)

        area.install((-1, '<<Load-text/x-python>>', trigger),
        (-1, '<<Save-text/x-python>>', trigger), (-1, '<<LoadData>>', lambda event: 
                                      area.unhook('INSERT', '<Control-Key-period>')))

install = JavascriptCompletion



