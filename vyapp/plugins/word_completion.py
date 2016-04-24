from vyapp.complete import CompleteWindow
from jedi import Script
from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
import sys

class WordCompleteWindow(CompleteWindow):
    """
    """

    def __init__(self, area, *args, **kwargs):

        CompleteWindow.__init__(self, area, completions, *args, **kwargs)

def install(area):
    trigger = lambda event: area.hook('INSERT', '<Control-Key-period>', 
                        lambda event: WordCompleteWindow(event.widget), add=False)

    area.install((-1, '<<LoadData>>', trigger), (-1, '<<SaveData>>', trigger))


