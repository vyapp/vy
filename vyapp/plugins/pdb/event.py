from untwisted.network import spawn, xmap
from untwisted.splits import Terminator
from re import search

def handle_found(device, data):
    TABLE = {
                '\> (?P<filename>.+)\((?P<line>[0-9]+)\)(?P<args>.+)':('LINE', ('filename', 'line', 'args')),
                '\(Pdb\) Deleted breakpoint (?P<index>[0-9]+)':('DELETED_BREAKPOINT', ('index',)),
                '\(Pdb\) Breakpoint (?P<index>[0-9]+) at (?P<filename>.+)\:(?P<line>[0-9]+)':('BREAKPOINT', ('index', 'filename', 'line'))
            }
    
    for regex, (event, groups) in TABLE.iteritems():
        sch = search(regex, data)
        if not sch: continue
        spawn(device, event, *sch.group(*groups))
        break

def install(device):
    xmap(device, Terminator.FOUND, handle_found)










