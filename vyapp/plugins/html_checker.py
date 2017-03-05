"""
Overview
========

Highlight html lines where errors/warnings were encountered by Html Tidy.

Plugin dependencies: 

vyapp.plugins.text_spots

Extern dependencies:
Html Tidy

"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.app import root
from re import findall
import sys

class HtmlChecker(object):
    def  __init__(self, area, path='tidy'):
        self.area = area
        # The path that tidy stays, in some
        # systems it may not be available in the
        # PATH variable.
        self.path = path
        area.install((-1, '<<Save-text/html>>', self.check))

    def check(self, event):
        child  = Popen([self.path, '-e', '-quiet', 
        self.area.filename], stdout=PIPE, stderr=STDOUT)
        output = child.communicate()[0]
        regex  = 'line ([0-9]+) column ([0-9]+) - (.+)'
        ranges = findall(regex, output)

        for line, col, error in ranges:
            self.area.tag_add('(SPOT)', '%s.0' % line, 
                '%s.0 lineend' % line)

        if child.returncode:
            root.status.set_msg('Errors were found!')
        else:
            root.status.set_msg('Errors were found!')
        sys.stdout.write('Errors:\n%s\n' % output)

install = HtmlChecker
