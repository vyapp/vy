""" 
Overview
========

This plugin implements block selection of text.

Key-Commands
============

Namespace: block-sel

Mode: NORMAL
Event: <Control-K> 
Description: Add block selection one line up.


Mode: NORMAL
Event: <Control-J>
Description: Add block selection one line down.

Mode: NORMAL
Event: <Control-H>
Description: Add block selection one char left.

Mode: NORMAL
Event: <Control-L>
Description: Add block selection one char right.

"""
from vyapp.app import root

class BlockSel:
    def __init__(self, area):
        area.install('block-sel', 
        ('NORMAL', '<Control-K>', self.block_up),
        ('NORMAL', '<Control-J>', self.block_down),
        ('NORMAL', '<Control-H>', self.block_left),
        ('NORMAL', '<Control-L>', self.block_right),
        ('NORMAL', '<Control-V>', self.start_block_selection))
        area.mark_set('(BLOCK_SEL_MARK)', '1.0')

        self.area = area

    def addblock(self, index0, index1):
        """
        It adds block selection from index0 to index1.
        """

        index2 = self.area.min(index0, index1)
        index3 = self.area.max(index0, index1)
        a, b   = self.area.indint(index2)
        c, d   = self.area.indint(index3)

        for ind in range(a, c + 1):
            self.area.addsel('%s.%s' % (ind, min(b, d)), 
                '%s.%s' % (ind, max(b, d)))

    def rmblock(self, index0, index1):
        """
        It removes block selection from index0 to index1.
        """

        index2 = self.area.min(index0, index1)
        index3 = self.area.max(index0, index1)

        a, b   = self.area.indint(index2)
        c, d   = self.area.indint(index3)

        for ind in range(a, c + 1):
            self.area.rmsel('%s.%s' % (ind, min(b, d)),  
                '%s.%s' % (ind, max(b, d)))

    def block_down(self, event):
        """  
        It adds or removes block selection one line down.  
        """

        a, b  = self.area.indref('(CURSOR_LAST_COL)')
        c, d  = self.area.indcur()

        index = self.area.index('(BLOCK_SEL_MARK)')
        self.rmblock(index, '%s.%s' % (c, b))
        self.area.down()

        a, b   = self.area.indref('(CURSOR_LAST_COL)')
        c, d = self.area.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def block_up(self, event):
        """  
        It adds or removes block selection one line up.  
        """

        a, b   = self.area.indref('(CURSOR_LAST_COL)')
        c, d   = self.area.indcur()
        index  = self.area.index('(BLOCK_SEL_MARK)')

        self.rmblock(index, '%s.%s' % (c, b))
        self.area.up()

        a, b = self.area.indref('(CURSOR_LAST_COL)')
        c, d = self.area.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def block_left(self, event):
        """
        It adds block selection to the left.
        """

        a, b   = self.area.indref('(CURSOR_LAST_COL)')
        c, d   = self.area.indcur()

        index = self.area.index('(BLOCK_SEL_MARK)')
        self.rmblock(index, '%s.%s' % (c, b))
        self.area.left()

        a, b   = self.area.indref('(CURSOR_LAST_COL)')
        c, d = self.area.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def block_right(self, event):
        """
        It adds/removes block selection to the right.
        """

        a, b   = self.area.indref('(CURSOR_LAST_COL)')
        c, d   = self.area.indcur()

        index = self.area.index('(BLOCK_SEL_MARK)')
        self.rmblock(index, '%s.%s' % (c, b))
        self.area.right()

        a, b   = self.area.indref('(CURSOR_LAST_COL)')
        c, d = self.area.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def start_block_selection(self, event):
        """
        Start block selection.
        """

        self.area.mark_set('(BLOCK_SEL_MARK)', 'insert')
        root.status.set_msg('Dropped block selection mark.')

install = BlockSel

