"""
Syntax Highlight Plugin
==========================

This plugin is used to highlight code. 

It supports all programming languages that pygments supports.

Load
====

Just add to your vyrc.

    import vyapp.plugins.syntax.spider
    import vyapp.plugins.syntax.themes.sun
    autoload(vyapp.plugins.syntax.spider, vyapp.plugins.syntax.themes.sun.THEME, 10)
    

It stands for the theme to be used. 
    
    vyapp.plugins.syntax.themes.sun.THEME

The following themes are implemented so far.

    vyapp.plugins.syntax.themes.sun
    vyapp.plugins.syntax.themes.dark

It corresponds to how many lines up and down from the cursor position it will be analyzed when Escape is pressed.

    10

Usage
=====

Whenever Escape event occurs the code around the cursor is highlighted.
It means, whenever you press Escape you get your code around the cursor highlighted.


Theme Creation
==============

This syntax highlight plugin is based on pygments. 
With such an approach it turns easy to create your own themes.
For such, you just need to follow these steps.

- Create a file where you will define your theme like dark.py
- Place dark.py inside your ~/.vy folder
- Implement your theme in dark.py

**Implement a theme**

A theme is a python dictionary that holds pairs like

THEME = {
'Token.Text': {'background':'#fff1e8', 'foreground':''},
'Token.Text.Whitespace': {'background':'#fff1e8', 'foreground':''},
'Token.Error': {'background':'#fff1e8', 'foreground':''},
'Token.Name':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Attribute':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Builtin':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Builtin.Pseudo':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Class':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Constant':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Decorator':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Entity':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Exception':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Function':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Label':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Namespace':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Other':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Tag':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Variable':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Variable.Class':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Variable.Global':{'background':'#fff1e8', 'foreground':'black'},
'Token.Name.Variable.Instance':{'background':'#fff1e8', 'foreground':'black'},
'Token.Comment.Multiline':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Literal.String.Doc':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Heredoc':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Backtick':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Char':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Double':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Escape':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Interpol':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Other':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Regex':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Single':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Literal.String.Symbol':{'background':'#fff1e8', 'foreground':'#CC99FF'},
'Token.Comment':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Comment.Preproc':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Comment.Single':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Comment.Special':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Literal':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Literal.Date':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Keyword':{'background':'#fff1e8', 'foreground': 'brown'},
'Token.Keyword.Constant':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Keyword.Declaration':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Keyword.Namespace':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Keyword.Pseudo':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Keyword.Reserved':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Keyword.Type':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number.Bin':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number.Float':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number.Hex':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number.Integer':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number.Integer.Long':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Literal.Number.Oct':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Operator':{'background':'#fff1e8', 'foreground':'#6600FF'},
'Token.Operator.Word':{'background':'#fff1e8', 'foreground':'#6600FF'},
'Token.Punctuation':{'background':'#fff1e8', 'foreground':'brown'},
'Token.Generic':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Deleted':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Emph':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Error':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Heading':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Inserted':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Output':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Prompt':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Strong':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Subheading':{'background':'#fff1e8', 'foreground':'blue'},
'Token.Generic.Traceback':{'background':'#fff1e8', 'foreground':'blue'},
}


The dictionary at the right of the token name holds attributes for the tag matching the token property.
These attributes can be.

    The background color to use for text having this tag.
    Note that the bg alias cannot be used with tags; it is interpreted as bgstipple rather than background.
    background (color)

    The name of a bitmap which is used as a stipple brush when drawing the background. 
    Typical values are "gray12", "gray25", "gray50", or "gray75". Default is a solid brush (no bitmap).
    bgstipple (bitmap)


    The width of the text border. The default is 0 (no border).
    Note that the bd alias cannot be used with tags.

    borderwidth (distance)

    The name of a bitmap which is used as a stipple brush when drawing the text. Typical values are "gray12", "gray25", "gray50", or "gray75". Default is a solid brush (no bitmap).
    fgstipple (bitmap)

    The font to use for text having this tag.
    font (font)

    The color to use for text having this tag.
    Note that the fg alias cannot be used with tags; it is interpreted as fgstipple rather than foreground.
    foreground (color)


    Controls text justification (the first character on a line determines how to justify the whole line). Use one of LEFT, RIGHT, or CENTER. Default is LEFT.
    justify (constant)

    The left margin to use for the first line in a block of text having this tag. Default is 0 (no left margin).
    lmargin1 (distance)

    The left margin to use for every line but the first in a block of text having this tag. Default is 0 (no left margin).
    lmargin2 (distance)


    Controls if the text should be offset from the baseline. Use a positive value for superscripts, a negative value for subscripts. Default is 0 (no offset).
    offset (distance)


    If non-zero, the text widget draws a line over the text that has this tag. For best results, you should use overstrike fonts instead.
    overstrike (flag)


    The border style to use for text having this tag. Use one of SUNKEN, RAISED, GROOVE, RIDGE, or FLAT. Default is FLAT (no border).
    relief (constant)


    The right margin to use for blocks of text having this tag. Default is 0 (no right margin).
    rmargin (distance)


    Spacing to use above the first line in a block of text having this tag. Default is 0 (no extra spacing).
    spacing1 (distance)


    Spacing to use between the lines in a block of text having this tag. Default is 0 (no extra spacing).
    spacing2 (distance)


    Spacing to use after the last line of text in a block of text having this tag. Default is 0 (no extra spacing).
    spacing3 (distance)


    If non-zero, the text widget underlines the text that has this tag. For example, you can get the standard hyperlink look with (foreground="blue", underline=1). For best results, you should use underlined fonts instead.
    tabs (string)
    underline (flag)

    The word wrap mode to use for text having this tag. Use one of NONE, CHAR, or WORD.
    wrap (constant)

The ideal background should be the one that you have set in your vyrc.


Once you have implemented a dictionary with tokens and their settings.
You can load your theme with syntax plugin with.

    import vyapp.plugins.syntax.spider
    import dark
    autoload(vyapp.plugins.syntax.spider, dark, 10)

If you have placed dark.py inside your ~/.vy.
"""

