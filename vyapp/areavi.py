"""

"""

from vyapp.mixins import DataEvent, IdleEvent
from re import escape
from tkinter import TclError
from vyapp.stderr import printd
from tkinter import Text, IntVar
import os

class AreaVi(Text, DataEvent, IdleEvent):
    INPUT  = None
    # Plugins should commonly use self.project
    # if it fails then use HOME.
    HOME   = ''

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
        DataEvent.__init__(self, self)
        IdleEvent.__init__(self, self)

        self.setup = dict()

        # Maybe it should be?
        # abspath(default_filename)
        self.default_filename = default_filename

        # The file's path and name.
        self.filename  = os.path.abspath(default_filename)
        self.extension = os.path.splitext(self.filename)

        self.mark_set('(CURSOR_LAST_COL)', '1.0')

        self.charset  = 'utf-8'
        self.map      = {}
        self.db       = {}
        self.project  = ''
        self.assoc_c  = 0

        # The character used for indentation.
        self.tabchar = ' '
        self.tabsize = 4

        def set_input(e):
            AreaVi.INPUT = e.widget
        self.hook('AreaVi', '-1', '<FocusIn>', set_input)

    def settab(self, tabsize, tabchar):
        self.tabchar = tabchar
        self.tabsize = tabsize

    def indent(self):
        self.edit_separator()
        self.insert('insert', self.tabchar * self.tabsize)

    def update_map(self, namespace, map):
        scheme = self.map.setdefault(namespace, {})
        scheme.update(map)

    def rsmode(self):
        """
        Restore its previous mode.
        """
        pass

    def chmode(self, id):
        """
        This function is used to change the AreaVi instance's mode.
        It receives one parameter named id which means the
        mode name.

        area = AreaVi('None')
        area.chmode('INSERT')

        It would make area be in INSERT mode.
        """
        opt = self.setup[id]
        self.id = id

        master = 'mode%s-1' % self
        slave = 'mode%s%s' % (self, id)

        if opt is True: 
            self.bindtags((master, slave, self, 'Text', '.'))
        else: 
            self.bindtags((master, slave, self, '.'))

        self.event_generate('<<Chmode>>')
        self.event_generate('<<Chmode-%s>>' % id)

    def add_mode(self, id, opt=False):
        """
        It adds a new mode. The opt argument means whether
        it should propagate the event to the internal text widget callbacks.

        def install(area):
            area.add_mode('MODE')

        The above code would add a mode named MODE to the AreaVi instance.

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

    def hook(self, namespace, id, seq, callback, add=True):
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

        scheme = self.map.get(namespace, {})
        for id, seq in scheme.get((id, seq), ((id, seq), )):
            self.hook_class(id, seq, callback, add)

    def hook_class(self, id, seq, callback, add=True):
        modn = 'mode%s%s' % (self, id)

        if self.bind_class(modn, seq):
            printd('Warning: %s %s already binded!' % (id, seq))
        self.bind_class(modn, seq, callback, add)

    def unhook(self, id, seq):
        """
        The opposite of AreaVi.hook.
    
        area.unhook('mode' '<Event>')
        """

        mode = 'mode%s%s' % (self, id)
        self.unbind_class(mode, seq)

    def install(self, namespace, *args):
        """
        It is a shorthand for AreaVi.hook. It is used as follows:

        def install(area):
            area.install(('MODE1', '<Event1>', callback1),
                         ('MODE2', '<Event2>', callback2),
                         ('MODE3', '<Event3>', callback3), ...)
        """

        for ind in args:
            self.hook(namespace, *ind)

    def uninstall(self, *args):
        """
        The opposite of AreaVi.install.

        area.uninstall(('mode', '<Event>'), ...)
        """

        for id, seq, callback in args:
            self.unhook(id, seq, callback)

    def append(self, data, *args):
        """
        This method is used to insert data to the end of the AreaVi instance widget
        and place the cursor at the end of the data that was appended. It makes the cursor
        visible.
        """

        # This is sort of odd, it seems that
        # i have to add -1l for it to work.
        # It shouldn't be necessary.
        index0 = self.index('end -1l')
        self.insert('end', data)

        for ind in args:
            self.tag_add(ind, index0, 'end -1c')

        # self.mark_set('insert', 'end')
        self.see('insert')

    def get_assoc_data(self, index='insert'):
        lst = (self.db[ind] for ind in self.tag_names(index)
        if 'ASSOC_DATA' in ind)
        return lst

    def set_assoc_data(self, index0, index1, data):
        id = '(ASSOC_DATA-%s)' % self.assoc_c
        self.tag_add(id, index0, index1)
        self.assoc_c = self.assoc_c + 1
        self.db[id]  = data
        return id

    def reset_assoc_data(self):
        for ind in self.db.keys():
            self.tag_delete(ind)
        self.db.clear()

    def setcur(self, line, col='0'):
        """
        It is used to set the cursor position at a given index using line 
        and col. 
        """


        self.mark_set('insert', '%s.%s' % (line, col))
        self.see('insert')

    def indexsplit(self, index='insert'):
        """ 
        Just a shorthand for:
        
        a, b = index.split('2.3')
        a, b = int(a), int(b)
        """

        index = self.index(index)
        a, b = index.split('.')
        return int(a), int(b)

    def down(self):
        """  
        It sets the cursor position one line down.  
        """

        # I have to use 'end -1l linestart' since it seems the 'end' tag
        # corresponds to a one line after the last visible line.
        # So last line lineend != 'end'.

        is_end = self.compare('insert linestart', '!=', 'end -1l linestart')
        if not is_end: return

        a, b = self.indexsplit('(CURSOR_LAST_COL)')
        c, d = self.indexsplit()
        self.setcur(c + 1, b)        
    
    def up(self):   
        """  
        It sets the cursor one line up.  
        """

        is_start = self.compare('insert linestart', '!=', '1.0')

        if not is_start: return
        a, b = self.indexsplit('(CURSOR_LAST_COL)')
        c, d = self.indexsplit()
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

    def clear_selection(self):
        """
        Unselect all text.
        """

        try:
            self.tag_remove('sel', 
                'sel.first', 'sel.last')
        except Exception:
            pass

    def cpsel(self, sep=''):
        """
        Copy selected text to the clipboard.
        """

        data = self.tag_xjoin('sel', sep)
        self.clipboard_clear()
        self.clipboard_append(data)
        self.tag_remove('sel', 'sel.first', 'sel.last')
    

    def ctsel(self, sep=''):
        """
        It cuts the selected text.
        """

        data = self.tag_xjoin('sel', sep)
        self.clipboard_clear()
        self.clipboard_append(data)
        self.edit_separator()
        self.tag_xswap('sel', '', '1.0', 'end')

    def tag_contains(self, name, index0, index1):
        """
        """ 

        ranges = self.tag_ranges(name)
        for ind in range(0, len(ranges) - 1, 2):
            if self.slc_contains(index0, index1, ranges[ind].string, 
                                ranges[ind + 1].string):
                return ranges[ind].string, ranges[ind + 1].string

    def index_in(self, index, index0, index1):
        """
        It returns True if index0 <= index <= index1 otherwise
        it returns False.
        """

        index2 = self.min(index0, index1)
        index3 = self.max(index0, index1)

        r1 = self.compare(index2, '<=', index)
        r2 = self.compare(index3, '>=', index)

        return r1 and r2

    def slc_contains(self, index0, index1, index2, index3):
        """
        It returns True if index2 <= index0 <= index1 <= index2 otherwise
        it returns False.
        """

        r1 = self.index_in(index0, index2, index3)
        r2 = self.index_in(index1, index2, index3)
        return r1 and r2

    def tag_toggle(self, name, index0, index1):
        """
        """

        index2 = index0
        index0 = self.min(index0, index1)
        index1 = self.max(index2, index1)

        map = self.tag_contains(name, index0, index1)
        if map:
            self.tag_remove(name, index0, index1)
        else:
            self.tag_add(name, index0, index1)

    def get_word_range(self, index='insert'):
        index1 = self.search('\W', index, regexp=True, stopindex='%s linestart' % index, backwards=True)
        index2 = self.search('\W', index, regexp=True, stopindex='%s lineend' % index)
        index1 = '%s linestart' % index if not index1 else '%s +1c' % index1
        index2 = '%s lineend' % index if not index2 else index2
        return index1, index2

    def get_seq_range(self, index='insert'):
        index1 = self.search(' ', index, regexp=True, stopindex='%s linestart' %index, backwards=True)
        index2 = self.search(' ', index, regexp=True, stopindex='%s lineend' % index)
        index1 = '%s linestart' % index if not index1 else '%s +1c' % index1
        index2=  '%s lineend' % index if not index2 else index2
        return index1, index2

    def get_line(self, index='insert'):
        return self.get('%s linestart' % index, 
        '%s lineend' % index)

    def tag_xmatch(self, name, regex, index='1.0', 
        stopindex='end', exact=False, regexp=True, nocase=False, 
        elide=False, nolinestop=False):

        """
        """
        
        map = self.tag_ranges(name)
        for indi in range(0, len(map) - 1, 2):
            seq = self.find(regex, map[indi], map[indi + 1], 
                exact=exact, regexp=regexp, nocase=nocase, 
                    elide=elide, nolinestop=nolinestop)
            yield from seq

    def tag_xsub(self, name, regex, data, exact=False, 
        regexp=True, nocase=False, elide=False, nolinestop=False):
        """
        """

        count = 0
        while True:
            map = self.tag_nextrange(name, '1.0', 'end')
            if map == (): 
                return count
            self.tag_remove(name, *map)

            inc = self.replace_all(regex, data, map[0], map[1], 
                    exact, regexp, nocase, elide, nolinestop)
            count = count + inc
        return count

    def split(self, regex, index='1.0', stopindex='end', *args, **kwargs):
        """
        """

        index0 = index
        matches = self.find(regex, index, stopindex, *args, **kwargs)
        for chk, index1, index2 in matches:
            yield(self.get(index0, index1), index0, index1)
            index0 = index2

        token = self.get(index0, stopindex)
        yield(token, index0, stopindex)
    
    def find(self, regex, index='1.0', stopindex='end', 
        backwards=False, exact=False, regexp=True, nocase=False, 
        elide=False, nolinestop=False, step=''):

        """
        """
        if not regex: 
            raise TclError('Regex is blank!')
        self.mark_set('(FIND-POS)', index)

        while True:
            count = IntVar()
            index = self.search(regex, '(FIND-POS)', stopindex, 
                None, backwards, exact, regexp, nocase, count=count,
                    elide=elide, nolinestop=nolinestop)

            if not index: 
                return None
            len  = count.get()
            pos0 = self.index(index)
            pos1 = self.index('%s +%sc' % (index, len))
            data = self.get(pos0, pos1)

            self.mark_set('(FIND-POS)', 
            index if len and backwards else (
                pos1 if len else (('%s -1c'  
                    if backwards else '%s +1c') % pos1)))

            if step != '':
                self.mark_set('(FIND-POS)',
                    '%s %s' % (self.index('(FIND-POS)'), step))
            yield(data, pos0, pos1)

    def isearch(self, pattern, index, stopindex='end', forwards=None,
        backwards=None, exact=None, regexp=None, nocase=None,
        count=None, elide=None, nolinestop=None):

        """
        Just AreaVi.search shortcut, in the sense it return the matched chunk
        the initial position and the end position.
        """
        count = IntVar()
        index = self.search(pattern, index, stopindex, 
        forwards, backwards, exact, regexp, nocase, count=count,
        elide=elide, nolinestop=nolinestop)

        if not index: return 

        len   = count.get()
        tmp   = '%s +%sc' % (index, len)
        chunk = self.get(index, tmp)

        pos0  = self.index(index)
        pos1  = self.index('%s +%sc' % (index, len))

        return chunk, pos0, pos1


    def search(self, pattern, index, stopindex='end', forwards=None,
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

    def ipick(self, name, regex, index='insert', stopindex='end', 
        verbose=False, backwards=False, exact=False, regexp=True, 
        nocase=False, elide=False, nolinestop=False):

        """
        """

        # Force to do a search from index.
        if verbose is True: 
            self.tag_remove(name, '1.0', 'end')
        if backwards is False: 
            ranges = self.tag_nextrange(name, index, 'end')
        else: 
            ranges = self.tag_prevrange(name, index, '1.0')

        if ranges: 
            index0, index1 = ranges[:2]
        else: 
            index0 = index1 = index

        index = self.isearch(regex, index=index0 if backwards else index1, 
        stopindex=stopindex, backwards=backwards, exact=exact, regexp=regexp, 
        nocase=nocase, elide=elide, nolinestop=nolinestop)

        if not index: 
            return None
        _, start, end = index

        self.mark_set('insert', start if backwards else end)
        self.see('insert')

        self.tag_remove(name, '1.0', 'end')
        self.tag_add(name, start, end)
        return start, end

    def replace(self, regex, data, index=None, stopindex=None,  
        forwards=None, backwards=None, exact=None, regexp=True, 
        nocase=None, elide=None, nolinestop=None):

        """
        """
        if not regex: 
            raise TypeError('Regex should be non blank!')

        count = IntVar()

        index = self.search(regex, index, stopindex, forwards=forwards, 
        backwards=backwards, exact=exact, nocase=nocase,  nolinestop=nolinestop, 
        regexp=regexp, elide=elide, count=count)
            
        if not index:  
            return None

        index0 = self.index('%s +%sc' % (index, count.get()))

        if callable(data): 
            data = data(self.get(index, index0), index, index0)
        
        self.delete(index, index0)
        self.insert(index, data)
        
        return index, len(data)

    def replace_all(self, regex, data, index='1.0', stopindex='end', 
        exact=None, regexp=True, nocase=None, elide=None, nolinestop=None):
        """
        """
        matches = self.find(regex, index, stopindex, exact=exact, 
        regexp=regexp, nocase=nocase, elide=elide, nolinestop=nolinestop)
        count = 0

        for xstr, pos0, pos1 in matches:
            if callable(data):
                self.swap(data(xstr), pos0, pos1)
            else:
                self.swap(data, pos0, pos1)
            count = count + 1
        return count

    def pair(self, lhs, rhs, index, max, backwards=False):
        """
        """

        sign  = '-' if backwards else '+'
        count = 0
        regex = '|'.join((escape(lhs), escape(rhs)))

        matches = self.find(regex, index, 
        '%s %s%sc' % (index, sign, max), backwards, regexp=True)

        for data, pos0, pos1 in matches:
            count = count + (1 if data == lhs else -1)
            if count == 0: 
                return pos0, pos1

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
        self.filename     = os.path.abspath(filename)
        _, self.extension = os.path.splitext(self.filename)

        self.event_generate('<<Pre-LoadData>>')
        self.event_generate('<<Pre-LoadData/*%s>>' % self.extension)

        fd   = open(self.filename, 'rb')
        data = fd.read()
        fd.close()

        try:
            data = data.decode(self.charset)
        except UnicodeDecodeError:
            self.charset = ''

        self.delete('1.0', 'end')
        self.insert('end', data)
        self.mark_set('insert', '1.0')
        self.see('insert')

        self.event_generate('<<LoadData>>')
        self.event_generate('<<Load/*%s>>' % self.extension)

    def decode(self, name):
        """
        Used to change the areavi encoding.
        """

        self.charset = name
        self.load_data(self.filename)

    def save_data(self):
        """
        It saves the actual text content in the current file.
        """
        _, self.extension = os.path.splitext(self.filename)
        self.event_generate('<<Pre-SaveData>>')
        self.event_generate('<<Pre-Save/*%s>>' % self.extension)

        data = self.get('1.0', 'end -1c')
        data = data.encode(self.charset)
        fd   = open(self.filename, 'wb')
        fd.write(data)
        fd.close()
        self.event_generate('<<SaveData>>')
        self.event_generate('<<Save/*%s>>' % self.extension)

    def save_data_as(self, filename):
        """
        It saves the content of the given AreaVi instance into
        a file whose name is specified in filename.


        filename - Name of the file to save the data.
        """

        self.filename = filename
        self.save_data()

    def swap(self, data, index0, index1):
        """
        Swap the text in the range index0, index1 for data.
        """

        self.delete(index0, index1)
        self.insert(index0, data)

    def tag_xswap(self, name, data, index='1.0', stopindex='end'):
        """
        This method swaps the text in each one of the ranges that 
        corresponds to tag name for data between index and stopindex.
        """

        count = 0
        self.mark_set('(TAG-XSWAP)', index)

        while True:
            range = self.tag_nextrange(
                name, '(TAG-XSWAP)', stopindex)
            if len(range) == 0: 
                return count

            self.mark_set('(TAG-XSWAP)', range[1])
            self.swap(data, *range)
            count = count + 1

    def tag_xjoin(self, name, sep=''):
        """     
        Join ranges of text that corresponds to tag name. The ranges
        are joined using sep.
        """

        data = ''
        ranges = self.tag_ranges(name)
        for ind in range(0, len(ranges) - 1, 2):
            data += self.get(ranges[ind], ranges[ind + 1]) + sep
        return data

    def tag_prev_occur(self, tag_names, index0, index1, default):
        """
        Should be renamed.
        """

        for ind in tag_names:
            pos = self.tag_prevrange(ind, index0, index1)
            if pos != (): 
                return pos[1]
        return default
    
    def tag_next_occur(self, tag_names, index0, index1, default):
        """
        Should be renamed.
        """

        for ind in tag_names:
            pos = self.tag_nextrange(ind, index0, index1)
            if pos != (): 
                return pos[0]
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
    
    def tag_bounds(self, tag, index='insert'):
        range0 = self.tag_nextrange(tag, index)
        if range0:
            if self.compare(range0[0], '<=', index):
                return range0

        range1 = self.tag_prevrange(tag, index)
        if range1:
            if self.compare(index, '<=', range1[1]):
                return range1

    def set_breakpoint(self, line, conf):
        self.tag_delete('(DebuggerPB)')
        self.tag_add('(DebuggerPB)', '%s.0 linestart' % line, '%s.0 lineend' % line)
        self.tag_config('(DebuggerPB)', **conf)
