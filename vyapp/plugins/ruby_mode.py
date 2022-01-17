"""
Overview
========

Extra mode for Ruby programming language.

Key-Commands
============

Namespace: ruby-mode

Mode: NORMAL
Event: <Key-exclam>
Description: Switch to ruby mode.
"""

from vyapp.plugins import Namespace

class RubyModeNS(Namespace):
    pass

class RubyMode:
    def __init__(self, area):
        self.area = area
        area.add_mode('RUBY')

        area.install(RubyModeNS, ('NORMAL', 
        '<Key-asterisk>', self.ruby_mode))

    def ruby_mode(self, event):
        self.area.chmode('RUBY')


install = RubyMode