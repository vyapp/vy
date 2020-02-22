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

    def __init__(self, area, lhs, lhr):
        self.lhr  = lhr
        self.lhs  = lhs
        self.area = area

        self.tname = '(blink%s)' % id(self)
        self.area.tag_config(self.tname, **self.setup)

        self.id = self.area.hook('blink-pair', '-1', 
        '<FocusIn>', lambda e: self.blink())

        self.area.hook('blink-pair', '-1', '<FocusOut>', 
        lambda e: self.area.after_cancel(self.id))
        
    def blink(self):
        self.id = self.area.after(self.timeout, self.blink)

        index = self.area.case_pair('insert', 
        self.max, self.lhs, self.lhr)

        if self.area.tag_ranges(self.tname):
            self.area.tag_remove(self.tname,     
                'insert -%sc' % self.max, 'insert +%sc' % self.max)

        if index: self.area.tag_add(self.tname, 
            index, '%s +1c' % index)

install = BlinkPair
