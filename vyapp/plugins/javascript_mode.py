"""
Overview
========

Extra mode for javascript programming language.

Key-Commands
============

Namespace: javascript-mode

Mode: NORMAL
Event: <Key-percent>
Description: Switch to JAVASCRIPT mode.
"""
from vyapp.plugins import Namespace

class JavascriptModeNS(Namespace):
    pass

def javascript_mode(area):
    area.chmode('JAVASCRIPT')

def install(area):
    area.add_mode('JAVASCRIPT')
    area.install(JavascriptModeNS, ('NORMAL', '<Key-percent>', 
    lambda event: javascript_mode(area)))


