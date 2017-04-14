"""

Key-Commands
============

Namespace: anchors

"""

class Anchors(object):
    def __init__(self, area):
        area.add_mode('ANCHORS')
        self.area  = area
        area.install('anchors', ('NORMAL', '<Alt-b>', lambda event: area.chmode('ANCHORS')),
                     ('ANCHORS', '<Control-Key>', self.drop),
                     ('ANCHORS', '<Key>', self.jump))

    def drop(self, event):
        self.area.mark_set('(ANCHORS-%s)' % event.keysym, 'insert')
        self.area.chmode('NORMAL')

    def jump(self, event):
        self.area.seecur('(ANCHORS-%s)' % event.keysym)
        self.area.chmode('NORMAL')

install = Anchors





