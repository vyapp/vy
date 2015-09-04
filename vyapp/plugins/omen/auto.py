"""

"""
from vyapp.plugins.omen.wordbox import Wordbox


def start_completion(area):
    wordbox = Wordbox(area)
    area.window_create('insert', {'window': wordbox})

def install(area):
    area.add_mode('INSERT_PYTHON', opt=True)
    area.install(('BETA', '<Key-m>', lambda event: event.widget.chmode('INSERT_PYTHON')), 
                 ('INSERT_PYTHON', '<F1>', lambda event: start_completion(event.widget)))


