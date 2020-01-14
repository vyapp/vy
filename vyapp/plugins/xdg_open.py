""""
Overview
========

Many times a file path appears in some contexts of a daily programmer.
This plugin uses xdg-open to open files using proper applications. It is enough
to place the cursor over the file path then press a key to get the file
opened with the proper application.

Key-Commands
============

Mode: NORMAL
Event: <Key-U> 
Description: Open a file using xdg-open whose path is under the cursor. The path
has to be mapped to an entire line otherwise it fails.
"""
from subprocess import Popen

class XdgOpen:
    def __init__(self, area):
        self.area = area

        area.install('xdg_open', ('NORMAL', '<Key-U>', lambda e: self.openfile()))

    def openfile(self):
        """
        Open a file using the appropriate program for. 
        """

        filename = self.area.get_line()
        # No need for "" because it is passing the entire filename
        # as parameter.
        Popen(['xdg-open', '%s'  % filename])

install = XdgOpen