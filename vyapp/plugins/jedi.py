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
from vyapp.plugins import Command

class PythonCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        source      = area.get('1.0', 'end')
        line, col   = area.indexref()
        script      = Script(source, line, col, area.filename)
        completions = script.completions()
        CompletionWindow.__init__(self, area, completions, *args, **kwargs)

def install(area):
    trigger = lambda event: area.hook('python-completion', 
    'INSERT', '<Control-Key-period>', lambda event: PythonCompletionWindow(
    event.widget), add=False)

    remove_trigger = lambda event: area.unhook('INSERT', '<Control-Key-period>')

    area.install('jedi', (-1, '<<Load/*.py>>', trigger), 
    (-1, '<<Save/*.py>>', trigger), (-1, '<<LoadData>>', remove_trigger), 
    (-1, '<<SaveData>>', remove_trigger))

@Command()
def acp(area):
    """
    Activate python completion when file extension is not 
    detected automatically.
    """
    area.hook('jedi', 'INSERT', '<Control-Key-period>', 
    lambda event: PythonCompletionWindow(event.widget), add=False)








