"""
Overview
========

Extra mode for golang programming language.

Key-Commands
============

Namespace: golang-mode

Mode: NORMAL
Event: <Key-numbersign>
Description: Switch to GOLANG mode.
"""

from vyapp.plugins import Namespace

class GolangModeNS(Namespace):
    pass

def golang_mode(area):
    area.chmode('GOLANG')

def install(area):
    area.add_mode('GOLANG')
    area.install(GolangModeNS, ('NORMAL', '<Key-numbersign>', 
    lambda event: golang_mode(area)))

