from pygments.lexers import get_lexer_for_filename 
from vyapp.plugins.syntax.tools import *
from vyapp.tools.misc import exec_quiet, consume_iter

TAG_KEYS_PRECEDENCE =('Token.Comment.Multiline',
    'Token.Literal.String.Doc',
    'Token.Literal.String.Heredoc',
    'Token.Literal.String.Regex',
    'Token.Literal.String.Symbol',
    'Token.Literal.String',
    'Token.Literal.String.Other',
    'Token.Literal.String.Single',
    'Token.Comment.Preproc',
    'Token.Comment',
    'Token.Comment.Single',
    'Token.Comment.Special',
    'Token.Literal.String.Double',
    'Token.Literal.String.Backtick',
    'Token.Literal.String.Char',
    'Token.Literal.Number.Float',
    'Token.Punctuation',
    'Token.Operator',
    'Token.Name')



def install(area, theme, max=10):
    """
    """
    def update_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return

        index0 = area.index('@0,0')
        index0 = area.index('%s -%sl' % (index0, max))
        index0 = area.tag_next_occur(TAG_KEYS_PRECEDENCE, index0, 'insert', '1.0')
        index1 = '@%s,%s' % (area.winfo_height(), area.winfo_width())
        index2 = area.index(index1)
        index2 = area.index('%s +%sl' % (index1, max))
        index2 = area.tag_prev_occur(TAG_KEYS_PRECEDENCE, index2, 'insert', 'end')

        for ind in theme.keys():
            area.tag_remove(ind, index0, index2)

        colorize(area, lexer, theme, index0, index2)

    def start_scheme():
        lexer = None
        try:
            lexer = get_lexer_for_filename(area.filename, '')
        except Exception:
            return
        colorize(area, lexer, theme, '1.0', 'end')

    INSTALL = [(-1, '<<LoadData>>', lambda event: start_scheme()),
               (1, '<Escape>', lambda event: update_scheme())]

    area.tag_setup(theme)

    area.install(*INSTALL)








