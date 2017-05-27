"""
    :)
"""

from vyapp.plugins.syntax.tools import *
from vyapp.plugins.syntax.keys import PRECEDENCE_TABLE, DEFAULT
from pygments.lexers import get_lexer_for_filename 
from re import search

class Spider(object):
    def  __init__(self, area, theme, max=10):
        self.area          = area
        self.max           = max
        self.styles        = theme.styles
        self.default_style = getattr(theme, 'default_style', '#957C8B')
        self.background    = theme.background_color
        area.configure(background = self.background)
        area.configure(foreground = self.default_style)

        for ind in self.styles.iterkeys():
            self.set_token_style(ind)

        area.install('syntax', (-1, '<<LoadData>>', 
        lambda event: self.update_all()),
        (-1, '<<SaveData>>', lambda event: self.update_all()),
        (-1, '<Escape>', lambda event: self.update()))

    def update_all(self):
        """
        Colorize all text in the widget.
        """

        lexer = None
        try:
            lexer = get_lexer_for_filename(self.area.filename, '')
        except Exception:
            return
        self.tag_tokens(lexer, '1.0', 'end')

    def update(self):
        """
        Update a small range of the text. It is mostly called 
        when Escape is pressed.
        """

        lexer = None
        try:
            lexer = get_lexer_for_filename(self.area.filename, '')
        except Exception:
            return

        lexer = get_lexer_for_filename(self.area.filename, '')
        TAG_KEYS_PRECEDENCE = PRECEDENCE_TABLE.get(
        tuple(lexer.aliases), DEFAULT)

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

        for ind in self.styles.iterkeys():
            self.area.tag_remove(str(ind), index0, index2)
        self.tag_tokens(lexer, index0, index2)

    def tag_tokens(self, lexer, index, stopindex):
        """
        Add the token'tag to each range of text.
        """

        count, offset = self.area.indref(index)
        tokens        = get_tokens_unprocessed_matrix(count, offset, 
        self.area.get(index, stopindex), lexer)

        for ((srow, scol), (erow, ecol)), token, value in tokens:
            self.area.tag_add(str(token), '%s.%s' % (srow, 
                 scol), '%s.%s' % (erow, ecol))

    def split(self, style):
        """
        Split the style into bg/fg values. Further compatibility 
        will be implemented.
        """

        sre = search('bg\:(?P<bg>.+) ?', style)
        bg  = sre.group('bg') if sre else self.background
        sre = search('(?P<fg>#.+) ?', style)
        fg  = sre.group('fg') if sre else self.default_style
        return bg, fg

    def set_token_style(self, token):
        """
        Configure the tag which maps to the token in the
        AreaVi. 
        
        If there is no such a definition of token
        in styles dict then it defaults to self.background 
        and self.default_style.
        """

        tag     = str(token)
        style   = self.get_token_style(token)
        bg, fg  = style if style else (self.background, self.default_style)
        self.area.tag_configure(tag, 
        foreground=fg, background=bg)

        # Note: It may be interesting to redefine
        # tag_configure in AreaVi and implement it there.
        self.area.tag_lower(tag, 'sel')

    def get_token_style(self, token):
        """
        Note: Styles dict is populated with all possible tokens. 
        It has to be written like this(without try/except block).
        """

        for ind in reversed(token.split()):
            style = self.styles.get(ind); 
            if  style: 
                return self.split(style)

install = Spider




