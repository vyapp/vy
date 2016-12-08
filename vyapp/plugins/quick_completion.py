"""

"""

from vyapp.widgets import CompletionWindow, Option
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.app import root
import sys

class WordCompletionWindow(CompletionWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):
        pattern     = area.get_seq()
        completions = map(lambda ind: ind[1][0], 
        area.find_all(root, '[^ ]*%s[^ ]*' % pattern 
        if pattern else '[^ ]+'))

        completions = set(completions)
        completions = map(lambda ind: 
        Option(ind), completions)

        CompletionWindow.__init__(self, area, 
        completions, *args, **kwargs)

def install(area):
    area.install(('INSERT', '<Control-q>', 
    lambda event: WordCompletionWindow(event.widget)))





