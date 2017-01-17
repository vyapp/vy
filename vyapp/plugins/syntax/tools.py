from pygments.lexers import PythonLexer
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.token import Token


def thread_colorize(area, lexer, theme, index, stopindex):
    for pos, token, value in lexer.get_tokens_unprocessed(area.get(index, stopindex)):
        area.tag_add(str(token), '%s +%sc' % (index, pos), 
                     '%s +%sc' % (index, pos + len(value)))

        yield

def matrix_step(map):
    count, offset = 0, 0
    for pos, token, value in map:
        srow   = count 
        scol   = pos - offset
        n      = value.count('\n')
        erow   = srow + n
        count  = count + n
        m      = value.rfind('\n') 
        offset = pos + m + 1 if m >= 0 else offset
        ecol   = len(value) - (m + 1) if m >= 0 else scol + len(value)
        yield(((srow, scol), (erow, ecol)), token, value)


def get_tokens_unprocessed_matrix(count, offset, data, lexer):
    map = matrix_step(lexer.get_tokens_unprocessed(data))

    for ((srow, scol), (erow, ecol)), token, value in map:
        if '\n' in value: 
            yield(((srow + count, scol + offset), 
                  (erow + count, ecol)), token, value)
            break
        else:
            yield(((srow + count, scol + offset), 
                  (erow + count, ecol + offset)), 
                   token, value)

    for ((srow, scol), (erow, ecol)), token, value in map:
        yield(((srow + count, scol), (erow + count, ecol)), 
               token, value)



