##############################################################################
tee >(stdbuf -o 0 python -i)

##############################################################################
# pychecker.

from re import findall
regex = '(.+?):([0-9]+):?([0-9]*):(.+)'
findall(regex, 'file1.py:4:6: invalid syntax')
findall(regex, "file0.py:1: 'file1' imported but unused")

findall('(a+)(b+)', 'aabbb\naaaabbb')

from re import findall
regex = '(.+?):([0-9]+):?[0-9]*:(.+)'
findall(regex, 'file1.py:4:6: invalid syntax')
findall(regex, "file0.py:1: 'file1' imported but unused")

findall('(a+)(b+)', 'aabbb\naaaabbb')

##############################################################################
import re
REGSTR = '\(Pdb\) Deleted breakpoint (?P<index>[0-9]+)(?P<foo>a)'
regex = re.search(REGSTR, '(Pdb) Deleted breakpoint 11a')
groups = ('index', )
regex.group(*groups)
regex.groups('index')
##############################################################################
import re
REGSTR = '\> (.+)\(([0-9]+)\)(.+)'
regex = re.search(REGSTR, 
'(Pdb) > /home/tau/tests/pyflakes/file0.py(2)<module>()')

regex.groups()
regex.group(0)
##############################################################################
def func(a, b):
    print(a, b)

s = '12'
func(*s)
##############################################################################

def get_sentinel_file(path, filename):
    """
    """

    tmp = path
    while True:
        tmp = dirname(tmp)
        if exists(join(tmp, filename)):
            return tmp
        elif tmp == dirname(tmp):
            return path
        path = tmp

