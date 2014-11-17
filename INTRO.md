
Mode System
===========

Vy implements a mode system. It means that when Vy is on mode 1 and you press 
Control-d then it will perform a different action from when Vy is on mode 2 and
you press Control-d.

Vy can have infinite modes. It means you can make it perform an infinite set of actions
whenever it happens an event like Control-d. So, it is possible to have a lot of new themes,
you can define your own themes(The way of how vy performs actions based on pressing of keys).

Vy has two main modes. The mode 1 and mode 0.
When Vy is on mode 0 you can insert text in the AreaVi that has focus.
When Vy is on mode 1, whenever you press a key Vy will perform an action corresponding to that key.

Mode 1
======

These commands are AreaVi oriented. It means that Vy will perform them based on the AreaVi instance that has focus.
AreaVi stands for the Text Area where you input text.

~~~
Key-i

It puts Vy on mode 0, it means you can insert text in the AreaVi instance that has focus.
~~~

~~~
Key-3

It puts Vy on mode 3.
~~~

~~~
Control-d

Pick up a file to edit in the AreaVi that has focus.
~~~


~~~
F8

Pick up a file to edit in a new tab.
~~~


~~~
F7

It adds a new tab.
~~~



~~~
Control-s

It dumps the text into the opened file from the AreaVi instance that has focus.
It basically means "Save".
~~~



~~~
Shift-s

Pick up a place where to save the text of the AreaVi instance that has focus.
~~~



~~~
Key-D

It clears all text in the text area.
~~~

~~~
Control-Escape

It saves the content of the text area then quits.
~~~

~~~
Shift-Escape

It quits.
~~~



~~~
F4

It adds a horizontal AreaVi instance.
~~~


~~~
F5

It adds a vertical AreaVi instance.
~~~



~~~
F6

It removes the AreaVi instance with focus.
~~~



~~~
End

It removes the selected tab.
~~~


~~~
Key-f

It adds selection to the line where the cursor is placed on.
~~~



~~~
Key-V

It removes selection from the character over the cursor. 
~~~



~~~
Key-C

It adds selection to the character over the cursor.
~~~

~~~
Key-x

It deletes the line whose cursor is on.
~~~

~~~
Key-z

It deletes a character over the cursor position.
~~~

~~~
Key-o

It puts the cursor over the start of the line. 
~~~

~~~
Key-p

It puts the cursor over the end of the line. 
~~~

~~~
Key-1

It puts the cursor in the start of the file.
~~~

~~~
Key-2

It puts the cursor in the end of the file.
~~~

~~~
Key-y

It copies selected text to the clipboard.
~~~

~~~
Key-u

It cuts selected text and append it to the clipboard.
~~~

~~~
Key-r

It pastes text from the clipboard one line down the cursor position.
~~~

~~~
Key-e

It pastes text from the clipboard one line up the cursor position.
~~~

~~~
Key-t

It pastes text from the clipboard on the cursor positon.
~~~

~~~
Key-d

It deletes everything that is selected.
~~~

~~~
Key-n

It inserts one line up the cursor position then goes to INSERT MODE.
~~~

~~~
Key-m

It inserts one line down the cursor position then goes to INSERT MODE.
~~~

~~~
Key-comma

It does undo on the text area.
~~~

~~~
Key-period

It does redo on the text area.
~~~

~~~
Key-bracketleft

It selects a word that is on the cursor.
~~~

The next key commands are used to talk with bash.

~~~
F1

It sends to the bash process the line text whose cursor is placed on.
The output is dumped over an AreaVi instance that you have marked with Key-Tab.

It places the cursor one line down after sending the line text.
~~~

~~~
Control-F1

It kills the actual bash process then starts other one.
It is useful if for some reason you got the processed hangged.
~~~

~~~
Return

It dumps the line text over the cursor but doesn't put the cursor one line down.
~~~

~~~
Control-backslash

It dumps to the bash process the signal SIGQUIT.
It makes the process being running on bash to quit.
~~~

~~~
Control-c

It dumps to the bash process the signal SIGINT.
~~~

~~~
Control-return

It dumps selected text to the bash.
~~~


Mode 0
======

~~~
Escape

It puts Vy on mode 1.
~~~

~~~
Control-q

It completes the actual word based on a search through all AreaVi instances.
~~~

~~~
F1

It sends to the bash process the line text whose cursor is placed on.
The output is dumped over an AreaVi instance that you have marked with Key-Tab.

It places the cursor one line down after sending the line text.
~~~


Mode 3
======

~~~
Escape

It puts Vy on mode 1.
~~~

~~~
Key-e

It comments a chunk of text that was previously selected. The comments are added based on the
file type that is being edited. 

It is useful when you are editing a program then you want to comment some block of code.
~~~

~~~
Key-r 

It takes off the comment from a previously selected block of text.
~~~

~~~
Key-q

It adds/removes a tag to the line which the cursor is placed on.
~~~

~~~
Key-a

It puts the cursor over the previous tag that was added with key-q.

It is useful to go back to regions of text that you were working on.
~~~

~~~
Key-s

It puts the cursor over the next tag that was added with Key-s.
~~~


~~~
Key-u

It appends to the clipboard the path of the file being edited.
~~~


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

    The name of a bitmap which is used as a stipple brush when drawing the text. Typical values are "gray12”, "gray25", "gray50", or "gray75". Default is a solid brush (no bitmap).
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


**It remains implementing docs for other key commands. These are the basic ones.**




