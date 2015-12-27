"""
Overview
========

It is handy to have Key-Commands to insert blank lines up/down the cursor when in NORMAL mode.

Usage
=====

In NORMAL mode, type <Key-m> to insert a blank line down the cursor or <Key-n> 
to insert a blank line up the cursor.

Key-Commands
============

Mode: NORMAL
Event: <Key-m> 
Description: Insert a line down then goes insert mode.


Mode: NORMAL
Event: <Key-n> 
Description: Insert a line up then goes insert mode.


"""

def insert_down(area):
        area.insert_line_down()
        area.chmode('INSERT')

def insert_up(area):
        area.insert_line_up()
        area.chmode('INSERT')

def install(area):
    area.install(('NORMAL', '<Key-m>', lambda event: insert_down(event.widget)),
                 ('NORMAL', '<Key-n>', lambda event: insert_up(event.widget)))





