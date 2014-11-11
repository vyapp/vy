from pygments.lexers import get_lexer_for_filename 
from vyapp.plugins.syntax.tools import *
from vyapp.tools.misc import exec_quiet, consume_iter


def install(area, theme):
    """
    """
    TIME = 1000

    # def cave():
        # index0 = area.index("@0,0")
    # 
        # index1 = area.index("@%s,%s" % (area.winfo_width(), area.winfo_height()))
        # colorize(area, get_lexer_for_filename(area.filename, ''), theme, index0, index1)

    def update_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return
        
        index0 = get_prev_token(area, theme.keys(), '@0,0')
        index1 = get_next_token(area, theme.keys(), '@0,%s' % area.winfo_height())

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
               (1, '<Key-apostrophe>', lambda event: update_scheme())]

    area.tag_setup(theme)


    area.install(*INSTALL)




























