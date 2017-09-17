"""
Overview
========

Highlight html lines where errors/warnings were encountered by Html Tidy.

When the plugin is installed in your vyrc, whenever an event
of the type <Key-h> in BETA mode happens it runs tidy against the file
and tags all regions where tidy found errors. 

It is possible to jump to these regions by using the keycommands implemented by
the core text_spots plugin. 

One would just jump back/next by pressing <Control-n> or <Control-m>
in NORMAL mode. 

The html checker plugin writes to sys.stdout all the errours
that were encountered in the html file. it is necessary
to set an output target on areavi instance in order to check
the errors/warnings.

For more information see: vyapp.plugins.text_spots

Plugin dependencies: 
    vyapp.plugins.text_spots

Extern dependencies:
    Html Tidy

Key-Commands
============

Namespace: html-checker

Mode: HTML
Event: <Key-h>
Description: Highlight all lines
with syntax errors/bad html. It is possible to jump upwards/downwards
using the same keys as defined in text_spots plugin.

"""

from subprocess import Popen, STDOUT, PIPE
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
        child  = Popen([self.PATH, '-e', '-quiet', 
        self.area.filename], stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset)

        output = child.communicate()[0]
        regex  = 'line ([0-9]+) column ([0-9]+) - (.+)'
        ranges = findall(regex, output)
        sys.stdout.write('Errors:\n%s\n' % output)
        self.area.reset_assoc_data()

        for line, col, error in ranges:
            self.assoc_msg(line, error)

        if child.returncode:
            root.status.set_msg('Errors were found!')
        else:
            root.status.set_msg('No errors!')
        self.area.chmode('NORMAL')

    def assoc_msg(self, line, error):
        index0 = '%s.0' % line, 
        index1 = '%s.0 lineend' % line

        self.area.tag_add('(SPOT)', index0, index1)
        self.area.set_assoc_data(index0, index1, error)

def install(area):
    html_checker = HtmlChecker(area)
    picker = lambda event: html_checker.check()

    area.install('html-checker', 
    ('HTML', '<Key-h>', picker))

def html_errors():
    html_checker = HtmlChecker(AreaVi.ACTIVE)
    html_checker.check()

ENV['html_errors'] = html_errors



