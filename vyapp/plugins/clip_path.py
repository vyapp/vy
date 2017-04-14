"""
Overview
========

It is handy to quickly get the absolute path of the file that is being edited. This plugin
implements a Key-Command for that.

Key-Commands
============

Namespace: clip-path

Mode: ALPHA
Event: <Key-u>
Description: Copies the complete path of the file to the clipboard.

"""

from vyapp.app import root

def clip_ph(area):
    """ Sends filename path to clipboard. """
    area.clipboard_clear()
    area.clipboard_append(area.filename)
    root.status.set_msg('File path copied to the clipboard.')

def install(area):
    area.install('clip-path', ('ALPHA', '<Key-u>', lambda event: clip_ph(event.widget)))














