"""

Key-Commands
============

Namespace: anchors

"""
from vyapp.app import root

class Anchors:
    def __init__(self, area):
        area.add_mode('ANCHORS-JUMP')
        area.add_mode('ANCHORS-DROP')
        self.area = area

        area.install('anchors', 
        ('NORMAL', '<Key-x>', self.switch_jump),
        ('NORMAL', '<Key-X>', self.switch_drop),
        ('ANCHORS-DROP', '<Key>', self.drop),
        ('ANCHORS-JUMP', '<Key>', self.jump))

    def switch_jump(self, event):
        self.area.chmode('ANCHORS-JUMP')
        root.status.set_msg('Jump to:')

    def switch_drop(self, event):
        self.area.chmode('ANCHORS-DROP')
        root.status.set_msg('Drop on:')

    def drop(self, event):
        self.area.mark_set('(ANCHORS-%s)' % event.keysym, 'insert')
        self.area.chmode('NORMAL')
        index = self.area.index('insert')
        root.status.set_msg('Droped: (%s) at %s' % (event.keysym, index))

    def jump(self, event):
        self.area.seecur('(ANCHORS-%s)' % event.keysym)
        self.area.chmode('NORMAL')

install = Anchors