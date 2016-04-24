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
        """

        Text.__init__(self, *args, **kwargs)
        self.setup = dict()

        # Maybe it should be?
        # abspath(default_filename)
        self.default_filename = default_filename

        # The file's path and name.
        self.filename = default_filename

        self.mark_set('(CURSOR_LAST_COL)', '1.0')
        self.mark_set('(RANGE_SEL_MARK)', '1.0')
        self.mark_set('(BLOCK_SEL_MARK)', '1.0')

        # def cave(event):
            # AreaVi.ACTIVE = event.widget
        # self.hook(-1, '<FocusIn>', cave)
        AreaVi.ACTIVE        = self
        self.charset         = 'utf-8'

    def active(self):
        """
        It is used to create a model of target for plugins
        defining python functions to access the AreaVi instance that was
        set as target.
        
        Plugins that expose python functions to be executed from vy
        should access AreaVi.ACTIVE when having to manipulate some AreaVi
        instance content.
        """

        AreaVi.ACTIVE = self

    def chmode(self, id):
        """
        This function is used to change the AreaVi instance's mode.
        It receives one parameter named id which means the
        mode name.

        area = AreaVi('None')
        area.chmode('INSERT')

        It would make area be in INSERT mode.
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

        def install(area):
            area.add_mode('MODE')

        The code above would add a mode named MODE to the AreaVi instance.

        def install(area):
            area.add_mode('TYPING', opt=True)

        The code above would add a mode named 'TYPING' that is possible to edit
        the content of the AreaVi instance. It means that keystrokes that maps
        printable characters it would be dropped over the AreaVi instance that has focus.
        """

        self.setup[id] = opt

    def del_mode(self, id):
        """
        """

        pass

    def hook(self, id, seq, callback, add=True):
        """
        This method is used to hook a callback to a sequence
        specified with its mode:
        
        def callback(event):
            event.widget.insert('An event happened!')

        def install(area):
            area.hook(('INSERT' '<Key-i>', callback))

        In the example above, whenever the event <Key-i> happens then
        the function named callback will be called with the event object.
        """

        MODE_Y = 'mode%s%s' % (self, id)

        self.bind_class(MODE_Y, seq, callback, add)


    def unhook(self, id, seq):
        """
        The opposite of AreaVi.hook.
    
        area.unhook('mode' '<Event>')
        """

        MODE_Y = 'mode%s%s' % (self, id)
        self.unbind_class(MODE_Y, seq)

    def install(self, *args):
        """
        It is a shorthand for AreaVi.hook. It is used as follows:

        def install(area):
            area.install(('MODE1', '<Event1>', callback1),
                         ('MODE2', '<Event2>', callback2),
                         ('MODE3', '<Event3>', callback3), ...)
        """

        for ind in args:
            self.hook(*ind)

    def uninstall(self, *args):
        """
        The opposite of AreaVi.install.

        area.uninstall(('mode', '<Event>'), ...)
        """

        for id, seq, callback in args:
            self.unhook(id, seq, callback)

    def append(self, data):
        """
        This method is used to insert data to the end of the AreaVi instance widget
        and place the cursor at the end of the data that was appended. It makes the cursor
        visible.
        """

        self.insert('end', data)
        self.mark_set('insert', 'end')
        self.see('end')

    def curline(self):
        """
        This method returns the string that corresponds to the cursor line.
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
        This method inserts data at index position then makes the cursor visible.
        """

        self.insert(index, data)
        self.see('insert')

    def cmd_like(self):
        """
        This method retrieves the cursor line then deletes it afterwards.
        """

        data = self.get('insert linestart', 'insert lineend')
        self.delete('insert linestart', 'insert lineend')
        return data

    def indref(self, index):
        """
        This is a short hand function. It is used to convert a Text index
        into two integers like:

        a, b = area.indref('insert')

        Now, a and b can be manipulated
        as numbers.
        """

        a, b  = self.index(index).split('.')
        return int(a), int(b)

    def setcur(self, line, col='0'):
        """
        It is used to set the cursor position at a given index using line 
        and col. 
        """

        self.mark_set('insert', '%s.%s' % (line, col))
        self.see('insert')

    def indint(self, index):
        """ 
        Just a shorthand for:
        
        a, b = index.split('2.3')
        a, b = int(a), int(b)
        """

        a, b = index.split('.')
        return int(a), int(b)

    def indcur(self):
        """
        It returns two integers that corresponds to the cursor
        position line and col.
        """

        a, b  = self.indref('insert')
        return int(a), int(b)

    def seecur(self, index):
        """
        Just a shorthand for:

        area.mark_set('insert', index)
        area.see('insert')
        """

        self.mark_set('insert', index)
        self.see('insert')

    def is_end(self):
        """
        This function returns True if the cursor is positioned
        at the end of the AreaVi instance.
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

        if not self.is_end():
            return

        a, b = self.indref('(CURSOR_LAST_COL)')
        c, d = self.indcur()
        self.setcur(c + 1, b)        
    
    def up(self):   
        """  
        It sets the cursor one line up.  
        """

        if not self.is_start():
            return

        a, b = self.indref('(CURSOR_LAST_COL)')
        c, d = self.indcur()
        self.setcur(c - 1, b)
    
    def left(self):
        """  
        It moves the cursor one character left.
        """

        self.mark_set('insert', 'insert -1c')

        # The mark used by self.down, self.up.
        self.mark_set('(CURSOR_LAST_COL)', 'insert')
    
    def right(self):
        """  
        It moves the cursor one character right.
        """

        self.mark_set('insert', 'insert +1c')

        # The mark used by self.down, self.up.
        self.mark_set('(CURSOR_LAST_COL)', 'insert')
    
    def start_selection(self):
        """  
        Start range selection.
        """

        self.mark_set('(RANGE_SEL_MARK)', 'insert')
    
    def start_block_selection(self):
        """
        Start block selection.
        """

        self.mark_set('(BLOCK_SEL_MARK)', 'insert')

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

        self.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.up()
        self.addsel('(RANGE_SEL_MARK)', 'insert')

    def sel_down(self):
        """ 
        It adds or removes selection one line down. 
        """

        self.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.down()
        self.addsel('(RANGE_SEL_MARK)', 'insert')
    
    def sel_right(self):
        """ 
        It adds or removes selection one character right.
        """


        self.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.right()
        self.addsel('(RANGE_SEL_MARK)', 'insert')
    
    def sel_left(self):
        """ 
        It adds or removes selection one character left.
        """

        self.rmsel('(RANGE_SEL_MARK)', 'insert')
        self.left()
        self.addsel('(RANGE_SEL_MARK)', 'insert')

    def addblock(self, index0, index1):
        """
        It adds block selection from index0 to index1.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        a, b   = self.indint(index2)
        c, d   = self.indint(index3)

        for ind in xrange(a, c + 1):
            self.addsel('%s.%s' % (ind, min(b, d)), '%s.%s' % (ind, max(b, d)))

    def rmblock(self, index0, index1):
        """
        It removes block selection from index0 to index1.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        a, b   = self.indint(index2)
        c, d   = self.indint(index3)

        for ind in xrange(a, c + 1):
            self.rmsel('%s.%s' % (ind, min(b, d)),  '%s.%s' % (ind, max(b, d)))

    def block_down(self):
        """  
        It adds or removes block selection one line down.  
        """

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d   = self.indcur()

        index = self.index('(BLOCK_SEL_MARK)')
        self.rmblock(index, '%s.%s' % (c, b))
        self.down()

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def block_up(self):
        """  
        It adds or removes block selection one line up.  
        """

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d   = self.indcur()
        index  = self.index('(BLOCK_SEL_MARK)')

        self.rmblock(index, '%s.%s' % (c, b))
        self.up()

        a, b = self.indref('(CURSOR_LAST_COL)')
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

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d   = self.indcur()

        index = self.index('(BLOCK_SEL_MARK)')
        self.rmblock(index, '%s.%s' % (c, b))
        self.left()

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

    def is_line_end(self):
        """
        It returns True if the cursor is at the end of the cursor line.
        """

        return self.compare('insert', '!=', 'insert lineend')

    def block_right(self):
        """
        It adds/removes block selection to the right.
        """

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d   = self.indcur()

        index = self.index('(BLOCK_SEL_MARK)')
        self.rmblock(index, '%s.%s' % (c, b))
        self.right()

        a, b   = self.indref('(CURSOR_LAST_COL)')
        c, d = self.indcur()

        self.addblock(index, '%s.%s' % (c, b))

                
    def clear_selection(self):
        """
        Unselect all text.
        """

        try:
            self.tag_remove('sel', 'sel.first', 'sel.last')
        except Exception:
            pass

    def select_char(self):
        """
        Select the cursor char.
        """

        self.addsel('insert', 'insert +1c')
    
    def unselect_char(self):
        """
        Unselect the cursor char.
        """

        self.rmsel('insert', 'insert +1c')

    def del_char(self):
        """
        It deletes a char from the cursor position.
        """

        self.edit_separator()
        self.delete('insert', 'insert +1c')

    def echo(self, data):
        self.insert('insert', data)

    def echo_num(self, keysym_num):
        try:
            self.echo(chr(keysym_num))
        except ValueError:
            pass

    def backspace(self):
        """
        """

        self.delete('insert -1c', 'insert')

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
        It selects all text from cursor position to the start position
        of the text.

        """

        index = self.index('insert')
        self.go_text_start()
        self.addsel(index, 'insert')

    def sel_text_end(self):
        """
        It selects all text from the cursor position to the end of the text.
        """

        index = self.index('insert')
        self.go_text_end()
        self.addsel(index, 'insert')

    def go_text_start(self):
        """
        Place the cursor at the beginning of the file.
        """

        self.mark_set('insert', '1.0')
        self.see('insert')
    
    def go_text_end(self):
        """
        Place the cursor at the end of the file.
        """

        self.mark_set('insert', 'end linestart')
        self.see('insert')
    
    def sel_line_start(self):
        """
        It adds selection from the cursor position to the 
        start of the line.
        """

        index = self.index('insert')
        self.go_line_start()
        self.addsel(index, 'insert')

    def sel_line_end(self):
        """
        It selects all text from the cursor position to the end of the line.
        """

        index = self.index('insert')
        self.go_line_end()
        self.addsel(index, 'insert')

    def go_line_start(self):
        """
        Place the cursor at the beginning of the line.
        """

        self.mark_set('insert', 'insert linestart')
        

    def go_line_end(self):
        """
        Place the cursor at the end of the line.
        """

        self.mark_set('insert', 'insert lineend')

    def go_next_word(self):
        """
        Place the cursor at the next word.
        """

        self.seek_next_down('\M')

    def go_prev_word(self):
        """
        Place the cursor at the previous word.
        """

        self.seek_next_up('\M')

    def go_next_sym(self, chars):
        """
        Place the cursor at the next occurrence of one of the chars.
        """

        chars = map(lambda ind: escape(ind), chars)
        REG   = '|'.join(chars)
        self.seek_next_down(REG)

    def go_prev_sym(self, chars):
        """
        Place the cursor at the previous occurrence of one of the chars.
        """

        chars = map(lambda ind: escape(ind), chars)
        REG   = '|'.join(chars)
        self.seek_next_up(REG)
    
    def del_line(self):
        """
        It deletes the cursor line, makes the cursor visible
        and adds a separator to the undo stack.
        """

        self.edit_separator()
        self.delete('insert linestart', 'insert +1l linestart')
        self.see('insert')
    

    def cpsel(self):
        """
        Copy selected text to the clipboard.
        """

        data = self.join_ranges('sel')
        self.clipboard_clear()
        self.clipboard_append(data)
        self.tag_remove('sel', 'sel.first', 'sel.last')
    

    def cpblock(self):
        """
        Copy ranges of selected text using the separator '\n'.
        """
        data = self.join_ranges('sel', '\n')
        self.clipboard_clear()
        self.clipboard_append(data)
        self.tag_remove('sel', 'sel.first', 'sel.last')
    

    def ctblock(self):
        """
        Cut ranges of selected text using the separator '\n'.
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


    def del_sel(self):
        """
        It deletes all selected text.
        """
        self.edit_separator()
        self.delete_ranges('sel')
    

    def ptsel(self):
        """
        Paste text at the cursor position.
        """

        data = self.clipboard_get()
        self.edit_separator()
        self.insert('insert', data)
    

    def ptsel_after(self):
        """
        Paste text one line down the cursor position.
        """

        data = self.clipboard_get()
        self.edit_separator()
        self.insert('insert +1l linestart', data)


    def ptsel_before(self):
        """
        Paste text one line up the cursor position.
        """

        data = self.clipboard_get()
        self.edit_separator()
        self.insert('insert linestart', data)


    def select_line(self):
        """
        It adds selection to the cursor line.
        """

        self.tag_add('sel', 'insert linestart', 'insert +1l linestart')

    def unselect_line(self):
        """
        It removes selection from the cursor line.
        """

        self.tag_remove('sel', 'insert linestart', 'insert +1l linestart')


    def toggle_line_selection(self):
        """
        Toggle line selection.
        """

        self.toggle_sel('insert linestart', 'insert +1l linestart')

    def toggle_sel(self, index0, index1):
        """
        Toggle selection in the range defined by index0 and index1.
        """

        self.toggle_range('sel', index0, index1)


    def toggle_range(self, name, index0, index1):
        """
        Toggle tag name in the range defined by index0 and index1.
        It means it adds a tag name to the range index0 and index1 if there is no
        tag mapped to that range otherwise it removes the tag name from the range.
        """

        index2 = index0
        index0 = self.min(index0, index1)
        index1 = self.max(index2, index1)

        map = self.is_tag_range(name, index0, index1)
        if map:
            self.tag_remove(name, index0, index1)
        else:
            self.tag_add(name, index0, index1)

    def select_word(self, index='insert'):
        """
        Select the closest word from the cursor.
        """

        index1, index2 = self.get_word_range(index)
        self.tag_add('sel', index1, index2)
    
    def get_word_range(self, index):
        index1 = self.search('\W', index, regexp=True, stopindex='%s linestart' % index, backwards=True)
        index2 = self.search('\W', index, regexp=True, stopindex='%s lineend' % index)
        index1 = '%s linestart' % index if not index1 else '%s +1c' % index1
        index2 = '%s lineend' % index if not index2 else index2
        return index1, index2

    def select_seq(self, index='insert'):
        """
        Select the closest sequence of non blank characters from the cursor.
        """

        index1, index2 = self.get_seq_range(index)
        self.tag_add('sel', index1, index2)

    def get_seq_range(self, index):
        index1 = self.search(' ', index, regexp=True, stopindex='%s linestart' %index, backwards=True)
        index2 = self.search(' ', index, regexp=True, stopindex='%s lineend' % index)
        index1 = '%s linestart' % index if not index1 else '%s +1c' % index1
        index2=  '%s lineend' % index if not index2 else index2
        return index1, index2

    def get_seq(self, index='insert'):
        return self.get(*self.get_seq_range(index))

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
        It scrolls one page down.
        """
        self.yview(SCROLL, 1, 'page')
        self.mark_set('insert', '@0,0')


    def scroll_page_up(self):
        """
        It scrolls one page up.
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
        Shift ranges of selected text to the right.
        """
        srow, scol = self.indref('sel.first')
        erow, ecol = self.indref('sel.last')
        self.shift_right(srow, erow, width, char)
    
    def shift_sel_left(self, width):
        """
        Shift ranges of selected text to the left.
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
    

    def collect(self, name, regex, *args, **kwargs):
        """
        The code below would find for 'PATTERN' in all selected text of an
        AreaVi instance:
        
        for data, pos0, pos1 in area.collect('sel', 'PATTERN'):
            pass
        """
        
        # It should be built on top of nextrange.
        map = self.tag_ranges(name)
        for indi in range(0, len(map) - 1, 2):
            seq = self.find(regex, map[indi], map[indi + 1], *args, **kwargs)
            for indj in seq: 
                yield indj

    def replace_ranges(self, name, regex, data, index='1.0', stopindex='end', 
                           *args, **kwargs):
        """
        It replaces all occurrences of regex in the ranges that are mapped to tag name.

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
            index = self.replace_all(regex, data, index3, index4, *args, **kwargs)

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
    
    def map_matches(self, name, matches):
        """"
        It adds a tag to the match ranges from either AreaVi.find or
        AreaVi.collect.
    
        name - The tag to be added.
        map  - An iterator from AreaVi.find or AreaVi.collect.
        """

        for _, index0, index1 in matches:
            self.tag_add(name, index0, index1)

    def tokenize(self, *args, **kwargs):
        """
        It tokenizes the contents of an AreaVi widget based on a regex.
        The *args, **kwargs are the same passed to AreaVi.find method.

        for token, index0, index1 in area.tokenize(PATTERN):
            pass
        """

        index0 = '1.0'
        for chk, index1, index2 in self.find(*args, **kwargs):
            if self.compare(index1, '>', index0): 
                yield(self.get(index0, index1), index0, index1)
            
            yield(chk, index1, index2)
            index0 = index2
    
    def find(self, regex, index='1.0', stopindex='end', exact=None, regexp=True, nocase=None, 
             elide=None, nolinestop=None, step=''):
        """
        It returns an iterator of matches. It is based on the Text.search method.

        for match, index0, index1 in area.find('pattern'):
            passs
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
            index = '%s%s' % (tmp, step)

            yield(chunk, pos0, pos1)

    def search(self, pattern, index, stopindex=None, forwards=None,
                backwards=None, exact=None, regexp=None, nocase=None,
                count=None, elide=None, nolinestop=None):
            
        """
        Standard search method, but with support for the nolinestop
        option which is new in tk 8.5 but not supported by tkinter out
        of the box.
        """
    
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
        self.mark_set('(REP_STOPINDEX)', stopindex)

        while True:
            map = self.replace(regex, data, index, '(REP_STOPINDEX)', exact=exact, nocase=nocase, 
                               nolinestop=nolinestop, regexp=regexp, elide=elide)

            if not map: 
                return self.index('(REP_STOPINDEX)')

            index, size = map
            index = self.index('%s +%sc' % (index, size))


    def get_paren_search_dir(self, index, start, end):
        """

        """

        char  = self.get(index, '%s +1c' % index)
        if char == start:
            return False
        elif char == end:
            return True
        else:
            return None

    def get_paren_search_sign(self, index, start, end):
        """

        """

        char  = self.get(index, '%s +1c' % index)
        if char == start:
            return '+'
        elif char == end:
            return '-'
        else:
            return None

    def sel_matching_pair_data(self, index, max=1500, pair=('(', ')')):
        index = self.case_pair(index, max, *pair)
        if not index: return

        min = self.min(index, 'insert')
        max = self.max(index, 'insert')
        min = '%s +1c' % min

        self.tag_add('sel', min, max)

    def sel_matching_pair(self, index, max=1500, pair=('(', ')')):
        """
        """
        index = self.case_pair(index, max, *pair)
        if not index: return

        min = self.min(index, 'insert')
        max = self.max(index, 'insert')
        max = '%s +1c' % max

        self.tag_add('sel', min, max)

    def get_matching_pair(self, index, max, start='(', end=')'):
        """
        """

        index0 = self.search(start, regexp=False, index=index, backwards=True)
        if not index0: return

        index1 = self.search(end, regexp=False, index=index)
        if not index1: return


        index2 = self.case_pair(index0, max, start, end)
        if not index2: return

        index3 = self.case_pair(index1, max, start, end)
        if not index3: return

        if self.is_in_range(index, index0, index2):
            return index0, index2
        elif self.is_in_range(index, index3, index1):
            return index3, index1
        
    def case_pair(self, index, max, start='(', end=')'):
        """
        Once this method is called, it returns an index for the next
        matching parenthesis or None if the char over the cursor
        isn't either '(' or ')'.
        """

        dir = self.get_paren_search_dir(index, start, end)

        # If dir is None then there is no match.
        if dir == None: return ''

        sign  = self.get_paren_search_sign(index, start, end)
        count = 0

        # If we are searching fowards we don't need
        # to add 1c.

        index0 = '%s %s' % (index, '+1c' if dir else '')
        size  = IntVar(0)

        while True:
            index0 = self.search('\%s|\%s' % (start, end), index = index0,
                                     stopindex = '%s %s%sc' % (index, sign, max), 
                                     count = size, backwards = dir, regexp = True) 

            if not index0: return ''

            char  = self.get(index0, '%s +1c' % index0)
            count = count + (1 if char == start else -1)

            if not count: 
                return index0

            # When we are searching backwards we don't need
            # to set a character back because index will point
            # to the start of the match.
            index0 = '%s %s' % (index0, '+1c' if not dir else '')
                

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
        Consider:
        
        area.tag_add('tag', '2.0', '5.0')

        # It returns True.
        area.is_tag_range('tag', '2.0', '3.0')

        # It returns False.
        area.is_tag_range('tag', '1.0', '2.0')
        """ 

        ranges = self.tag_ranges(name)
        for ind in xrange(0, len(ranges) - 1, 2):
            if self.is_subrange(index0, index1, ranges[ind].string, 
                                ranges[ind + 1].string):
                return ranges[ind].string, ranges[ind + 1].string

    def is_in_range(self, index, index0, index1):
        """
        It returns True if index0 <= index <= index1 otherwise
        it returns False.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        r1     = self.compare(index2, '<=', index)
        r2     = self.compare(index3, '>=', index)

        return r1 and r2

    def is_subrange(self, index0, index1, index2, index3):
        """
        It returns True if index2 <= index0 <= index1 <= index2 otherwise
        it returns False.
        """

        r1 = self.is_in_range(index0, index2, index3)
        r2 = self.is_in_range(index1, index2, index3)
        return r1 and r2

    def swap(self, data, index0, index1):
        """
        Swap the text in the range index0, index1 for data.
        """

        self.delete(index0, index1)
        self.insert(index0, data)

    def swap_ranges(self, name, data, index0='1.0', index1='end'):
        """
        It swaps ranges of text that are mapped to a tag name for data between index0
        and index1.
        """

        while True:
            range = self.tag_nextrange(name, index0, index1)
            if not range: break
            self.swap(data, *range)

    def delete_ranges(self, name, index0='1.0', index1='end'):
        """
        It deletes ranges of text that are mapped to tag name between index0 and index1.
        """

        self.swap_ranges(name, '', index0, index1)

    def join_ranges(self, name, sep=''):
        """     
        Join ranges of text that corresponds to a tag defined by name using a seperator.
        """

        data = ''
    
        for ind in self.get_ranges(name):
            data = data + ind + sep
        return data


    def get_ranges(self, name):
        """
        It returns an iterator whose elements are ranges of text that
        corresponds to the ranges of the tag name.
        """

        ranges = self.tag_ranges(name)
        for ind in xrange(0, len(ranges) - 1, 2):
            data = self.get(ranges[ind], ranges[ind + 1])
            yield(data)

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
    def areavi_widgets(wid):
        """
        This method is a static method that receives a widget as argument
        then returns an iterator of AreaVi instances that have the wid paramater as
        master widget. It is used like:

        from vyapp.app import root
        for ind in AreaVi.areavi_widgets(root):
            ind.insert('end', 'FOO')

        The code above would insert 'FOO' at the end of all AreaVi widgets
        that have root as one of its master widget.
        """

        for ind in wid.winfo_children():
            if isinstance(ind, AreaVi):
                yield ind
            else:
                for ind in AreaVi.areavi_widgets(ind):
                    yield ind

    @staticmethod
    def get_opened_files(wid):
        """
        This method returns a dictionary that maps all AreaVi instances
        that have widget as master like:

        from vyapp.app import root
        map = area.get_opened_files(root)

        Where map is a dictionary like:

        map = { '/home/tau/file.c':AreaVi_Instance,
                '/home/tau/file.b': AreaVi_Instance}
        """

        map = dict()
        for ind in AreaVi.areavi_widgets(wid):
            map[ind.filename] = ind
        return map
    
    @staticmethod
    def find_all(wid, regex, index='1.0', stopindex='end', *args, **kwargs):
        """
        This method is used to perform pattern searches over all AreaVi instances that have
        wid as master. It basically returns an iterator that corresponds to:

        from vyapp.app import root
        for ind, (match, index0, index1) in area.find_all(root, 'pattern'):
            pass

        Where ind is the AreaVi widget that the pattern matched and match is the match, 
        index0 and index1 are the positions in the text.
        """

        for indi in AreaVi.areavi_widgets(wid):
            it = indi.find(regex, index, stopindex, *args, **kwargs)
    
            for indj in it:
                yield indi, indj
    
    def complete_word(self, wid):
        """
        It returns an iterator with possible word completions
        for a word that is close to the cursor.
        """

        index    = self.search('\W', 'insert', 
                                 stopindex='insert linestart',regexp=True, 
                                 backwards=True)
        index    = 'insert linestart' if not index else '%s +1c' % index
        pattern  = self.get(index, 'insert')

        if not pattern: return

        table = []

        for area, (data, _, _) in self.find_all(wid, '\w*%s\w*' % pattern):
            if not data in table:
                table.append(data)
            else:
                continue
            self.swap(data, index, 'insert')
            yield

        self.swap(pattern, index, 'insert')









