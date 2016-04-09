from vyapp.complete import CompleteWindow
from jedi import Script
import sys

class PythonCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        self.area = area

        source      = self.area.get('1.0', 'end')
        line        = self.area.indcur()[0]
        size        = len(self.area.get('insert linestart', 'insert'))
        script      = Script(source, line, size, self.area.filename)
        completions = script.completions()

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)
        self.bind('<F1>', lambda event: sys.stdout.write('%s\n%s\n' % ('#' * 80, self.box.elem_desc())))

        self.area.wait_window(self)



