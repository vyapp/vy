"""
"""

from pygments.lexers import get_lexer_for_filename 
from vyapp.plugins.syntax.tools import *
from vyapp.exe import exec_quiet

TAG_KEYS_PRECEDENCE =('Token.Name.Tag',
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
    'Token.Text',
    'Token.Keyword',
    'Token.Generic',
    'Token.Generic.Deleted',
    'Token.Generic.Emph',
    'Token.Generic.Error',
    'Token.Generic.Heading',
    'Token.Generic.Inserted',
    'Token.Generic.Output',
    'Token.Generic.Prompt',
    'Token.Generic.Strong',
    'Token.Generic.Subheading',
    'Token.Generic.Traceback')

def install(area, theme, max=10):
    """
    """
    def update_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return

        index0 = area.index('@0,0')
        index0 = area.index('%s -%sl' % (index0, max))
        index0 = area.tag_next_occur(TAG_KEYS_PRECEDENCE, index0, 'insert', '1.0')
        index1 = '@%s,%s' % (area.winfo_height(), area.winfo_width())
        index2 = area.index(index1)
        index2 = area.index('%s +%sl' % (index1, max))
        index2 = area.tag_prev_occur(TAG_KEYS_PRECEDENCE, index2, 'insert', 'end')
        for ind in theme.styles.iterkeys():
            area.tag_remove(str(ind), index0, index2)

        colorize(area, lexer, theme.styles, index0, index2)

    def start_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return
        colorize(area, lexer, theme.styles, '1.0', 'end')

    area.install((-1, '<<LoadData>>', lambda event: start_scheme()),
                 (-1, '<Escape>', lambda event: update_scheme()))

    setup_theme_scheme(area, theme)







