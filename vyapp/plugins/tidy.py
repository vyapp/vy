"""
Overview
========

Show errors in html files by running Tidy.

Extern dependencies:
    Html Tidy

Key-Commands
============

Namespace: tidy

Mode: HTML
Event: <Key-h>
Description: Run Tidy on the current html file and display
a dialog window with all encountered errors. When the dialog
window is shown with the errors it is possible to jump to the
error line by pressing <Return>.

Commands
========

Command: html_errors()
Description: Same as the keycommand <Key-h>.

"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.plugins import ENV
from vyapp.app import root
from re import findall
import sys

class HtmlChecker(object):
    PATH = 'tidy'

    def  __init__(self, area):
        self.area = area

    def check(self):
        child  = Popen([self.PATH, '--show-body-only', '1', '-e', '-quiet',
        self.area.filename], stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset)

        output = child.communicate()[0]
        regex  = 'line ([0-9]+) column ([0-9]+) - (.+)'
        ranges = findall(regex, output)
        ranges = map(lambda ind: (self.area.filename, ind[0], ind[2]), ranges)

        sys.stdout.write('Errors:\n%s\n' % output)
        self.area.chmode('NORMAL')

        if child.returncode:
            self.display(ranges)
        else:
            root.status.set_msg('No errors!')

    def display(self, ranges):
        root.status.set_msg('Errors were found!' )
        options = LinePicker()
        options(ranges)

def install(area):
    html_checker = HtmlChecker(area)
    picker       = lambda event: html_checker.check()
    area.install('tidy', ('HTML', '<Key-h>', picker))

def html_errors():
    html_checker = HtmlChecker(AreaVi.ACTIVE)
    html_checker.check()

ENV['html_errors'] = html_errors

