"""

"""

from Tkinter import *
from re import escape
import mimetypes

class AreaVi(Text):
    ACTIVE = None

    def __init__(self, default_filename, *args, **kwargs):
        """
        This class receives all Text widget arguments
        and one named default_filename which means
        the filename that is saved when no filename
        is specified.

        default_filename:   
        The default path file where contents are saved.        

        It implements a system of modes to handle
        tkinter keypresses events. 
        
        The method hook can be used to bind events
        to callbacks mapped to specific modes.
        """

        Text.__init__(self, *args, **kwargs)
        self.setup = dict()

        # Maybe it should be?
        # abspath(default_filename)
        self.default_filename = default_filename

        # The file's path and name.
        self.filename = default_filename

        # Shouldn't it be LAST_COL and MSEL?
        self.last_col = '_last_col_'
        self.mark_set(self.last_col, '1.0')

        # This mark is used in AreaVi.replace_all.

        self.STOP_REPLACE_INDEX = '_stop_replace_index_'
        # Tags have name starting and ending with __


        # def cave(event):
            # AreaVi.ACTIVE = event.widget
        # self.hook(-1, '<FocusIn>', cave)
        AreaVi.ACTIVE        = self
        self.charset         = 'utf-8'

    def active(self):
        """
        It is used to create a model of target for plugins
        defining python functions to run on fly.
        
        With such an abstraction it is possible to define a AreaVi instance target
        that python code will act on.
        """

        AreaVi.ACTIVE = self

    def chmode(self, id):
        """
        This function is used to change the AreaVi instance's mode.
        It receives one parameter named id which means the
        mode number.
        """
        opt     = self.setup[id]
        self.id = id

        MODE_X = 'mode%s-1' % self
        MODE_Y = 'mode%s%s' % (self, id)

        if opt: self.bindtags((MODE_X, MODE_Y, self, 'Text', '.'))
        else: self.bindtags((MODE_X, MODE_Y, self, '.'))


    def add_mode(self, id, opt=False):
        """
        It adds a new mode. The opt argument means whether
        it should propagate the event to the internal text widget callbacks.
        """

        self.setup[id] = opt

    def del_mode(self, id):
        """
        It performs the opposite of add_mode.
        """

        del self.setup[id]


    def hook(self, id, seq, callback):
        """
        This method is used to hook a callback to a sequence
        specified with its mode. The standard modes are insert and selection.
        The insert mode prints the key character on the text area.
        """
        MODE_Y = 'mode%s%s' % (self, id)

        self.bind_class(MODE_Y, seq, callback, add=True)


    def unhook(self, id, seq, callback=None):
        """
        It performs the opposite of unhook.
        """
        MODE_Y = 'mode%s%s' % (self, id)

        self.unbind_class(MODE_Y, seq)

    def install(self, *args):
        """
        It is like self.hook but accepts
        a sequence of (id, seq, callback).
        """

        for id, seq, callback in args:
            self.hook(id, seq, callback)

    def uninstall(self, *args):
        """
        Like self.hook but accepts.
        (id, seq, callback).
        """

        for id, seq, callback in args:
            self.unhook(id, seq, callback)

    def append(self, data):
        """
        """

        self.insert('end', data)
        self.mark_set('insert', 'end')
        self.see('end')

    def curline(self):
        """
        A short hand for.

        area.get('insert linestart', 'insert +1l linestart')
        """
        return self.get('insert linestart', 'insert +1l linestart')

    def tag_update(self, name, index0, index1, *args):
        """
        It removes a given tag from index0 to index1 and re adds
        the tag to the ranges of text delimited in args.

        Example:

        DATA_X = 'It is black.\n'
        DATA_Y = 'It is blue.\n'
        text = Text()
        text.pack()
        text.insert('1.0', DATA_X)
        text.insert('2.0', DATA_Y)
        text.tag_add('X', '1.0', '1.0 lineend')
        text.tag_add('Y', '2.0', '2.0 lineend')
        text.tag_config('X', background='black')
        text.tag_config('Y', foreground='blue')
        text.tag_update(text, 'X', '1.0', 'end', ('2.0', '2.0 lineend'))

        It removes the X tag from '1.0' to 'end' then adds
        the X tag to the range '2.0' '2.0 lineend'. 
        """

        self.tag_remove(name, index0, index1)

        for indi, indj in args:
            self.tag_add(name, indi, indj)

    def insee(self, index, data):
        """
        """

        self.insert(index, data)
        self.see('insert')

    def cmd_like(self):
        """
        """

        data = self.get('insert linestart', 'insert lineend')
        self.delete('insert linestart', 'insert lineend')
        return data

    def indref(self, index):
        """
        This is a short hand function. 
        It is used to convert a Text index
        into two integers.

        Ex:

        a, b = area.indref('insert')

        Now, a and b can be manipulated
        as numbers.
        """

        a, b  = self.index(index).split('.')
        return int(a), int(b)

    def setcur(self, line, col):
        """
        It is used to set the cursor position at
        a given index using line and col.

        line is a number which represents
        a given line index in the AreaVi instance.
    
        col is a column.
        """

        self.mark_set('insert', '%s.%s' % (line, col))
        self.see('insert')

    def setcurl(self, line):
        """
        set cursor line.
        It is used to set the cursor position at a given
        line. It sets the cursor at line.0 position.
        """

        self.mark_set('insert', '%s.%s' % (line, '0'))
        self.see('insert')


    def indint(self, index):
        """ 
        This method is used
        when i can't use self.indref.

        It seems self.indref returns 

        2.10 when the input is 2.34

        it happens when the index col
        is longer than the actual line col.
        """

        a, b = index.split('.')
        return int(a), int(b)

    def indcol(self):
        """
        This is a short hand method for getting
        the last col in which the cursor was in.

        It is useful when implementing functions to
        select pieces of text.
        """

        a, b  = self.indref(self.last_col)
        return int(a), int(b)

    def setcol(self, line, col):
        """
        It sets the mark used by the arrows
        keys and selection state.
        """

        self.mark_set(self.last_col, '%s.%s' % (line, col))

    def indcur(self):
        """
        It returns the actual line, col for the
        cursor position. So, the values can be
        manipulated with integers.
        """

        a, b  = self.indref('insert')
        return int(a), int(b)

    def seecur(self):
        """
        Just a shorthand for area.see('insert')
        which makes the cursor visible wherever it is in.
        """

        self.see('insert')

    def inset(self, index):
        """
        Just a shorthand for area.mark_set('insert', index)
        so we spare some typing.
        """

        self.mark_set('insert', index)


    def is_end(self):
        """
        This function returns True if the cursor is positioned
        at the end of the AreaVi instance.
        
        This is useful when implementing other methods.
        Like those from visual block selection to avoid
        the cursor jumping to odd places when it achieves
        the end of the text region.
        """

        # I have to use 'end -1l linestart' since it seems the 'end' tag
        # corresponds to a one line after the last visible line.
        # So last line lineend != 'end'.

        return self.compare('insert linestart', '!=', 'end -1l linestart')

    def is_start(self):
        """
        This function returns True if the cursor is
        at the start of the text region. It is on index '1.0'
        """

        return self.compare('insert linestart', '!=', '1.0')

    def down(self):
        """  
        It sets the cursor position one line down.  
        """

        if self.is_end():
        # We first check if it is at the end
        # so we avoid the cursor jumping at odd positions.
            a, b = self.indcol()
            c, d = self.indcur()
            self.setcur(c + 1, b)        
        
    def up(self):   
        """  
        It sets the cursor one line up.  
        """

        if self.is_start():
            a, b = self.indcol()
            c, d = self.indcur()
            self.setcur(c - 1, b)
        
    def left(self):
        """  
        It moves the cursor one character left.
        """

        self.mark_set('insert', 'insert -1c')

        # The mark used by self.down, self.up.
        self.mark_set(self.last_col, 'insert')
    
    def right(self):
        """  
        It moves the cursor one character right.
        """

        self.mark_set('insert', 'insert +1c')

        # The mark used by self.down, self.up.
        self.mark_set(self.last_col, 'insert')
    
    def start_selection(self):
        """  
        It sets the mark sel_start to the insert position.

        So, when sel_up, sel_down, sel_right, sel_left are
        called then they will select a region from this mark.  
        """

        self.mark_set('_sel_start_', 'insert')
    
    def start_block_selection(self):
        self.mark_set('_block_sel_start_', 'insert')


    def is_add_up(self, index):
        """
        It checks whether the selection must be
        removed or added.
        
        If it returns True then the selection must be
        removed. True means that the '_sel_start_'
        mark is positioned above the cursor position.
        So, it must remove the selection instead of
        adding it.
        """

        return self.compare('%s linestart' % index, '<=', 'insert linestart')

    def rmsel(self, index0, index1):
        """
        It removes the tag sel from the range that is delimited by index0 and index1
        regardless whether index0 <= index1.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        self.tag_remove('sel', index2, index3)

    def addsel(self, index0, index1):
        """
        It adds the tag sel to the range delimited by index0 and index1 regardless
        whether index0 <= index1.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        self.tag_add('sel', index2, index3)


    def min(self, index0, index1):
        """
        It returns the min between index0 and index1.
        """

        if self.compare(index0, '<=', index1):
            return index0
        else:
            return index1

    def max(self, index0, index1):
        """
        It returns the max between index0 and index1.
        """

        if self.compare(index0, '<=', index1):
            return index1
        else:
            return index0

    def sel_up(self):
        """
        It adds 'sel' one line up the 'insert' position
        and sets the cursor one line up.
        """

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.rmsel(index0, index1)
        self.up()

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.addsel(index0, index1)

    def is_add_down(self, index):
        """
        It returns True if the cursor is positioned below
        the initial mark for selection. 

        It determins if the selection must be removed or added when
        sel_down is called.
        """

        return self.compare('%s linestart' % index, '>=', 'insert linestart')

    def sel_down(self):
        """ 
        It adds or removes selection one line down. 
        """

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.rmsel(index0, index1)
        self.down()

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.addsel(index0, index1)
    

    def is_add_right(self, index):
        """
        It returns True if the cursor is positioned at the left
        of the initial selection mark. It is useful for sel_right method.
        """

        return self.compare(index, '>=', 'insert')

    def sel_right(self):
        """ 
        It adds or removes selection one character right.
        """

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.rmsel(index0, index1)
        self.right()

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.addsel(index0, index1)
    

    def is_add_left(self, index):
        """
        It returns True if the cursor is positioned at the right of
        the initial mark selection.
        """

        return self.compare(index, '<=', 'insert')

    def sel_left(self):
        """ 
        It adds or removes selection one character left.
        """

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.rmsel(index0, index1)
        self.left()

        index0 = self.min('_sel_start_', 'insert')
        index1 = self.max('_sel_start_', 'insert')

        self.addsel(index0, index1)

    def indmsel(self):
        """
        It is just a shorthand for getting the last selection mark.
        """

        a, b = self.indref('_sel_start_')
        return int(a), int(b)

    def addblock(self, index0, index1):
        """
        It adds block selection from index0 to index1.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        a, b   = self.indint(index2)
        c, d   = self.indint(index3)

        for ind in xrange(a, c + 1):
            e = min(b, d)
            f = max(b, d)
            self.addsel('%s.%s' % (ind, e), '%s.%s' % (ind, f))

    def rmblock(self, index0, index1):
        """
        It removes block selection from index0 to index1.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        a, b   = self.indint(index2)
        c, d   = self.indint(index3)

        for ind in xrange(a, c + 1):
            e = min(b, d)
            f = max(b, d)
            self.rmsel('%s.%s' % (ind, e),  '%s.%s' % (ind, f))

    def block_down(self):
        """  
        It adds or removes block selection one line down.  
        """

        a, b   = self.indcol()
        c, d   = self.indcur()

        index = self.index('_block_sel_start_')
        self.rmblock(index, '%s.%s' % (c, b))
        self.down()

        a, b   = self.indcol()
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def block_up(self):
        """  
        It adds or removes block selection one line up.  
        """

        a, b   = self.indcol()
        c, d   = self.indcur()
        index  = self.index('_block_sel_start_')

        self.rmblock(index, '%s.%s' % (c, b))
        self.up()

        a, b = self.indcol()
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def is_line_start(self):
        """
        It returns True if the cursor is at the start of the cursor line.
        """

        return self.compare('insert', '!=', 'insert linestart')

    def block_left(self):
        """
        It adds block selection to the left.
        """

        a, b   = self.indcol()
        c, d   = self.indcur()

        index = self.index('_block_sel_start_')
        self.rmblock(index, '%s.%s' % (c, b))
        self.left()

        a, b   = self.indcol()
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def is_line_end(self):
        """
        It returns True if the cursor is at the end of the cursor line.
        """

        return self.compare('insert', '!=', 'insert lineend')

    def block_right(self):
        """
        It adds a block selection to the right.
        """

        a, b   = self.indcol()
        c, d   = self.indcur()

        index = self.index('_block_sel_start_')
        self.rmblock(index, '%s.%s' % (c, b))
        self.right()

        a, b   = self.indcol()
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

                
    def clear_selection(self):
        """
        It removes 'sel' tag from all ranges.
        """

        try:
            self.tag_remove('sel', 'sel.first', 'sel.last')
        except Exception:
            pass

    def select_char(self):
        """
        it adds 'sel' a char ahead the cursor position.
        """

        self.addsel('insert', 'insert +1c')
    
    def unselect_char(self):
        """
        It removes 'sel' a char from the cursor position.
        """

        self.rmsel('insert', 'insert +1c')

    def clchar(self):
        """
        It deletes a char from the cursor position.
        """

        self.edit_separator()
        self.delete('insert', 'insert +1c')
    
    def do_undo(self):
        """
        It does undo.
        """

        try:
            self.edit_undo()
        except TclError:
            pass
    
    def do_redo(self):
        """
        It redoes.
        """

        try:
            self.edit_redo()
        except TclError:
            pass

    def sel_text_start(self):
        """
        It selects all text from insert position to the start position
        of the text.

        """

        index = self.index('insert')
        self.go_text_start()
        self.addsel(index, 'insert')

    def sel_text_end(self):
        """
        It selects all text from the insert position to the end of the text.
        """

        index = self.index('insert')
        self.go_text_end()
        self.addsel(index, 'insert')

    def go_text_start(self):
        """
        It goes to the first position in the text.
        """

        self.mark_set('insert', '1.0')
        self.see('insert')
    
    def go_text_end(self):
        """
        It goes to the end of the text.
        """

        self.mark_set('insert', 'end linestart')
        self.see('insert')
    
    def sel_line_start(self):
        """
        It adds selection from the insert position to the 
        start of the line.
        """

        index = self.index('insert')
        self.go_line_start()
        self.addsel(index, 'insert')

    def sel_line_end(self):
        """
        It selects all text from insert position to the end of the line.
        """

        index = self.index('insert')
        self.go_line_end()
        self.addsel(index, 'insert')

    def go_line_start(self):
        """
        It goes to the beginning of the cursor position line.
        """

        self.mark_set('insert', 'insert linestart')
        

    def go_line_end(self):
        """
        It goes to the end of the cursor position line.
        """

        self.mark_set('insert', 'insert lineend')

    def go_next_word(self):
        """
        It puts the cursor on the beginning of the next word.
        """

        self.seek_next_down('\M')

    def go_prev_word(self):
        """
        It puts the cursor in the beginning of the previous word.
        """

        self.seek_next_up('\M')

    def go_next_sym(self, chars):
        """
        It puts the cursor on the next occurency of the symbols in chars.
        """

        chars = map(lambda ind: escape(ind), chars)
        REG   = '|'.join(chars)
        self.seek_next_down(REG)

    def go_prev_sym(self, chars):
        """
        It puts the cursor on the previous occurency of:
        """

        chars = map(lambda ind: escape(ind), chars)
        REG   = '|'.join(chars)
        self.seek_next_up(REG)
    
    def cllin(self):
        """
        It deletes the cursor position line, makes the cursor visible
        and adds a separator to the undo stack.
        """

        self.edit_separator()
        self.delete('insert linestart', 'insert +1l linestart')
        self.see('insert')
    

    def cpsel(self):
        """
        It copies to the clip board ranges of text
        that are selected and removes the selection.
        """

        data = self.join_ranges('sel')
        self.clipboard_clear()
        self.clipboard_append(data)
        self.tag_remove('sel', 'sel.first', 'sel.last')
    

    def cpblock(self):
        """
        It copies blocks of text that are selected
        with a separator '\n'.
        """
        data = self.join_ranges('sel', '\n')
        self.clipboard_clear()
        self.clipboard_append(data)
        self.tag_remove('sel', 'sel.first', 'sel.last')
    

    def ctblock(self):
        """
        It cuts blocks of text with a separator '\n'.
        """

        data = self.join_ranges('sel', '\n')
        self.clipboard_clear()
        self.clipboard_append(data)
        self.edit_separator()
        self.delete_ranges('sel')
    

    def ctsel(self):
        """
        It cuts the selected text.
        """

        data = self.join_ranges('sel')
        self.clipboard_clear()
        self.clipboard_append(data)
        self.edit_separator()
        self.delete_ranges('sel')


    def clsel(self):
        """
        It deletes all selected text.
        """
        self.edit_separator()
        self.delete_ranges('sel')
    

    def ptsel(self):
        """
        It pastes over the cursor position data from the clipboard 
        and adds a separator.
        """

        data = self.clipboard_get()
        self.edit_separator()
        self.insert('insert', data)
    

    def ptsel_after(self):
        """
        It pastes one line after the cursor position data from clipboard
        and adds a separator.
        """

        data = self.clipboard_get()
        self.edit_separator()
        self.insert('insert +1l linestart', data)


    def ptsel_before(self):
        """
        It pastes data from the cursor position one line before the cursor
        position and adds a separator.
        """

        data = self.clipboard_get()
        self.edit_separator()
        self.insert('insert linestart', data)


    def select_line(self):
        """
        It adds selection to the cursor position line.
        """

        self.tag_add('sel', 'insert linestart', 'insert +1l linestart')

    def unselect_line(self):
        """
        It removes selection from the cursor position line.
        """

        self.tag_remove('sel', 'insert linestart', 'insert +1l linestart')


    def toggle_line_selection(self):
        map = self.is_tag_range('sel', 'insert linestart', 'insert +1l linestart')

        if map:
            self.unselect_line()
        else:
            self.select_line()


    def select_word(self):
        """
        It selects a word from the cursor position.
        """

        index1 = self.search('\W', 'insert', regexp=True, stopindex='insert linestart', backwards=True)
        index2 = self.search('\W', 'insert', regexp=True, stopindex='insert lineend')
        self.tag_add('sel', 'insert linestart' if not index1 else '%s +1c' % index1, 
                     'insert lineend' if not index2 else index2)
    

    def scroll_line_up(self):
        """
        It scrolls one line up
        """

        self.yview(SCROLL, -1, 'units')
        is_visible = self.dlineinfo('insert')
        if not is_visible:
            self.mark_set('insert', 'insert -1l')
    
    def scroll_line_down(self):
        """
        It scrolls one line down.
        """

        self.yview(SCROLL, 1, 'units')
        is_visible = self.dlineinfo('insert')
        if not is_visible:
            self.mark_set('insert', 'insert +1l')
    

    def scroll_page_down(self):
        """
        It goes one page down.
        """
        self.yview(SCROLL, 1, 'page')
        self.mark_set('insert', '@0,0')


    def scroll_page_up(self):
        """
        It goes one page up.
        """

        self.yview(SCROLL, -1, 'page')
        self.mark_set('insert', '@0,0')
    
    def insert_line_down(self):
        """
        It inserts one line down from the cursor position.
        """

        self.edit_separator()
        self.insert('insert +1l linestart', '\n')
        self.mark_set('insert', 'insert +1l linestart')
        self.see('insert')
    
    def select_all(self):
        """
        It selects all text.
        """

        self.tag_add('sel', '1.0', 'end')

    def insert_line_up(self):
        """
        It inserts one line up.
        """

        self.edit_separator()
        self.insert('insert linestart', '\n')
        self.mark_set('insert', 'insert -1l linestart')
        self.see('insert')


    def shift_sel_right(self, width, char):
        """

        """
        srow, scol = self.indref('sel.first')
        erow, ecol = self.indref('sel.last')
        self.shift_right(srow, erow, width, char)
    
    def shift_sel_left(self, width):
        """

        """

        srow, scol = self.indref('sel.first')
        erow, ecol = self.indref('sel.last')
        self.shift_left(srow, erow, width)
    
    def shift_right(self, srow, erow, width, char):
        """
        Given a start row and a end row it shifts
        a block of text to the right.
        
        This is specially useful when working with
        source code files.
        """

        self.edit_separator()
        for ind in xrange(srow, erow + 1):
            self.insert('%s.0' % ind, width * char) 
    

    def shift_left(self, srow, erow, width):
        """
        Given a start row and a end row it shifts
        a block of text to the left.


        This is specially useful when working with
        source code files.
        """

        self.edit_separator()
        for ind in xrange(srow, erow + 1):
            self.delete('%s.0' % ind, '%s.%s' % (ind, width)) 
    

    def tag_find_ranges(self, name, regex, *args, **kwargs):
        """
        It returns an interator corresponding to calling AreaVi.find
        between the ranges of the tag specified by name.

        You shouldn't delete or insert data while performing this operation.
        """
        
        # It should be built on top of nextrange.
        map = self.tag_ranges(name)
        for indi in range(0, len(map) - 1, 2):
            seq = self.find(regex, map[indi], map[indi + 1], *args, **kwargs)
            for indj in seq: 
                yield indj

    def tag_replace_ranges(self, name, regex, data, index='1.0', stopindex='end', 
                           *args, **kwargs):
        """
        It replaces all occurrences of regex inside a tag ranges
        for data.

        name     - Name of the tag.
        regex    - The pattern.
        data     - The data to replace.
        args     - Arguments given to AreaVi.find.
        **kwargs - A dictionary of arguments given to AreaVi.find.
        """

        while True:
            map = self.tag_nextrange(name, index, stopindex)
            if not map: break

            index3, index4 = map
            index = index4

            self.replace_all(regex, data, index3, index4, *args, **kwargs)

    def setup_tags_conf(self, kwargs):
        """
        kwargs is a dictionary like:

        kwargs = {'tag_name': {'background': 'blue'}}

        In the kwargs above, this method would set the background value to 'blue'
        for the tag named 'tag_name'.
        """

        for name, kwargs in kwargs.iteritems():
            self.tag_config(name, **kwargs)
            self.tag_lower(name)
    
    def tag_add_found(self, name, map):
        """"
        It adds a tag to the match ranges from either AreaVi.find or
        AreaVi.tag_find_ranges.
    
        name - The tag to be added.
        map  - An iterator from AreaVi.find or AreaVi.tag_find_ranges.
        """

        for _, index0, index1 in map:
            self.tag_add(name, index0, index1)

    def split_with_cond(self, regex, cond, *args, **kwargs):
        """
        It determines which chunks should be yielded based on cond.
        """

        for chk, index0, index1 in self.split(regex, *args, **kwargs):
            data = cond(chk, index0, index1)
            if data: yield data

    def split(self, *args, **kwargs):
        """
        It splits the contents of the text widget into chunks based on a regex.
        """

        index0 = '1.0'
        for chk, index1, index2 in self.find(*args, **kwargs):
            if self.compare(index1, '>', index0): 
                yield(self.get(index0, index1), index0, index1)
            
            yield(chk, index1, index2)
            index0 = index2
    

    def find_with_cond(self, regex, cond, *args, **kwargs):
        """
        It determines which matches should be yielded.
        """

        for chk, index0, index1 in self.find(regex, *args, **kwargs):
            data = cond(chk, index0, index1)
            if not data: continue
            yield(data)
            
    def find_one_by_line(self, regex, index, stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None):

        count = IntVar()

        while True:
            index = self.search(regex, index, stopindex, exact=exact, nocase=nocase, 
                                nolinestop=nolinestop, regexp=regexp, elide=elide, count=count)

            if not index:
                break

            len   = count.get()
            tmp   = '%s +%sc' % (index, len)
            chunk = self.get(index, tmp)

            pos0  = self.index(index)
            pos1  = self.index('%s +%sc' % (index, len))
            index = '%s +1l' % pos0
            yield(chunk, pos0, pos1)

    def find(self, regex, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None):
        """
        It returns an iterator of matches. It is based on the Text.search method

        """

        count = IntVar()

        while True:
            index = self.search(regex, index, stopindex, exact=exact, nocase=nocase, 
                                nolinestop=nolinestop, regexp=regexp, elide=elide, count=count)

            if not index:
                break

            len   = count.get()
            tmp   = '%s +%sc' % (index, len)
            chunk = self.get(index, tmp)

            pos0  = self.index(index)
            pos1  = self.index('%s +%sc' % (index, len))
            index = '%s +1c' % tmp
            yield(chunk, pos0, pos1)

    def search(self, pattern, index, stopindex=None, forwards=None,
                backwards=None, exact=None, regexp=None, nocase=None,
                count=None, elide=None, nolinestop=None):
            
        '''Standard search method, but with support for the nolinestop
        option which is new in tk 8.5 but not supported by tkinter out
        of the box.
        '''
    
        args = [self._w, 'search']
        if forwards: args.append('-forwards')
        if backwards: args.append('-backwards')
        if exact: args.append('-exact')
        if regexp: args.append('-regexp')
        if nocase: args.append('-nocase')
        if elide: args.append('-elide')
        if nolinestop: args.append("-nolinestop")
        if count: args.append('-count'); args.append(count)
        if pattern and pattern[0] == '-': args.append('--')
        args.append(pattern)
        args.append(index)
        if stopindex: args.append(stopindex)
    
        return str(self.tk.call(tuple(args)))

    def seek_next_up(self, regex, index0='insert', stopindex='1.0', exact=None, regexp=True, 
                        nocase=None, elide=None, nolinestop=None):
        """
        Find the next match with regex up the cursor.
        It sets the cursor at the index of the occurrence.
        """

        count = IntVar()
        index = self.search(regex, index0, stopindex=stopindex, regexp=regexp, exact=exact, 
                            nocase=nocase, elide=elide, nolinestop=nolinestop, backwards=True, count=count)
        if not index: return

        index1 = self.index('%s +%sc' % (index, count.get())) 
        self.mark_set('insert', index)
        self.see('insert')

        return index, index1

    def seek_next_down(self, regex, index0='insert', stopindex='end', exact=None, regexp=True, 
                       nocase=None, elide=None, nolinestop=None):

        """
        Find the next match with regex down.
        It sets the cursor at the index of the occurrence.
        """

        count = IntVar()

        index = self.search(regex, index0, stopindex=stopindex, regexp=regexp, exact=exact, nocase=nocase, 
                            elide=elide, nolinestop=nolinestop, count=count)

        if not index: return

        index1 = self.index('%s +%sc' % (index, count.get())) 
        self.mark_set('insert', index1)
        self.see('insert')

        return index, index1

    def pick_next_up(self, name, *args, **kwargs):

        """
        """

        index = self.seek_next_up(*args, **kwargs)
        if not index:
            return

        self.tag_add(name, *index)
        return index

    def pick_next_down(self, name, *args, **kwargs):

        """
        """

        index = self.seek_next_down(*args, **kwargs)

        if not index:    
            return

        self.tag_add(name, *index)
        return index

    def replace(self, regex, data, index=None, stopindex=None, forwards=None,
                backwards=None, exact=None, regexp=True, nocase=None, elide=None, nolinestop=None):

        """
        It is used to replace occurrences of a given match.

        It is possible to use a callback function to return what is replaced 
        as well.
        """

        count = IntVar()
        index = self.search(regex, index, stopindex, forwards=forwards, backwards=backwards, exact=exact, nocase=nocase, 
                            nolinestop=nolinestop, regexp=regexp, elide=elide, count=count)

            
        if not index: return

        if callable(data): data = data(index, self.index('%s +%sc' % (index, count.get())))

        index0 = self.index('%s +%sc' % (index, count.get()))
        self.delete(index, index0)
        self.insert(index, data)

        return index, len(data)

    def replace_all(self, regex, data, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None):
        """
        It is used to replace all occurrences of a given match in a range.
        It accepts a callback function that determines what is replaced.
        """

        # It is needed because the range will grow
        # when data is inserted, the intent is searching
        # over a pre defined range.
        self.mark_set(self.STOP_REPLACE_INDEX, stopindex)

        while True:
            map = self.replace(regex, data, index, self.STOP_REPLACE_INDEX, exact=exact, nocase=nocase, 
                               nolinestop=nolinestop, regexp=regexp, elide=elide)

            if not map: return

            index, size = map
            index = self.index('%s +%sc' % (index, size))

    def get_paren_search_dir(self, start, end):
        """

        """

        char  = self.get('insert', 'insert +1c')
        if char == start:
            return False
        elif char == end:
            return True
        else:
            return None

    def get_paren_search_sign(self, start, end):
        """

        """

        char  = self.get('insert', 'insert +1c')
        if char == start:
            return '+'
        elif char == end:
            return '-'
        else:
            return None

    def select_case_pair(self, pair, MAX=1500):
        """

        """

        index = self.case_pair(MAX, *pair)
        if not index: return
    
        min = self.min(index, 'insert')
        if self.compare(min, '==', 'insert'): min = '%s +1c' % min
    
        max = self.max(index, 'insert')
        if self.compare(max, '==', 'insert'): min = '%s +1c' % min
    
        self.tag_add('sel', min, max)
    
    def case_pair(self, max, start='(', end=')'):
        """
        Once this method is called, it returns an index for the next
        matching parenthesis or None if the char over the cursor
        isn't either '(' or ')'.
        """

        dir = self.get_paren_search_dir(start, end)

        # If dir is None then there is no match.
        if dir == None: return ''

        REG   = '\%s|\%s' % (start, end)
        sign  = self.get_paren_search_sign(start, end)
        count = 0

        # If we are searching fowards we don't need
        # to add 1c.

        index = 'insert %s' % ('+1c' if dir else '')
        size  = IntVar(0)

        while True:
            index = self.search(REG, index     = index,
                                     stopindex = 'insert %s%sc' % (sign, max),
                                     count     = size, 
                                     backwards = dir, 
                                     regexp    = True) 

            if not index: return ''

            char  = self.get(index, '%s +1c' % index)
            count = count + (1 if char == start else -1)

            if not count: 
                return index

            # When we are searching backwards we don't need
            # to set a character back because index will point
            # to the start of the match.
            index = '%s %s' % (index, '+1c' if not dir else '')
                

    def clear_data(self):
        """
        It clears all text inside an AreaVi instance.
        """
        import os
        
        self.delete('1.0', 'end')
        self.filename = os.path.abspath(self.default_filename)
        self.event_generate('<<ClearData>>')

    def load_data(self, filename):
        """
        It dumps all text from a file into an AreaVi instance.
        
        filename - Name of the file.
        """
        import os
        filename      = os.path.abspath(filename)        
        self.filename = filename
        fd            = open(filename, 'r')
        data          = fd.read()
        fd.close()

        # i could generate a tk event here.
        try:
            data = data.decode(self.charset)
        except UnicodeDecodeError:
            self.charset = ''

        self.delete('1.0', 'end')
        self.insert('1.0', data)
        self.event_generate('<<LoadData>>')
        type, _ = mimetypes.guess_type(self.filename)
        self.event_generate('<<Load-%s>>' % type)

    def decode(self, name):
        self.charset = name
        self.load_data(self.filename)

    def save_data(self):
        """
        It saves the actual text content in the current file.
        """

        data = self.get('1.0', 'end')
        data = data.encode(self.charset)
        fd   = open(self.filename, 'w')
        fd.write(data)
        fd.close()
        self.event_generate('<<SaveData>>')

        type, _ = mimetypes.guess_type(self.filename)
        self.event_generate('<<Save-%s>>' % type)

    def save_data_as(self, filename):
        """
        It saves the content of the given AreaVi instance into
        a file whose name is specified in filename.


        filename - Name of the file to save the data.
        """

        self.filename = filename
        self.save_data()


    def is_tag_range(self, name, index0, index1):
        """
        """ 

        ranges = self.tag_ranges(name)
        for ind in xrange(0, len(ranges) - 1, 2):
            if self.is_subrange(index0, index1, ranges[ind].string, 
                                ranges[ind + 1].string):
                return ranges[ind].string, ranges[ind + 1].string

    def is_in_range(self, index, index0, index1):
        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        r1     = self.compare(index2, '<=', index)
        r2     = self.compare(index3, '>=', index)

        if r1 and r2: return True
        else: return False

    def is_subrange(self, index0, index1, index2, index3):
        r1 = self.is_in_range(index0, index2, index3)
        r2 = self.is_in_range(index1, index2, index3)
        return r1 and r2

    def replace_range(self, data, index0, index1):
        self.delete(index0, index1)
        self.insert(index0, data)

    def replace_ranges(self, name, data, index0='1.0', index1='end'):
        """
        It replaces ranges of text that are mapped to a tag name for data between index0
        and index1.
        """

        while True:
            range = self.tag_nextrange(name, index0, index1)
            if not range: break
            self.replace_range(data, *range)

    def delete_ranges(self, name, index0='1.0', index1='end'):
        """
        It deletes ranges of text that are mapped to tag name between index0 and index1.
        """

        self.replace_ranges(name, '', index0, index1)

    def join_ranges(self, name, sep=''):
        """     
        """

        data = ''
    
        for ind in self.get_ranges(name):
            data = data + ind + sep
        return data


    def get_ranges(self, name):
        """
        """

        ranges = self.tag_ranges(name)
        for ind in xrange(0, len(ranges) - 1, 2):
            data = self.get(ranges[ind], ranges[ind + 1])
            yield(data)


    def mark_set_next(self, tag, mark):
        """

        """

        next_tag = self.tag_nextrange(tag, '%s +1c' % mark)
        if next_tag:
            self.mark_set(mark, next_tag[0])
    
    def mark_set_prev(self, tag, mark):
        """

        """

        prev_tag = self.tag_prevrange(tag, mark)
        if prev_tag:
            self.mark_set(mark, prev_tag[0])
    
    def tag_prev_occur(self, tag_names, index0, index1, default):
        for ind in tag_names:
            pos = self.tag_prevrange(ind, index0, index1)
            if pos: return pos[1]
        return default
    
    def tag_next_occur(self, tag_names, index0, index1, default):
        for ind in tag_names:
            pos = self.tag_nextrange(ind, index0, index1)
            if pos: return pos[0]
        return default
    
    @staticmethod
    def get_all_areavi_instances(wid):
        for ind in wid.winfo_children():
            if isinstance(ind, AreaVi):
                yield ind
            else:
                for ind in AreaVi.get_all_areavi_instances(ind):
                    yield ind

    @staticmethod
    def get_opened_files(wid):
        map = dict()
        for ind in AreaVi.get_all_areavi_instances(wid):
            map[ind.filename] = ind
        return map
    
    @staticmethod
    def find_on_all(wid, chunk):
        for indi in AreaVi.get_all_areavi_instances(wid):
            it = indi.find(chunk, '1.0', 'end')
    
            for indj in it:
                yield indi, indj
    
    def get_cursor_word(self):
        """

        """

        if self.compare('insert', '==', 'insert linestart'):
            return ''

        index = self.search(' ', 'insert', 
                                      stopindex='insert linestart',regexp=True, 
                                      backwards=True)

        if not index: index = 'insert linestart'
        else: index = '%s +1c' % index
        if self.compare(index, '==', 'insert'): return ''
        data = self.get(index, 'insert')
        return data, index
    
    def match_word(self, wid, delim=' '):
        data, index = self.get_cursor_word()
        for area, (chk, pos0, pos1) in self.find_on_all(wid, '[^ ]*%s[^ ]+' % data):
            yield chk, index

    def complete_word(self, wid):
        seq   = self.match_word(wid)
        table = []

        for data, index in seq:
            if not data in table:
                table.append(data)
            else:
                continue

            self.delete(index, 'insert')
            self.insert(index, data)
            yield











