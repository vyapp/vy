"""
    :)
"""
from vyapp.plugins.syntax.tools import get_tokens_matrix
from pygments.lexers import get_lexer_for_filename, guess_lexer, guess_lexer_for_filename
from pygments.formatter import Formatter
from pygments.filter import Filter
from pygments.token import Token
from itertools import groupby

DEFAULT = (
    'Token.Name.Tag',
    'Token.Comment.Multiline',
    'Token.Literal.String.Doc',
    'Token.Literal.String.Heredoc',
    'Token.Literal.String.Regex',
    'Token.Literal.String.Symbol',
    'Token.Literal.String',
    'Token.Literal.String.Other',
    'Token.Literal.String.Single',
    'Token.Comment.Preproc',
    'Token.Comment',
    'Token.Comment.Single',
    'Token.Comment.Special',
    'Token.Literal.String.Double',
    'Token.Literal.String.Backtick',
    'Token.Literal.String.Char',
    'Token.Literal.Number.Float',
    'Token.Punctuation',
    'Token.Operator',
    'Token.Name',
    'Token.Keyword',
    'Token.Text',
)

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

        lexer = guess_lexer_for_filename(self.area.filename, 
        self.area.get('insert -10l', 'insert +10l'), stripnl=False, 
        stripall=False, tabsize=False)
        lexer.add_filter(JoinTType())

        index0 = self.area.index('@0,0')
        index1 = self.area.index('%s -%sl' % (index0, self.max))
        index2 = self.area.tag_prev_occur(DEFAULT, index0, index1, '1.0')

        index3 = '@%s,%s' % (self.area.winfo_height(), self.area.winfo_width())
        index4 = self.area.index(index3)
        index5 = self.area.index('%s +%sl' % (index4, self.max))
        index6 = self.area.tag_next_occur(DEFAULT, index4, index5, 'end')
        index2 = self.area.index('%s -1l' % index2)
        index6 = self.area.index('%s +1l' % index6)

        for ttype, tokstyle in self.style.styles.items():
            self.area.tag_remove(str(ttype), index2, index6)
        data = self.area.get(index2, index6)

        line, col = self.area.indexsplit(index2)
        tokens = get_tokens_matrix(line, col, data, lexer)
        self.formatter.format(tokens, self.area)

install = Spider

