
class QuickJumps(object):
    def __init__(self, area):
        self.area  = area
        area.install(('NORMAL', '<Key-m>', lambda event: self.area.mark_set('(PREV_POSITION)', 'insert')),
                     ('NORMAL', '<Key-n>', lambda event: self.area.mark_set('(PREV_POSITION)', 'insert')),
                     ('NORMAL', '<Key-i>', lambda event: self.area.mark_set('(PREV_POSITION)', 'insert')),
                     ('NORMAL', '<BackSpace>', lambda event: self.area.seecur('(PREV_POSITION)')))

install = QuickJumps
