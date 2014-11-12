from pygments.lexers import get_lexer_for_filename 
from vyapp.plugins.syntax.tools import *
from vyapp.tools.misc import exec_quiet, consume_iter

# It remains adding Token.Name and fixing the precedence.
TAG_KEYS_PRECEDENCE =('Token.Comment.Multiline',
    'Token.Literal.String.Doc',
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
    'Token.Generic.Strong',
    'Token.Generic.Prompt',
    'Token.Generic',
    'Token.Keyword.Pseudo',
    'Token.Generic.Deleted',
    'Token.Keyword.Declaration',
    'Token.Generic.Error',
    'Token.Generic.Output',
    'Token.Generic.Traceback',
    'Token.Literal.Number.Bin',
    'Token.Operator.Word',
    'Token.Literal.Date',
    'Token.Keyword',
    'Token.Generic.Emph',
    'Token.Keyword.Type',
    'Token.Keyword.Constant',
    'Token.Literal.Number',
    'Token.Generic.Subheading',
    'Token.Generic.Inserted',
    'Token.Literal',
    'Token.Literal.Number.Oct',
    'Token.Operator',
    'Token.Literal.Number.Integer',
    'Token.Keyword.Namespace',
    'Token.Keyword.Reserved',
    'Token.Generic.Heading',
    'Token.Punctuation',
    'Token.Literal.Number.Hex')


def install(area, theme):
    """
    """
    TIME = 1000

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
        colorize(area, lexer, theme, index0, index1)

    area.tag_setup(theme)

    def cave():
        update_scheme()
        area.after(TIME, cave)
    cave()































