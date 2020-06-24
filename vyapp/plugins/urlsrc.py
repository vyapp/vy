"""
Overview
========

Implement keycommands to download url source and view it in the
given AreaVi instance. It also can load HTML content in the browser.

Key-Commands
===========

Namespace: urlsrc

Mode: HTML
Event: <Key-o>
Description: Load the focused AreaVi instance file in the browser.

Mode: HTML
Event: <Key-s>
Description: Download the source code of the URL that is in the clipboard
and writes it to sys.stdout.
"""

import webbrowser
import urllib.request, urllib.error, urllib.parse

class UrlSrc:
    def  __init__(self, area):
        self.area = area
        area.install('urlsrc', 
        ('HTML', '<Key-o>', self.bload_data),
        ('HTML', '<Key-s>', self.url_download))
    
    def bload_data(self, event):
        webbrowser.open_new_tab(event.widget.filename)
        event.widget.chmode('NORMAL')
    
    def url_download(self, event):
        opener            = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        req               = opener.open(event.widget.clipboard_get()) 
        event.widget.delete('1.0', 'end')
        event.widget.insert('1.0', req.read())
        event.widget.chmode('NORMAL')
    
install = UrlSrc
