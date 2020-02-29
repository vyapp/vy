"""
Overview
========

This plugin implements a mechanism to highligh pairs of ( ) [ ] { }.


"""
from vyapp.areavi import AreaVi
from vyapp.app import root

class BlinkPair:
    setup={'background':'pink', 
   'foreground':'black'}
    max=1500
    timeout=1000

    def __init__(self, area, *pairs):
        self.pairs = pairs
        self.area  = area

        self.area.tag_config('(BLINK)', **self.setup)
        self.id = self.area.hook('blink-pair', '-1', 
        '<FocusIn>', lambda e: self.scale())

        self.area.hook('blink-pair', '-1', '<FocusOut>', 
        lambda e: self.area.after_cancel(self.id))
        
    def scale(self):
        self.id = self.area.after(self.timeout, self.scale)
        index0  = 'insert -%sc' % self.max
        index1  = 'insert +%sc' % self.max

        if self.area.tag_ranges('(BLINK)'):
            self.area.tag_remove('(BLINK)', index0, index1)
        for lhs, lhr in self.pairs:
            index = self.area.case_pair(
                'insert', self.max, lhs, lhr)
            if index: self.area.tag_add(
                '(BLINK)', index, '%s +1c' % index)

install = BlinkPair
