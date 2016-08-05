"""

"""

from vyapp.tools import set_status_msg
from vyapp.exe import exec_quiet

class ModeShortcut(object):
    target_id  = 'NORMAL'
    DEFAULT_ID = 'NORMAL'

    def __init__(self, area):
        self.area = area
        area.install(('-1', '<Alt-n>',  lambda event: self.check_mode()))
                     
    def check_mode(self):
        if self.area.id == self.DEFAULT_ID:
            self.area.chmode(self.target_id)
        else:
            self.save_mode()
        return 'break'

    def save_mode(self):
        self.target_id = self.area.id
        self.area.chmode(self.DEFAULT_ID)

install = ModeShortcut

