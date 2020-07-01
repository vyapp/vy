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
    max=1000
    pairs = ('(', ')'), ('[', ']'), ('{', '}')

    def __init__(self, area):
        area.tag_config('(BLINK)', **self.setup)
        self.area = area
        area.bind('<<Idle>>', self.blink, add=True)

    def blink(self, event):
        index0  = 'insert -%sc' % self.max
        index1  = 'insert +%sc' % self.max

        self.area.tag_remove('(BLINK)', index0, index1)
        for lhs, lhr in self.pairs:
            index = self.area.case_pair('insert', self.max, lhs, lhr)
            if index: 
                self.area.tag_add('(BLINK)', index, '%s +1c' % index)

install = BlinkPair