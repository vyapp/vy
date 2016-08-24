"""

"""


class ModeShortcut(object):
    target_id  = 'NORMAL'
    DEFAULT_ID = 'NORMAL'

    def __init__(self, area):
        self.area = area
        area.install(('-1', '<Alt-Escape>',  lambda event: self.area.chmode(self.target_id)),
        ('-1', '<Alt-n>',  lambda event: self.save_mode()))
                     
    def save_mode(self):
        self.target_id = self.area.id
        self.area.chmode(self.DEFAULT_ID)
        return 'break'

install = ModeShortcut






