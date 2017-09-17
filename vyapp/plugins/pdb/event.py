from untwisted.network import spawn, xmap
from untwisted.splits import Terminator
from re import search

class PdbEvents:
    def __init__(self, dev, encoding='utf8'):
        xmap(dev, Terminator.FOUND, self.handle_found)
        self.encoding = encoding

    def handle_found(self, dev, data):
        TABLE = {
        '\> (.+)\(([0-9]+)\)(.+)':'LINE',
        '\(Pdb\) Deleted breakpoint ([0-9]+)':'DELETED_BREAKPOINT',
        '\(Pdb\) Breakpoint ([0-9]+) at (.+)\:([0-9]+)':'BREAKPOINT'}

        data = data.decode(self.encoding)    
        for regstr, event in TABLE.items():
            regex = search(regstr, data)
            if regex: spawn(dev, event, 
                *regex.groups())
  
  










