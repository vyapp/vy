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


def get_prev_token(area, tag_names, index, default='1.0'):
    for ind in tag_names:
        pos = area.tag_prevrange(ind, index)
        if pos: return pos[0]
    return default

def get_next_token(area, tag_names, index, default='end'):
    for ind in tag_names:
        pos = area.tag_nextrange(ind, index)
        if pos: return pos[1]
    return default













