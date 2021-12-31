"""
Overview
========

It is handy to quickly get the absolute path of the file that is being edited. This plugin
implements a Key-Command for that.

Key-Commands
============

Namespace: clip-path

Mode: EXTRA
Event: <Key-ampersand>
Description: Copies the complete path of the file to the clipboard.

"""

from vyapp.app import root
from vyapp.plugins import Namespace

class ClipPathNS(Namespace):
    pass

class ClipPath:
    def __init__(self, area):
        self.area = area
        area.install(ClipPathNS, ('EXTRA', '<Key-ampersand>', 
        self.clip_ph))

    def clip_ph(self, event):
        """ Sends filename path to clipboard. """
        self.area.clipboard_clear()
        self.area.clipboard_append(area.filename)
        root.status.set_msg('File path copied to the clipboard.')
    
install = ClipPath