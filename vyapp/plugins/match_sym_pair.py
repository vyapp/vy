"""
Overview
========

This plugin implements a mechanism to highligh pairs of ( ) [ ] { }.


"""
from vyapp.areavi import AreaVi
from vyapp.app import root

class MatchSymPair:
    setup={'background':'pink', 
   'foreground':'black'}
    max=1500
    timeout=1000

    def __call__(self, area):
        area.tag_config('(paren)', **self.setup)
        area.tag_config('(bracket)', **self.setup)
        area.tag_config('(brace)', **self.setup)

    def __init__(self):
        # root.bind('<<Started>>', self.install_handles, once=True)
        root.bind('<<Started>>', self.install_handles)

    def install_handles(self, event):
        self.blink('(paren)', ('(', ')'))
        self.blink('(bracket)', ('[', ']'))
        self.blink('(brace)', ('{', '}'))
    
    def blink(self, name, args):
        root.after(self.timeout, self.blink, name, args)
        if not AreaVi.INPUT: return

        index = AreaVi.INPUT.case_pair('insert', self.max, *args)
        AreaVi.INPUT.tag_remove(name, 
        'insert -%sc' % self.max, 'insert +%sc' % self.max)

        if not index: return
        AreaVi.INPUT.tag_add(name, 'insert', 'insert +1c')
        AreaVi.INPUT.tag_add(name, index, '%s +1c' % index)

install = MatchSymPair()
