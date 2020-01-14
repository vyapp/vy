"""
Overview
========

Implement keycommands to deal with urls.

Key-Commands
===========

Namespace: urls

Mode: EXTRA
Event: <Key-l>
Description: Open the url over the cursor in the browser, a new tab is opened.

Mode: EXTRA
Event: <Key-o>
Description: Load the focused AreaVi instance file in the browser.

Mode: EXTRA
Event: <Key-s>
Description: Download the source code of the URL that is in the clipboard
and writes it to sys.stdout.
"""

import webbrowser
import urllib.request, urllib.error, urllib.parse

def visit_url(event):
    start, end = event.widget.get_seq_range()
    url = event.widget.get(start, end)
    webbrowser.open_new_tab(url)
    event.widget.chmode('NORMAL')

def bload_data(event):
    webbrowser.open_new_tab(event.widget.filename)
    event.widget.chmode('NORMAL')

def url_download(event):
    opener            = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    req               = opener.open(event.widget.clipboard_get()) 
    event.widget.delete('1.0', 'end')
    event.widget.insert('1.0', req.read())
    event.widget.chmode('NORMAL')

def install(area):
    area.install('urls', 
    ('EXTRA', '<Key-U>', visit_url),
    ('EXTRA', '<Key-o>', bload_data),
    ('EXTRA', '<Key-s>', url_download))

