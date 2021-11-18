"""
    :)
"""
from vyapp.plugins.syntax.tools import get_tokens_unprocessed_matrix
from vyapp.plugins.syntax.keys import PRECEDENCE_TABLE, DEFAULT
from pygments.lexers import get_lexer_for_filename, guess_lexer


class Spider:
    def  __init__(self, area, theme, max=10):
        self.area          = area
        self.max           = max
        self.theme         = theme
        self.styles        = theme.styles
        self.default_style = getattr(theme, 'default_style', '#957C8B')
        self.default_style = self.default_style if self.default_style else '#957C8B'

        self.default_background = theme.background_color \
        if theme.background_color else 'black'
        self.lexer = None
        area.configure(background = self.default_background)
        area.configure(foreground = self.default_style)

        for ind in self.styles.keys():
            self.set_token_style(ind)

        area.install('syntax', (-1, '<<LoadData>>', 
        lambda event: self.update_all()),
        (-1, '<<SaveData>>', lambda event: self.update_all()),
        (-1, '<Escape>', lambda event: self.update()))

    def set_lexer(self):
        """
        Try to detect the lexer by filename if it fails
        then try to guess the lex by shebang statement.
        
        The shebang statement should be placed in the first
        20 lines of the file.
        """

        try:
            self.lexer = get_lexer_for_filename(self.area.filename, '')
        except Exception as e:
            self.lexer = guess_lexer(self.area.get('1.0', '20.0'))

    def update_all(self):
        """
        Colorize all text in the widget.
        """

        # When it need to update all the text
        # just save the lexer for later usage.
        self.set_lexer()
        self.tag_tokens('1.0', 'end')

    def update(self):
        """
        Update a small range of the text. It is mostly called 
        when Escape is pressed.
        """

        TAG_KEYS_PRECEDENCE = PRECEDENCE_TABLE.get(
        tuple(self.lexer.aliases), DEFAULT)

        index0 = self.area.index('@0,0')
        index0 = self.area.index('%s -%sl' % (index0, self.max))
        index0 = self.area.tag_next_occur(TAG_KEYS_PRECEDENCE, 
        index0, 'insert', '1.0')

        index1 = '@%s,%s' % (self.area.winfo_height(), 
        self.area.winfo_width())

        index2 = self.area.index(index1)
        index2 = self.area.index('%s +%sl' % (index1, self.max))

        index2 = self.area.tag_prev_occur(TAG_KEYS_PRECEDENCE, 
        index2, 'insert', 'end')

        for ind in self.styles.keys():
            self.area.tag_remove(str(ind), index0, index2)
        self.tag_tokens(index0, index2)

    def tag_tokens(self, index, stopindex):
        """
        Add the token'tag to each range of text.
        """

        count, offset = self.area.indexsplit(index)
        tokens        = get_tokens_unprocessed_matrix(count, offset, 
        self.area.get(index, stopindex), self.lexer)

        for ((srow, scol), (erow, ecol)), token, value in tokens:
            self.area.tag_add(str(token), '%s.%s' % (srow, 
                 scol), '%s.%s' % (erow, ecol))

    def set_token_style(self, token):
        """
        Configure the tag which maps to the token in the
        AreaVi. 
        
        If there is no such a definition of token
        in styles dict then it defaults to self.background 
        and self.default_style.
        """

        tag  = str(token)
        conf = self.theme.style_for_token(token)

        self.area.tag_configure(tag, 
        foreground='#%s' % conf['color'] if conf['color'] \
        else self.default_style, 
        background='#%s' % conf['bgcolor'] if conf['bgcolor'] else \
        self.default_background, 
        underline=conf['underline'])

        # Note: It may be interesting to redefine
        # tag_configure in AreaVi and implement it there.
        self.area.tag_lower(tag, 'sel')

install = Spider



