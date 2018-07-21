"""
Overview
========

This module implements keycommands to select sequences of chars that
match a special pattern, words, non blank sequences etc.

Key-Commands
============

Namespace: data-sel

Mode: NORMAL
Event: <Key-f> 
Description: Add selection to a line over the cursor.

Mode: NORMAL
Event: <Control-o> 
Description: Add selection from the cursor position to the beginning of the line.

Mode: NORMAL
Event: <Control-p> 
Description: Add selection from the cursor position to the end of the line.
Mode: NORMAL
Event: <Key-bracketleft> 
Description: Add selection to a word where the cursor is placed on.

Mode: NORMAL
Event: <Control-bracketleft>
Description: Select a sequence of non blank chars that is over
the cursor.

Mode: NORMAL
Event: <Control-Key-1> 
Description: Add selection from the cursor positon to the beginning of the file.


Mode: NORMAL
Event: <Control-Key-2> 
Description: Add selection from the cursor position to the end of the file.


Mode: NORMAL
Event: <Control-a> 
Description: Add selection from the beginning to the end of the file.
"""

class DataSel:
    def __init__(self, area):
        area.install('data-sel', 
        ('NORMAL', '<Control-bracketleft>', self.sel_seq),
        ('NORMAL', '<Key-bracketleft>', self.sel_word), 
        ('NORMAL', '<Control-Key-1>', self.sel_text_start),
        ('NORMAL', '<Control-Key-2>', self.sel_text_end),
        ('NORMAL', '<Control-a>', self.sel_all), 
        ('NORMAL', '<Key-f>', self.sel_line),
        ('NORMAL', '<Control-o>', self.sel_line_start),
        ('NORMAL', '<Control-p>', self.sel_line_end))
        self.area = area

    def sel_seq(self, event):
        """
        Select the closest sequence of non blank characters from the cursor.
        """

        index1, index2 = self.area.get_seq_range()
        self.area.tag_add('sel', index1, index2)

    def sel_word(self, event):
        """
        Select the closest word from the cursor.
        """

        index1, index2 = self.area.get_word_range()
        self.area.tag_add('sel', index1, index2)

    def sel_all(self, event):
        """
        It selects all text.
        """

        self.area.tag_add('sel', '1.0', 'end')

    def sel_text_start(self, event):
        """
        It selects all text from cursor position to the start position
        of the text.

        """

        index = self.area.index('insert')
        self.area.mark_set('insert', '1.0')
        self.area.see('insert')
        self.area.addsel(index, 'insert')

    def sel_text_end(self, event):
        """
        It selects all text from the cursor position to the end of the text.
        """

        index = self.area.index('insert')
        self.area.mark_set('insert', 'end linestart')
        self.area.see('insert')
        self.area.addsel(index, 'insert')

    def sel_line_start(self, event):
        """
        It adds selection from the cursor position to the 
        start of the line.
        """

        index = self.area.index('insert')
        self.area.mark_set('insert', 'insert linestart')
        self.area.addsel(index, 'insert')

    def sel_line_end(self, event):
        """
        It selects all text from the cursor position to the end of the line.
        """

        index = self.area.index('insert')
        self.area.mark_set('insert', 'insert lineend')
        self.area.addsel(index, 'insert')

    def sel_line(self, event):
        """
        Toggle line selection.
        """

        self.area.toggle_range('sel', 
        'insert linestart', 'insert +1l linestart')

install = DataSel


