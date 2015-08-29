"""
Overview
========

It is handy to quickly get the absolute path of the file that is being edited. This plugin
implements a Key-Command for that.

Usage
=====

When a file is opened, vy holds a complete path for the file. It is possible
to put such a complete path in the clipboard area for other purposes. For such
switch to ALPHA mode by pressing <Key-3> in NORMAL mode then press <Key-u>.

After pressing <Key-u> in ALPHA mode there will appear a msg on the status bar notifying that
the complete path was copied to the clipboard.

Key-Commands
============

Mode: ALPHA
Event: <Key-u>
Description: Copies the complete path of the file to the clipboard.

"""

from vyapp.tools import set_status_msg

def clip_ph(area):
    """ Sends filename path to clipboard. """
    area.clipboard_clear()
    area.clipboard_append(area.filename)
    set_status_msg('File path copied to the clipboard.')

def install(area):
    area.install(('ALPHA', '<Key-u>', lambda event: clip_ph(event.widget)))










