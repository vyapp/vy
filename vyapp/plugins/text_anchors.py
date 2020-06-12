"""

Key-Commands
============

Namespace: anchors

"""
from vyapp.app import root
from tkinter import TclError

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
        index = self.area.index('insert')
        root.status.set_msg('Droped: (%s) at %s' % (event.keysym, index))
        self.area.chmode('NORMAL')

    def jump(self, event):
        index = '(ANCHORS-%s)' % event.keysym

        try:
            self.area.seecur(index)
        except TclError as error:
            root.status.set_msg('Bad index: (%s)' % event.keysym)
        else:
            root.status.set_msg('Jumped: (%s)' % event.keysym)
        self.area.chmode('NORMAL')

install = Anchors