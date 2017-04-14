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

        area.install('html-checker', (-1, '<<Load-text/html>>', lambda event: 
        self.area.hook('BETA', '<Key-h>', self.check)),
        (-1, '<<LoadData>>', lambda event: 
        self.area.unhook('BETA', '<Key-h>')),
        (-1, '<<Save-text/html>>', lambda event: 
        self.area.hook('BETA', '<Key-h>', self.check)),
        (-1, '<<SaveData>>', lambda event: 
        self.area.unhook('BETA', '<Key-h>')))

    def check(self, event):
        child  = Popen([self.path, '-e', '-quiet', 
        self.area.filename], stdout=PIPE, stderr=STDOUT)
        output = child.communicate()[0]
        regex  = 'line ([0-9]+) column ([0-9]+) - (.+)'
        ranges = findall(regex, output)

        sys.stdout.write('Errors:\n%s\n' % output)
        for line, col, error in ranges:
            self.area.tag_add('(SPOT)', '%s.0' % line, 
            '%s.0 lineend' % line)

        if child.returncode:
            root.status.set_msg('Errors were found!')
        else:
            root.status.set_msg('No errors!')
        self.area.chmode('NORMAL')

install = HtmlChecker




