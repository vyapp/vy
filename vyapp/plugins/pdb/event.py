from untwisted.network import spawn, xmap
from untwisted.splits import Terminator
from re import search

class PdbEvents:
    def __init__(self, dev, encoding='utf8'):
        xmap(dev, Terminator.FOUND, self.handle_found)
        self.encoding = encoding

    def handle_found(self, dev, data):
        TABLE = {
                    '\> (?P<filename>.+)\((?P<line>[0-9]+)\)(?P<args>.+)':('LINE', ('filename', 'line', 'args')),
                    '\(Pdb\) Deleted breakpoint (?P<index>[0-9]+)':('DELETED_BREAKPOINT', ('index',)),
                    '\(Pdb\) Breakpoint (?P<index>[0-9]+) at (?P<filename>.+)\:(?P<line>[0-9]+)':('BREAKPOINT', ('index', 'filename', 'line'))
                }

        data = data.decode(self.encoding)    
        for regex, (event, groups) in TABLE.items():
            sch = search(regex, data)
            if not sch: continue
            spawn(dev, event, *sch.group(*groups))
            break
    











