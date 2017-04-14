"""
Overview
========

This plugin implements Key-Commands to comment and uncomment blocks of code.

Key-Commands
============

Namespace: inline-comment

Mode: ALPHA
Event: <Key-e>
Description: Add inline comments to a selected block of text.

Mode: ALPHA
Event: <Key-r>
Description: Remove inline comments from a selected block of text.

"""

from mimetypes import guess_type
from re import escape

DEFAULT = '#'
TABLE   = { 
              'text/x-python'            :'#',
              'text/x-java-source'       :'//',
              'text/x-csrc'              :'//',
              'text/x-sh'                :'#',
              'application/x-javascript' :'//',
              'text/x-c++src'            :'//'
          }

def add_inline_comment(area):
    """
    It adds inline comment to selected lines based on the file extesion.
    """

    comment = TABLE.get(guess_type(area.filename)[0], DEFAULT)
    area.replace_ranges('sel', '^ +|^', 
    lambda data, index0, index1: '%s%s ' % (area.get(index0, index1), comment))
    area.clear_selection()
    area.chmode('NORMAL')

def rm_inline_comment(area):
    """
    It removes the inline comments.
    """

    comment = TABLE.get(guess_type(area.filename)[0], DEFAULT)
    area.replace_ranges('sel', '^ *%s ?' % comment, 
    lambda data, index0, index1: area.get(index0, index1).replace(
        '%s ' % comment, '').replace(comment, ''))
    area.clear_selection()
    area.chmode('NORMAL')

def install(area):
    area.install('inline-comment',
    ('ALPHA', '<Key-r>', lambda event: rm_inline_comment(event.widget)),
    ('ALPHA', '<Key-e>', lambda event: add_inline_comment(event.widget)))









