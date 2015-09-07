from jedi import Script
from vyapp.complete import CompleteWindow

class PythonCompleteWindow(CompleteWindow):
    """
    Inherits from CompleteWindow then reimplements feed.
    That is enough to have a window completion to complete stuff :P
    """

    def __init__(self, area, *args, **kwargs):
        self.area = area
        CompleteWindow.__init__(self, area, *args, **kwargs)

    def feed(self):
        source      = self.area.get('1.0', 'end')
        line        = self.area.indcur()[0]
        size        = len(self.area.get('insert linestart', 'insert'))
        script      = Script(source, line, size, self.area.filename)
        completions = script.completions()

        for ind in completions:
            self.box.insert('end', ind.name)

