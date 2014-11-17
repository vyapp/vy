from pygments.lexers import PythonLexer
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.token import Token

def colorize(area, lexer, theme, index, stopindex):
    count, offset = area.indref(index)
    for ((srow, scol), (erow, ecol)), token, value in get_tokens_unprocessed_matrix(count, offset, 
                                                                                    area.get(index, stopindex), lexer):
        if theme.has_key(str(token)):
            area.tag_add(str(token), '%s.%s' % (srow, scol), 
                         '%s.%s' % (erow, ecol))


def thread_colorize(area, lexer, theme, index, stopindex):
    for pos, token, value in lexer.get_tokens_unprocessed(area.get(index, stopindex)):
        if theme.has_key(str(token)):
            area.tag_add(str(token), '%s +%sc' % (index, pos), 
                         '%s +%sc' % (index, pos + len(value)))
        yield


def get_tokens_unprocessed_matrix(count, offset, data, lexer):
    for pos, token, value in lexer.get_tokens_unprocessed(data):
        srow  = count 
        scol  = pos - offset
        scol  = offset + pos if scol < 0 else scol
        n     = value.count('\n')
        erow  = srow + n
        count = count + n

        m     = value.rfind('\n') 
        offset = pos + m + 1 if m >= 0 else offset

        ecol  = len(value) - (m + 1) if m >= 0 else scol + len(value)

        yield(((srow, scol), (erow, ecol)), token, value)













