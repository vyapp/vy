from pygments.lexers import get_lexer_for_filename 
from vyapp.plugins.syntax.tools import *
from vyapp.tools.misc import exec_quiet, consume_iter

# It remains adding Token.Name and fixing the precedence.
TAG_KEYS_PRECEDENCE =('Token.Comment.Multiline',
    'Token.Literal.String.Doc',
    'Token.Error',
    'Token.Literal.String.Heredoc',
    'Token.Literal.String.Interpol',
    'Token.Literal.String.Regex',
    'Token.Literal.String.Symbol',
    'Token.Literal.Number.Integer.Long',
    'Token.Literal.String',
    'Token.Literal.String.Other',
    'Token.Literal.String.Single',
    'Token.Literal.String.Escape',
    'Token.Comment.Preproc',
    'Token.Comment',
    'Token.Comment.Single',
    'Token.Comment.Special',
    'Token.Literal.String.Double',
    'Token.Literal.String.Backtick',
    'Token.Literal.String.Char',
    'Token.Literal.Number.Float',
    'Token.Punctuation',
    'Token.Operator')



def install(area, theme):
    """
    """

    def update_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return

        # This is working because the comments appear first in the sun.py theme.
        # So the comments have a greater precedence.
        index0 = get_prev_token(area, TAG_KEYS_PRECEDENCE, 'insert', '@0,0')
        index1 = get_next_token(area, TAG_KEYS_PRECEDENCE, 'insert', '@%s,%s' % (area.winfo_width(), area.winfo_height()))

        for ind in theme.keys():
            area.tag_remove(ind, index0, index1)

        colorize(area, lexer, theme, index0, index1)

    def start_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return
        iterator = thread_colorize(area, lexer, theme, '1.0', 'end')
        consume_iter(iterator)

    INSTALL = [(-1, '<<LoadData>>', lambda event: start_scheme()),
               (1, '<Escape>', lambda event: update_scheme())]



    area.tag_setup(theme)

    area.install(*INSTALL)

































