from untwisted.network import spawn, xmap
from untwisted.splits import Terminator
from re import search
from re import split, escape

class RegexEvent:
    def __init__(self, spin, regstr, event, encoding='utf8'):
        self.encoding = encoding
        self.regstr   = regstr
        self.event    = event
        xmap(spin, Terminator.FOUND, self.handle_found)

    def handle_found(self, spin, data):
        data  = data.decode(self.encoding)
        regex = search(self.regstr, data)

        if regex: spawn(spin, 
            self.event, *regex.groups())

def build_regex(data, delim='.+'):
    """

    """

    data    = split(' +', data)
    pattern = ''
    for ind in range(0, len(data)-1):
        pattern = pattern + escape(data[ind]) + delim
    pattern = pattern + escape(data[-1])
    return pattern

def match_sub_pattern(pattern, lst):
    # pattern = buffer(pattern)
    for indi in lst:
        for indj in range(0, len(pattern)):
                if indi.startswith(pattern[indj:]):
                    yield indi, indj
                    
