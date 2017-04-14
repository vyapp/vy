"""
Overview
========

Implement keycommands to deal with urls.

Key-Commands
===========

Namespace: urls

Mode: ALPHA
Event: <Key-l>
Description: Open the url over the cursor in the browser, a new tab is opened.

Mode: ALPHA
Event: <Key-o>
Description: Load the focused AreaVi instance file in the browser.

Mode: ALPHA
Event: <Key-s>
Description: Download the source code of the URL that is in the clipboard
and writes it to sys.stdout.
"""

import webbrowser
import sys
import urllib2

def open_cursor_url(event):
    webbrowser.open_new_tab(event.widget.get_seq('insert'))
    event.widget.chmode('NORMAL')

def open_current_file(event):
    webbrowser.open_new_tab(event.widget.filename)
    event.widget.chmode('NORMAL')

def get_url_source(event):
    opener            = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    req               = opener.open(event.widget.clipboard_get()) 
    event.widget.delete('1.0', 'end')
    event.widget.insert('1.0', req.read())
    event.widget.chmode('NORMAL')

def install(area):
    area.install('urls', ('ALPHA', '<Key-l>', open_cursor_url),
                 ('ALPHA', '<Key-o>', open_current_file),
                 ('ALPHA', '<Key-s>', get_url_source))











