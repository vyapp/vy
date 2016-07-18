class Anchors(object):
    def __init__(self, area):
        area.add_mode('ANCHORS')
        self.area  = area
        area.install(('NORMAL', '<Alt-b>', lambda event: area.chmode('ANCHORS')),
                     ('ANCHORS', '<Key>', self.drop_anchor))

    def drop_anchor(self, event):
        try:
            name = '(ANCHORS-%s)' % event.keysym
            pos0 = self.area.index(name)
        except Exception:
            self.area.mark_set(name, 'insert')
        else:
            if self.area.compare(pos0, '==', 'insert'):
                self.area.mark_unset(name)
            else:
                self.area.seecur(name)

        self.area.chmode('NORMAL')

install = Anchors


