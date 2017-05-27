"""
Overview
========

This plugin does autocompletion using jedi library.


Key-Commands
============

Namespace: python-completion

Mode: INSERT
Event: <Control-Key-period>
Description: Open the completion window with possible python words for
completion.

"""

from vyapp.completion import CompletionWindow
from jedi import Script
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
import sys

class PythonCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        source      = area.get('1.0', 'end')
        line, col   = area.indcur()
        script      = Script(source, line, col, area.filename)
        completions = script.completions()
        CompletionWindow.__init__(self, area, completions, *args, **kwargs)
        self.bind('<F1>', lambda event: sys.stdout.write('%s\n%s\n' % ('#' * 80, self.box.selection_docs())))

def install(area):
    trigger = lambda event: area.hook('python-completion', 'INSERT', '<Control-Key-period>', 
                        lambda event: PythonCompletionWindow(event.widget), add=False)
    remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')

    area.install('python-completion', (-1, '<<Load/*.py>>', trigger), (-1, '<<Save/*.py>>', trigger),
                 (-1, '<<LoadData>>', remove_trigger), (-1, '<<SaveData>>', remove_trigger))

def active_python_completion():
    AreaVi.ACTIVE.hook('INSERT', '<Control-Key-period>', 
                  lambda event: PythonCompletionWindow(event.widget), add=False)

ENV['active_python_completion'] = active_python_completion


