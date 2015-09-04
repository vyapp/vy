"""

"""
from vyapp.plugins.omen.wordbox import Wordbox


def start_completion(area):
    area.after(100, lambda: Wordbox(area))

def install(area):
    area.add_mode('INSERT_PYTHON', opt=True)
    area.install(('BETA', '<Key-m>', lambda event: event.widget.chmode('INSERT_PYTHON')), 
                 ('INSERT_PYTHON', '<Key-period>', lambda event: start_completion(event.widget)))


