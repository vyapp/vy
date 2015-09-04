"""

"""
from vyapp.plugins.omen.wordbox import Wordbox
from os.path import splitext

def check_file_extension(area):
    filename, extension = splitext(area.filename)
    extension           = extension.lower()

    if extension == '.py':
        area.hook('INSERT', '<Key-period>', 
                  lambda event: show_window_completion(event.widget))
    else:
        area.unhook('INSERT', '<Key-period>')
    
def show_window_completion(area):
    area.after(100, lambda: Wordbox(area))

def install(area):
    area.hook(-1, '<<LoadData>>', lambda event: check_file_extension(event.widget))



