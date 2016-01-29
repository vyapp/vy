"""
Overview
========

This module implements a keycommand to download the source code of the url that is
in the clipboard.

Usage
=====

In order to have the url source code inserted in an AreaVi instance it is neeeded to set an output
target. Copy a URL address to the clipboard then switch to BETA mode and press <Key-m>.
The source code that corresponds to the URL address will be inserted in the
AreaVi instance that was set as output target.

Key-Commands
============

Mode: BETA
Event: <Key-m>
Description: Download the source code of the URL that is in the clipboard
and writes it to sys.stdout.
"""

import sys
import urllib2

def install(area):
    def get_url_source():
        opener            = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        req               = opener.open(area.clipboard_get()) 
        sys.stdout.write(req.read())

    area.hook('BETA', '<Key-m>', lambda event: get_url_source())





