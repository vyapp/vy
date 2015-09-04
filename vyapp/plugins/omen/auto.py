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
from vyapp.plugins.omen.utils import PythonCompleteWindow
from os.path import splitext

def check_file_extension(area):
    filename, extension = splitext(area.filename)
    extension           = extension.lower()

    if extension == '.py':
        area.hook('INSERT', '<Control-Key-period>', 
                  lambda event: show_window_completion(event.widget))
    else:
        area.unhook('INSERT', '<Control-Key-period>')
    
def show_window_completion(area):
    area.after(100, lambda: PythonCompleteWindow(area))

def install(area):
    area.hook(-1, '<<LoadData>>', lambda event: check_file_extension(event.widget))
    area.hook(-1, '<<SaveData>>', lambda event: check_file_extension(event.widget))







