"""

Overview
========

This plugin implements two Key-Commands to make the cursor jump to specific
region of texts.

Key-Commands
============

Namespace: text-jumps

Mode: NORMAL
Event: <Key-1> 
Description: Place the cursor at the beginning of the file.


Mode: NORMAL
Event: <Key-2> 
Description: Place the cursor at the end of the file.

Mode: NORMAL
Event: <Key-o> 
Description: Place the cursor at the beginning of the line.


Mode: NORMAL
Event: <Key-p> 
Description: Place the cursor at the end of the line.

Mode: NORMAL
Event: <Key-braceleft> 
Description: Place the cursor at the beginning of the next word.


Mode: NORMAL
Event: <Key-braceright> 
Description: Place the cursor at the beginning of the previous word.
"""

class TextJumps:
    def __init__(self, area):
        area.install('text-jumps', 
        ('NORMAL', '<Key-1>', self.text_start),
        ('NORMAL', '<Key-2>', self.text_end), 
        ('NORMAL', '<Key-o>', self.line_start),
        ('NORMAL', '<Key-p>', self.line_end), 
        ('NORMAL', '<Key-braceleft>', self.next_word),
        ('NORMAL', '<Key-braceright>', self.prev_word))
        self.area = area

    def text_start(self, event):
        """
        Place the cursor at the beginning of the file.
        """

        self.area.mark_set('insert', '1.0')
        self.area.see('insert')
    
    def text_end(self, event):
        """
        Place the cursor at the end of the file.
        """

        self.area.mark_set('insert', 'end linestart')
        self.area.see('insert')

    def line_start(self, event):
        """
        Place the cursor at the beginning of the line.
        """

        self.area.mark_set('insert', 'insert linestart')
        

    def line_end(self, event):
        """
        Place the cursor at the end of the line.
        """

        self.area.mark_set('insert', 'insert lineend')

    def next_word(self, event):
        """
        Place the cursor at the next word.
        """

        _, index0, index1 = self.area.isearch('\M', index='insert', 
        regexp=True, stopindex='end')

        self.area.mark_set('insert', index0)
        self.area.see('insert')

    def prev_word(self, event):
        """
        Place the cursor at the previous word.
        """

        _, index0, index1 = self.area.isearch('\M', backwards=True, 
        regexp=True, index='insert', stopindex='1.0')

        self.area.mark_set('insert', index1)
        self.area.see('insert')

install = TextJumps

