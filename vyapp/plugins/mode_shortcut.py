"""
Overview
========

Implement keycommands to pin a given mode and easily switch back to it.


Key-Commands
============

Namespace: mode-shortcut

Mode: GLOBAL
Event: <Alt-n>
Description: Pin the current mode.

Mode: GLOBAL
Event: <Alt-Escape>
Description: Switch to the previous pinned mode.

"""

from vyapp.app import root

class ModeShortcut(object):
    target_id  = 'NORMAL'
    DEFAULT_ID = 'NORMAL'

    def __init__(self, area):
        self.area = area
        area.install('mode-shortcut', ('-1', '<Alt-Escape>',  
        lambda event: self.area.chmode(self.target_id)),
        ('-1', '<Alt-n>',  lambda event: self.save_mode()))
                     
    def save_mode(self):
        self.target_id = self.area.id
        self.area.chmode(self.DEFAULT_ID)
        root.status.set_msg('Mode %s pinned!' % self.target_id)
        return 'break'

install = ModeShortcut









