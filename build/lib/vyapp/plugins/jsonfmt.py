"""
Overview
========

This plugin implements a key-command to format JSON strings. You select
the region containing the JSON then issue the key-command to format it will
print any errors on the status bar.

Key-Commands
============

Namespace: jsonfmt

Mode: EXTRA
Event: <Key-j>
Description: Format the selected JSON data then switch to NORMAL mode.

"""

from subprocess import Popen, PIPE
from vyapp.app import root

class FmtJSON:
    def __init__(self, area, *args, **kwargs):
        self.area = area
        area.install('fmtjson', ('EXTRA', '<Key-j>', self.run_printer))

    def run_printer(self, event):
        start = self.area.index('sel.first')
        end = self.area.index('sel.last')
        data = self.area.get(start, end)

        child = Popen('python -m json.tool', encoding=self.area.charset,
        stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=1)

        output, err = child.communicate(data)
        print('\nJSON Errors:\n', err)

        if child.returncode: 
            root.status.set_msg('JSON Errors! Check its output.')
        else:
            self.area.swap(output, start, end)

        self.area.chmode('NORMAL')

install = FmtJSON