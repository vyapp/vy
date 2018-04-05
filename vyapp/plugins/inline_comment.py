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

from re import escape
import os.path

DEFAULT = '#'
TABLE   = { 
              '.py'   :'#',
              '.java'  :'//',
              '.c'    :'//',
              '.sh'   :'#',
              '.js'   :'//',
              '.cpp'  :'//',
              '.html' :'//',
              '.go'   :'//',
              '.rb' :'#',

          }

def add_inline_comment(area):
    """
    It adds inline comment to selected lines based on the file extesion.
    """

    comment = TABLE.get(os.path.splitext(area.filename)[1], DEFAULT)
    area.replace_ranges('sel', '^ *|^\t*', 
    lambda data, index0, index1: '%s%s ' % (data, comment))
    area.clear_selection()
    area.chmode('NORMAL')

def rm_inline_comment(area):
    """
    It removes the inline comments.
    """

    comment = TABLE.get(os.path.splitext(area.filename)[1], DEFAULT)
    area.replace_ranges('sel', '^ *%s ?|^\t*%s ?' % (comment, comment), 
    lambda data, index0, index1: data.replace(
        '%s ' % comment, '').replace(comment, ''))
    area.clear_selection()
    area.chmode('NORMAL')

def install(area):
    area.install('inline-comment',
    ('ALPHA', '<Key-r>', lambda event: rm_inline_comment(event.widget)),
    ('ALPHA', '<Key-e>', lambda event: add_inline_comment(event.widget)))












