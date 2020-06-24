"""
Overview
========

This plugin implements Key-Commands to comment and uncomment blocks of code.

Key-Commands
============

Namespace: inline-comment

Mode: EXTRA
Event: <Key-e>
Description: Add inline comments to a selected block of text.

Mode: EXTRA
Event: <Key-r>
Description: Remove inline comments from a selected block of text.

"""

import os.path

table   = { 
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

class Clipboard:
    default = '#'

    def __init__(self, area):
        self.area = area

        area.install('inline-comment',
        ('EXTRA', '<Key-C>', self.remove_comment),
        ('EXTRA', '<Key-c>', self.add_comment))
    
    def add_comment(self, event):
        """
        It adds inline comment to selected lines based on the file extesion.
        """
    
        comment = table.get(os.path.splitext(self.area.filename)[1], self.default)
        self.area.replace_ranges('sel', '^ *|^\t*', 
        lambda data, index0, index1: '%s%s ' % (data, comment))
        self.area.clear_selection()
        self.area.chmode('NORMAL')
    
    def remove_comment(self, event):
        """
        It removes the inline comments.
        """
    
        comment = table.get(os.path.splitext(self.area.filename)[1], self.default)
        self.area.replace_ranges('sel', '^ *%s ?|^\t*%s ?' % (comment, comment), 
        lambda data, index0, index1: data.replace(
            '%s ' % comment, '').replace(comment, ''))
        self.area.clear_selection()
        self.area.chmode('NORMAL')

install = Clipboard