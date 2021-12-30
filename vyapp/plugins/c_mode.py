"""
Overview
========

Extra mode for c programming language.

Key-Commands
============

Namespace: c-mode

Mode: NORMAL
Event: <Key-exclam>
Description: Switch to C mode.
"""

from vyapp.plugins import Namespace

class CModeNS(Namespace):
    pass

def c_mode(area):
    area.chmode('C/C++')

def install(area):
    area.add_mode('C/C++')
    area.install(CModeNS, ('NORMAL', '<Key-dollar>', 
    lambda event: c_mode(area)))


