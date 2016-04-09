"""
Overview
========

This plugin does autocompletion using jedi library.


Usage
=====

Whenever one presses <Control-Key-period> in INSERT mode
it should popup a window with possible completions.


Key-Commands
============

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.

"""

from vyapp.complete import CompleteWindow
from jedi import Script
from os.path import splitext
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

def show_window(event):
    event.widget.after(100, lambda: PythonCompleteWindow(event.widget))

def install(area):
    x = lambda event: area.hook('INSERT', '<Control-Key-period>', show_window, add=False)
    area.hook(-1, '<<Load-text/x-python>>', x, add=False)
    area.hook(-1, '<<Save-text/x-python>>', x, add=False)
    area.hook(-1, '<<LoadData>>', lambda event: area.unhook('INSERT', '<Control-Key-period>'))





