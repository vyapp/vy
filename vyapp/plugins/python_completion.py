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
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
import sys

class PythonCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()
        script      = Script(source, line, col, area.filename)
        completions = script.completions()

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)
        self.bind('<F1>', lambda event: sys.stdout.write('%s\n%s\n' % ('#' * 80, self.box.elem_desc())))

def install(area):
    trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                        lambda event: PythonCompleteWindow(event.widget), add=False)
    remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')

    area.install((-1, '<<Load-text/x-python>>', trigger), (-1, '<<Save-text/x-python>>', trigger),
                 (-1, '<<LoadData>>', remove_trigger), (-1, '<<SaveData>>', remove_trigger))

def active_python_completion():
    AreaVi.ACTIVE.hook('INSERT', '<Control-Key-period>', 
                  lambda event: PythonCompleteWindow(event.widget), add=False)

ENV['active_python_completion'] = active_python_completion





