from vyapp.ask import Ask
from vyapp.tools import set_status_msg
from itertools import permutations, product
from re import escape

class ISearch(object):
    def __init__(self, area):
        """

        """
        self.REGX = '.+?'
        area.add_mode('ISEARCH')
        area.install(('NORMAL', '<Key-0>', lambda event: self.set_data(event.widget)),
                        ('ISEARCH', '<Key-j>', lambda event: self.go_down(event.widget)),
                        ('ISEARCH', '<Key-k>', lambda event: self.go_up(event.widget)))


        self.seq   = []
        self.index = 0

    def set_data(self, area):
        """

        """

        self.seq   = []
        self.index = 0
        ask        = Ask(area)

        area.chmode('ISEARCH')

        seq = self.create_perm(ask.data.split(' '))
        for ind in seq:
            for ch, index0, index1 in area.find(ind[:-3], '1.0'):
                self.seq.append((index0, index1))

        if not self.seq:
            set_status_msg('No pattern found!')
        else:
            self.go_down(area)
    
    def create_prod(self, data):
        prod = product(data, (self.REGX, ))
        for ind in prod:
            yield ''.join(ind)


    def create_perm(self, data):    
        seq  = self.create_prod(data)
        seq  = permutations(seq)
        for ind in seq:
            yield ''.join(ind) 

    def go_up(self, area):
        """

        """

        if not self.seq: return
        pos0, pos1 = self.seq[self.index - 1]
        area.tag_add('sel', pos0, pos1)
        area.inset(pos1)
        area.see('insert')

        if self.index > 1: self.index = self.index - 1



    def go_down(self, area):
        """

        """
        if not self.seq: return
        pos0, pos1 = self.seq[self.index]

        area.tag_add('sel', pos0, pos1)
        area.inset(pos1)
        area.see('insert')
        if self.index < len(self.seq) - 1: self.index = self.index + 1

install = ISearch






