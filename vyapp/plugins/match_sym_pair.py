"""
Overview
========

This plugin implements a mechanism to highligh pairs of ( ) [ ] { }.


"""

class MatchSymPair(object):
    def __init__(self, area, setup={'background':'pink', 
            'foreground':'black'}, max=1500, timeout=500):
        self.max     = max
        self.timeout = timeout
        self.area    = area

        area.tag_config('(paren)', **setup)
        area.tag_config('(bracket)', **setup)
        area.tag_config('(brace)', **setup)

        self.blink('(paren)', ('(', ')'))
        self.blink('(bracket)', ('[', ']'))
        self.blink('(brace)', ('{', '}'))
    
    def blink(self, name, args):
        self.area.after(self.timeout, self.blink, name, args)
        index = self.area.case_pair('insert', self.max, *args)

        self.area.tag_remove(name, '1.0', 'end')
        if not index: return
        self.area.tag_add(name, 'insert', 'insert +1c')
        self.area.tag_add(name, index, '%s +1c' % index)



install = MatchSymPair






