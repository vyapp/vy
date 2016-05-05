"""
Overview
========

Implement a key command to quickly open urls.

Usage
=====

Place the cursor over a string that corresponds to a url address then switch to ALPHA mode. Once
in ALPHA mode, press <Key-l>. It will open the url in the current browser's tab.

Key-Commands
===========

Mode: ALPHA
Event: <Key-l>
Description: Open the url over the cursor in the browser, a new tab is opened.

Mode: ALPHA
Event: <Key-L>
Description: Load the focused AreaVi instance file in the browser.
"""

import webbrowser

def open_url(event):
    webbrowser.open_new_tab(event.widget.get_seq('insert'))
    event.widget.chmode('NORMAL')

def open_file(event):
    webbrowser.open_new_tab(event.widget.filename)
    event.widget.chmode('NORMAL')

def install(area):
    area.install(('ALPHA', '<Key-l>', open_url),
                 ('ALPHA', '<Key-L>', open_file))



