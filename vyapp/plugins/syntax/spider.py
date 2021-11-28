"""
    :)
"""
from vyapp.plugins.syntax.tools import get_tokens_matrix
from vyapp.plugins.syntax.styles.vy import VyStyle
from pygments.util import ClassNotFound 
from pygments.lexers import get_lexer_for_filename as get_lexer
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.formatter import Formatter
from vyapp.stderr import printd
from pygments.filter import Filter
from pygments.token import Token
from itertools import groupby

TK_ORDER = ('Token.Name.Tag', 'Token.Comment.Multiline',
'Token.Literal.String.Doc','Token.Literal.String.Heredoc',
'Token.Literal.String.Regex', 'Token.Literal.String.Symbol',
'Token.Literal.String', 'Token.Literal.String.Other',
'Token.Literal.String.Single', 'Token.Comment.Preproc',
'Token.Comment', 'Token.Comment.Single',
'Token.Comment.Special', 'Token.Literal.String.Double',
'Token.Literal.String.Backtick', 'Token.Literal.String.Char',
'Token.Literal.Number.Float', 'Token.Punctuation',
'Token.Operator', 'Token.Name', 'Token.Keyword',
'Token.Text',
)

def findlexer(filename, text, **opts):
    """
    The pygments guess_lexer_for_filename works only when there is
    a lexer has a pattern in filename.
    
    When get_lexer_for_filename fails it uses the value in text
    to guess the lexer using pygments guess_lexer.
    """

    try:
        return get_lexer(filename, **opts)
    except ClassNotFound as excpt:
        if not text: 
            raise excpt
    return guess_lexer(text, **opts)

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
    style = VyStyle
    guesslex = True

    def  __init__(self, area, max=10):
        self.area  = area
        self.max   = max

        area.install('syntax', 
        (-1, '<<LoadData>>', self.update_all),
        (-1, '<<SaveData>>', self.update_all),
        (-1, '<Escape>', self.update))

        if self.style.background_color:
            self.area.configure(background=self.style.background_color)
        default_style = getattr(self.style, 'default_style')

        # Set foreground as pygments style.default_style value.
        if default_style:
            self.area.configure(foreground=default_style)

        for tokname, tokstyle in self.style:
            self.conf_tokstyle(str(tokname), tokstyle)
        self.formatter = TkTxtFormatter(style=self.style)
        self.lexer = None

    @classmethod
    def c_style(cls, style):
        """
        """
        cls.style = style

    @classmethod
    def c_guesslex(self, value):
        self.guesslex = value

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
        Colorize the whole text.
        """

        printd("Syntax - Detecting lexer.")
        self.lexer = findlexer(self.area.filename, 
        self.area.get('1.0', '1.0 +258c') if self.guesslex else None, 
        stripnl=False, stripall=False, tabsize=False)

        printd("Syntax - Detected lexer:", self.lexer)
        data = self.area.get('1.0', 'end')

        # Attempt to add the filter. If no lexer is set then raises
        # an exception.
        self.lexer.add_filter(JoinTType())
        tokens = get_tokens_matrix(1, 0, data, self.lexer)
        self.formatter.format(tokens, self.area)

    def update(self, event):
        """
        Colorize visible region.
        """

        index0 = self.area.index('@0,0')
        index1 = self.area.index('%s -%sl' % (index0, self.max))
        index2 = self.area.tag_prev_occur(TK_ORDER, index0, index1, '1.0')

        index3 = '@%s,%s' % (self.area.winfo_height(), self.area.winfo_width())
        index4 = self.area.index(index3)
        index5 = self.area.index('%s +%sl' % (index4, self.max))
        index6 = self.area.tag_next_occur(TK_ORDER, index4, index5, 'end')

        # Macumba attempt.
        index7 = self.area.tag_prevrange('Token.Text', index2, '1.0')
        index8 = self.area.tag_nextrange('Token.Text', index6, 'end')
        index2 = index7[1] if index7 else index2
        index6 = index8[0] if index8 else index6

        for ttype, tokstyle in self.style.styles.items():
            self.area.tag_remove(str(ttype), index2, index6)
        data = self.area.get(index2, index6)

        line, col = self.area.indexsplit(index2)
        tokens = get_tokens_matrix(line, col, data, self.lexer)
        self.formatter.format(tokens, self.area)

install = Spider

