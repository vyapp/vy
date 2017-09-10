##############################################################################
# pychecker.

from re import findall
regex = '(.+?):([0-9]+):?([0-9]*):(.+)'
findall(regex, 'file1.py:4:6: invalid syntax')
findall(regex, "file0.py:1: 'file1' imported but unused")

findall('(a+)(b+)', 'aabbb\naaaabbb')

