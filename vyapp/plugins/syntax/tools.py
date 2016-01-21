from pygments.lexers import PythonLexer
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments.token import Token

def colorize(area, lexer, theme, index, stopindex):
    count, offset = area.indref(index)
    for ((srow, scol), (erow, ecol)), token, value in get_tokens_unprocessed_matrix(count, offset, 
                                                                                    area.get(index, stopindex), lexer):
        area.tag_add(str(token), '%s.%s' % (srow, scol), 
                     '%s.%s' % (erow, ecol))


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

def get_setting_fg(setting):
    for ind in setting:
        if ind.startswith('#'):
            return ind
    return ''

def get_setting_bg(setting):
    for ind in setting:
        if ind.startswith('bg:'):
            return ind.split(':')[1]
    return ''


def get_token_setting(theme, token, extractor):
    while token:
        setting = theme.styles[token]
        setting = extractor(setting.split(' '))
        if setting: 
            return setting
        token = token.parent
    return ''

def setup_token_scheme(area, theme, token):
    fg = get_token_setting(theme, token, get_setting_fg)
    area.tag_configure(str(token), foreground=fg)
    bg = get_token_setting(theme, token, get_setting_bg)
    area.tag_configure(str(token), background=bg)


def setup_theme_scheme(area, theme):
    area.configure(background=theme.background_color)
    area.configure(foreground='black' if not theme.default_style else theme.default_style)

    for ind in theme.styles.iterkeys():
        setup_token_scheme(area, theme, ind)


