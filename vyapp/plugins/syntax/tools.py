from pygments.lexers import PythonLexer
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.token import Token

def colorize(area, lexer, theme, index, stopindex):
    for pos, token, value in lexer.get_tokens_unprocessed(area.get(index, stopindex)):
        if theme.has_key(str(token)):
            area.tag_add(str(token), '%s +%sc' % (index, pos), 
                         '%s +%sc' % (index, pos + len(value)))


def thread_colorize(area, lexer, theme, index, stopindex):
    for pos, token, value in lexer.get_tokens_unprocessed(area.get(index, stopindex)):
        if theme.has_key(str(token)):
            area.tag_add(str(token), '%s +%sc' % (index, pos), 
                         '%s +%sc' % (index, pos + len(value)))

        if token is Token.Error:
            return
        yield















