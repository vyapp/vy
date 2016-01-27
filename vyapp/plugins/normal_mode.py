"""
Overview
========

Usage
=====

Key-Commands
============

"""

def install(area):
    area.add_mode('NORMAL')
    area.chmode('NORMAL')
    area.install((-1, '<Escape>', lambda event: area.chmode('NORMAL')))
    area.install(('NORMAL', '<Escape>', lambda event: area.clear_selection()))


