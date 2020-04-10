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
    timeout=2000
    pairs = ('(', ')'), ('[', ']'), ('{', '}')

    def __init__(self, area):
        area.tag_config('(BLINK)', **self.setup)

    @classmethod
    def scale(cls):
        loop = lambda: root.after(cls.timeout, cls.scale)
        root.after_idle(loop)
        area = root.focus_get()
        if isinstance(area, AreaVi):
            cls.blink(area)

    @classmethod
    def blink(cls, area):
        index0  = 'insert -%sc' % cls.max
        index1  = 'insert +%sc' % cls.max

        area.tag_remove('(BLINK)', index0, index1)
        for lhs, lhr in cls.pairs:
            index = area.case_pair('insert', cls.max, lhs, lhr)
            if index: 
                area.tag_add('(BLINK)', index, '%s +1c' % index)

install = BlinkPair
root.bind('<<Started>>', lambda event: BlinkPair.scale())