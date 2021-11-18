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

def ruby_mode(area):
    area.chmode('RUBY')

def install(area):
    area.add_mode('RUBY')
    area.install('ruby-mode', ('NORMAL', '<Key-asterisk>', 
    lambda event: ruby_mode(area)))



