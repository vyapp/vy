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

def golang_mode(area):
    area.chmode('GOLANG')

def install(area):
    area.add_mode('GOLANG')
    area.install('golang-mode', ('NORMAL', '<Key-numbersign>', 
    lambda event: golang_mode(area)))

























