"""
Overview
========

Implement keycommands to pin a given mode and easily switch back to it.
It is interesting to be used with modes like PDB etc.

Key-Commands
============

Namespace: mode-shortcut

Mode: GLOBAL
Event: <Alt-g>
Description: Pin the current mode.

Mode: NORMAL
Event: <Key-g>
Description: Switch to the previous pinned mode.

"""

from vyapp.app import root

class ModeShortcut(object):
    target_id  = 'NORMAL'

    def __init__(self, area):
        self.area = area
        area.install('mode-shortcut', ('NORMAL', '<Key-g>',  
        lambda event: self.area.chmode(self.target_id)),
        ('-1', '<Alt-g>',  lambda event: self.save_mode()))
                     
    def save_mode(self):
        self.target_id = self.area.id
        self.area.chmode('NORMAL')
        root.status.set_msg('Mode %s pinned!' % self.target_id)
        return 'break'

install = ModeShortcut











