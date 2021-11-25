"""
    :)
"""
from vyapp.plugins.syntax.tools import get_tokens_matrix
from pygments.lexers import get_lexer_for_filename, guess_lexer, guess_lexer_for_filename
from vyapp.plugins.syntax.keys import PRECEDENCE_TABLE, DEFAULT
from pygments.formatter import Formatter
from pygments.filter import Filter
from pygments.token import Token
from itertools import groupby

class JoinTType(Filter):
    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        groups = groupby(stream, lambda ind: ind[0])
        for ttype, seq in groups:
            yield ttype, ''.join(map(lambda ind: ind[1], seq))

class TkTxtFormatter(Formatter):
    def __init__(self, **options):
        Formatter.__init__(self, **options)

    def format(self, tokens, area):
        for (index0, index1), ttype, value in tokens:
            index0, index1 = '%s.%s' % index0,  '%s.%s' % index1
            tokname = self.has_tokstyle(ttype)
            area.tag_add(str(tokname), index0, index1)
            area.tag_add('Token.SStr', index0, index1)
            if '\n' in value:
                area.tag_add('Token.MStr', index0, index1)

    def has_tokstyle(self, token):
        ttype = token
        while ttype not in self.style.styles:
            ttype = ttype.parent
            if ttype is None:
                return None
        return ttype

class Spider:
    def  __init__(self, area, style, max=10):
        self.area  = area
        self.max   = max
        self.style = style

        area.install('syntax', 
        (-1, '<<LoadData>>', self.update_all),
        (-1, '<<SaveData>>', self.update_all),
        (-1, '<Escape>', self.update))

        if style.background_color:
            self.area.configure(background=style.background_color)
        default_style = getattr(style, 'default_style')

        if default_style:
            self.area.configure(foreground=default_style)

        for tokname, tokstyle in self.style:
            self.conf_tokstyle(str(tokname), tokstyle)
        self.formatter = TkTxtFormatter(style=style)

    def conf_tokstyle(self, tokname, tokstyle):
        foreground = tokstyle.get('color')
        background = tokstyle.get('bgcolor')
        underline  = tokstyle.get('underline')

        if not foreground is None:
            self.area.tag_config(tokname, foreground='#%s' % foreground)
        if not background is None:
            self.area.tag_config(tokname, background='#%s' % background)
        if not underline is None:
            self.area.tag_config(tokname, underline=underline)
        self.area.tag_lower(tokname, 'sel')

    def update_all(self, event):
        """
        """
        data = self.area.get('1.0', 'end')
        lexer = guess_lexer_for_filename(self.area.filename, 
        data[0:20], stripnl=False, stripall=False, tabsize=False)

        tokens = get_tokens_matrix(1, 0, data, lexer)
        lexer.add_filter(JoinTType())
        self.formatter.format(tokens, self.area)

    def update(self, event):
        """
        """

        index0 = self.area.index('@0,0')
        index0 = self.area.index('%s -%sl' % (index0, self.max))

        lexer  = guess_lexer_for_filename(self.area.filename, 
        self.area.get('insert -10l', 'insert +10l'), stripnl=False, 
        stripall=False, tabsize=False)

        lexer.add_filter(JoinTType())

        TAG_KEYS_PRECEDENCE = PRECEDENCE_TABLE.get(
        tuple(lexer.aliases), DEFAULT)

        index0 = self.area.tag_next_occur(TAG_KEYS_PRECEDENCE, 
        index0, 'insert', '1.0')

        index1 = '@%s,%s' % (self.area.winfo_height(), 
        self.area.winfo_width())

        index2 = self.area.index(index1)
        index2 = self.area.index('%s +%sl' % (index1, self.max))

        index2 = self.area.tag_prev_occur(TAG_KEYS_PRECEDENCE, 
        index2, 'insert', 'end')

        for ttype, tokstyle in self.style.styles.items():
            self.area.tag_remove(str(ttype), index0, index2)
        data = self.area.get(index0, index2)

        line, col = self.area.indexsplit(index0)
        tokens = get_tokens_matrix(line, col, data, lexer)
        self.formatter.format(tokens, self.area)

install = Spider

