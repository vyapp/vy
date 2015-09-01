
Introduction
============

Vy is a powerful editor, it is powerful because it is written in python on top of tkinter that is one of the most productive
graphical toolkits ever. It is also powerful because it was designed with code clarity and modularity in mind. Everything
in vy is based on a modular approach. Everything is modular.

As vy is self documented, it means all plugins that are implemented just have docs explaning how to use the Key-Commands, the
best approach to write this intro is going through the plugins docs.

Vy is written in pure python, it gives the possibility of taking all power of vy with python, with no need for learning
a non mainstream language like vimscript or emacs lisp. It is possible to drop python code to vy then affect the state
of the editor in real time. 

Vy changes the way of the python interpreter instance that runs vy outputs stuff. It substitutes sys.stdout for a class that
manages where the interpreter should output data. In this way it is possible to redirect to different AreaVi instances
the output of what the interpreter should print to the real sys.stdout.

Vy implements mechanisms to drop python code to the python interpreter. The simplest mechanism is through
a Key-Command in NORMAL mode.

What is a modal editor?
======================

A modal editor is an editor that can be in different states. It performs different operations/tasks/actions
from each state it is in. When vy is NORMAL mode and you type <Key-j> it will make the cursor jump one line down.
When it is in INSERT mode and you type <Key-j> it will merely insert the character 'j' at the cursor position.

Vy differently from vim can have as many modes as it is needed. It means you can implement new modes
that perform all kind of actions/operations.


The Key-Commands definition
===========================

Along this intro i'll use some terms like Key-Commands, AreaVi instances. A Key-Command
is an event that happens when an AreaVi instance has focus. It is when you press some key
from your keyboard or open a file/save a file.

An AreaVi instance is a class instance of the Tkinter Text widget from which AreaVi inherits from.
AreaVi implements new features that turn the Text tkinter widget more powerful.
It is possible to create multiple AreaVi instances by creating new tabs or panes.

A Key-Command happens when there is a handle mapped to an event like 
    
    <Key-i>

It means when you press 'i' in a given mode, vy will call a handle mapped to that event that corresponds to the
mode in which vy is in.

It is possible to have multiple AreaVi instances that are in different modes. The mode statusbar field
shows in which mode the AreaVi instance that has focus is in.

Basic Modes
===========

The basic two modes of vy are NORMAL and INSERT. The normal mode is in which vy starts. The INSERT mode is used
to insert data in the AreaVi instance. In order to switch to INSERT mode from NORMAL mode you press 

    <Key-i>

The statusbar field Mode shows in which mode vy is in. Once you change to INSERT mode by pressing <Key-i> in NORMAL mode
it would appear on the status bar field Mode: INSERT. You can switch back to NORMAL mode by pressing 

    <Escape>

The NORMAL mode is where most basic plugins are implemented in. This mode offers all kind of handy Key-Commands
like opening files, saving files, jumping the cursor to positions, searching pattern of text, replacing ranges
of text etc.

Execute Inline Python
=====================

Before dropping python commands to vy it is needed to set where the output should be printed. For such you need
to use a Key-Command. Place the cursor in the AreaVi instance that you want to drop the output of the python commands
at the line.row then press 

    <Tab> 

in NORMAL mode. It will show on the status bar that the output was redirected to that position.

After redirecting the output, you're done, just press 

    <Key-semicolon>

in NORMAL mode. It will appear an input text field where you can drop python commands to vy 
whose output will be dropped at the AreaVi instance position that you have set.

Try inserting the following python code.

~~~python
    print 'Hello from vy'
~~~

After you press enter, the AreaVi instance from where you issued the event in NORMAL mode will regain 
the focus and the output from the command will be dropped at the position that you have set
as target output.

try now typing other commands like.

~~~python
for ind in xrange(10):
    print ind
~~~

Switch to INSERT mode by pressing 

    <Key-i>

or 'i' in NORMAL mode, insert some blank lines then
switch back to NORMAL mode by pressing 

    <Escape>

Then try picking up a different position where to drop python code output by pressing 

    <Tab>

in NORMAL mode.

You will notice that it is possible to set different places where to drop python code output.
It is particularly useful in some situations.

When dealing with vim, one drops vim commands to vim, when dealing with vy one inserts
python functions. You can define your own python functions inside plugins to perform 
all kind of different tasks.

Vy offers a consistent plugin interface with a powerful scheme to affect the state of the editor
through python code.

One can obtain help from a plugin doc definition by dropping.

~~~python
    help(vyapp.plugins.plugin_name)
~~~

The help for the plugin would be outputed on the AreaVi instance that you have set the drop mark.

Try getting help from 

~~~python
    help(vyapp.plugins.move_cursor)
~~~

The ALPHA mode
==============

The BETA mode
==============


Using vy as a terminal
======================


E-scripts
=========


The vy plugins
==============

Vy is highly modular, it permits a good level of self documentation. Every plugin
implemented in vy is self documented. The best way to get help is through our help python function.

Set the output target on an AreaVi instance with 

    <Tab> 

in NORMAL mode.

Press 

    <Key-semicolon> 

in NORMAL mode. It will show up an input text field then insert.

    help(vyapp.plugins.plugin_name) 

then press

    <Enter>

then it will output the docs for the plugin.

## Cursor movement

    Help on module vyapp.plugins.move_cursor in vyapp.plugins:
    
    NAME
        vyapp.plugins.move_cursor
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/move_cursor.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements the basic cursor movements.
        
        Usage
        =====
        
        The way to move the cursor up is by pressing <Key-k>, to move the cursor down <Key-j>,
        to move the cursor left <Key-h>, to move the cursor right <Key-l>. These events
        work in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-j> 
        Description: Move the cursor one line down.
        
        
        Mode: NORMAL
        Event: <Key-k> 
        Description: Move the cursor one line up.
        
        
        Mode: NORMAL
        Event: <Key-h> 
        Description: Move the cursor one character left.
        
        
        Mode: NORMAL
        Event: <Key-l> 
        Description: Move the cursor one character right.
    
    FUNCTIONS
        install(area)


That is great. You got your first help. Vy is self documented, that is our philosophy !


## Open, Save, files

    Help on module vyapp.plugins.io in vyapp.plugins:
    
    NAME
        vyapp.plugins.io
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/io.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements basic Key-Commands to open/save files.
        
        Usage
        =====
        
        It is possible to pops a file window selection to load the contents of a file
        in a given AreaVi instance by pressing <Control-d>.
        
        After some changes to a opened file it is possible to save the contents of the file
        by pressing <Control-s> in NORMAL mode.
        
        The way to save the contents of an AreaVi instance as a different filename is by
        pressing <Shift-S> in NORMAL mode. It will open a file save dialog to pick up a name.
        
        Sometimes it is handy to just save and quit, for such just press <Control-Escape> in NORMAL mode.
        You can just quit without saving by pressing <Shift-Escape> in NORMAL mode as well.
        
        There is a Key-Command to clean all the text from a given active AreaVi instance. For such
        type <Key-D> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Control-d>
        Description: It pops a file selection window to load the contents of a file.
        
        Mode: NORMAL
        Event: <Control-s>
        Description: It saves the content of the AreaVi instance into the opened file.
        
        Mode: NORMAL
        Event: <Shift-S>
        Description: It pops a save file dialog to save the contents of the active AreaVi
        instance with a different filename.
        
        Mode: NORMAL
        Event: <Key-D>
        Description: Clear all text of the active AreaVi instance.
        
        Mode: NORMAL
        Event: <Control-Escape>
        Description: Save and quit.
        
        Mode: NORMAL
        Event: <Shift-Escape>
        Description: Quit.
    
    FUNCTIONS
        install(area)
        
        load(area)
            It pops a askopenfilename to find a file to drop
            the contents in the focused text area.
        
        save(area)
            It just saves the text area contents into the    
            actual opened file.
        
        save_as(area)
            It pops a asksaveasfilename window to save the contents of
            the text area.
        
        save_quit(area)
            It saves the contents of the text area then quits.
    
    DATA
        ABORT = 'abort'
        ABORTRETRYIGNORE = 'abortretryignore'
        CANCEL = 'cancel'
        ERROR = 'error'
        IGNORE = 'ignore'
        INFO = 'info'
        NO = 'no'
        OK = 'ok'
        OKCANCEL = 'okcancel'
        QUESTION = 'question'
        RETRY = 'retry'
        RETRYCANCEL = 'retrycancel'
        WARNING = 'warning'
        YES = 'yes'
        YESNO = 'yesno'
        YESNOCANCEL = 'yesnocancel'
        root = <vyapp.app.App instance>
    

## Insert blank lines

    Help on module vyapp.plugins.insert_line in vyapp.plugins:
    
    NAME
        vyapp.plugins.insert_line
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/insert_line.py
    
    DESCRIPTION
        Overview
        ========
        
        It is handy to have Key-Commands to insert blank lines up/down the cursor when in NORMAL mode.
        
        Usage
        =====
        
        In NORMAL mode, type <Key-m> to insert a blank line down the cursor or <Key-n> 
        to insert a blank line up the cursor.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-m> 
        Description: Insert a line down then goes insert mode.
        
        
        Mode: NORMAL
        Event: <Key-n> 
        Description: Insert a line up then goes insert mode.
    
    FUNCTIONS
        insert_down(area)
        
        insert_up(area)
        
        install(area)
    
    
## Jump to the start/end of lines

    Help on module vyapp.plugins.jump_line_mark in vyapp.plugins:
    
    NAME
        vyapp.plugins.jump_line_mark
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/jump_line_mark.py
    
    DESCRIPTION
        Overview
        ========
        This plugin implements Key-Commands to make the cursor jump to the end/beginning of the line whose
        the cursor is on.
        
        Usage
        =====
        
        Sometimes it is handy to quickly jump to the beginning of the line whose cursor is on.
        For such, switch to NORMAL mode then press <Key-o>. To place the cursor at the end
        of the line just press <Key-p> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-o> 
        Description: Place the cursor at the beginning of the line.
        
        
        Mode: NORMAL
        Event: <Key-p> 
        Description: Place the cursor at the end of the line.
    
    FUNCTIONS
        install(area)
    
    
## Jump to the start/end of file

    Help on module vyapp.plugins.jump_text_mark in vyapp.plugins:
    
    NAME
        vyapp.plugins.jump_text_mark
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/jump_text_mark.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements two Key-Commands to make the cursor jump to the begining/end of the file.
        
        Usage
        =====
        
        In order to jump to the beginning of the file wherever the cursor is placed on, just type <Key-1>
        in NORMAL mode. To place the cursor at the end of file then type <Key-2> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-1> 
        Description: Place the cursor at the beginning of the file.
        
        
        Mode: NORMAL
        Event: <Key-2> 
        Description: Place the cursor at the end of the file.
    
    FUNCTIONS
        install(area)



## Create text marks/shade lines.

    Help on module vyapp.plugins.shade in vyapp.plugins:
    
    NAME
        vyapp.plugins.shade
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/shade.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements a handy functionality that is shading lines and being
        capable of making the cursor jump back/next to these shaded lines. It is basically a 
        mark system.
        
        Usage
        =====
        
        In order to shade a line it is neeeded to switch to ALPHA mode by pressing
        <Key-3> in NORMAL mode. Make sure the cursor is positioined over the line that 
        should be shaded/marked. 
        
        After being in ALPHA mode it is enough to type <Key-q> the line over the cursor 
        will be shaded according to the dictionary options passed to the install function.
        
        When it is needed to unshade a line, just put the cursor over the shaded line
        then switch to ALPHA mode then press <Key-q> it will toggle the selection.
        
        After having shaded/marked some lines it is possible to jump back/next to those
        lines by pressing <Key-a> or <Key-s> in ALPHA mode.
        
        Once the cursor is positioned on the right line , just press <Escape> to go
        back to NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: ALPHA
        Event <Key-q>
        Description: Shade/unshade a line.
        
        Mode: ALPHA
        Event: <Key-s>
        Description: Makes the cursor jump to the next shaded line from the cursor position.
        
        Mode: ALPHA
        Event: <Key-a>
        Description: Makes the cursor jump to the previous shaded line from the cursor position.
    
    FUNCTIONS
        go_next_shade(area)
        
        go_prev_shade(area)
        
        install(area, setup={'background': 'green', 'foreground': 'black'})
        
        toggle_shade(area)
    
    DATA
        TAG_SHADE = '_shade_'
    


## Managing tabs

    help(vyapp.plugins.notebook)


    Help on module vyapp.plugins.notebook in vyapp.plugins:
    
    NAME
        vyapp.plugins.notebook
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/notebook.py
    
    DESCRIPTION
        Overview
        ========
        
        Tabs are a great feature when manipulating several files. This plugin implements Key-Commands to create, 
        open files, change the focus between opened tabs.
        
        Usage
        =====
        
        The way to create a blank tab is by pressing <F7> in NORMAL mode.    
        It will open a new blank tab but keep the focus in the actual one.
        
        There is a handy Key-Command to create a tab and load the contents of a file into it.
        For such, just put in NORMAL mode then type <F8>. By pressig <F8> it pops a file
        selection window to pick up a file.
        
        Sometimes you will be done with a given tab, you can remove such a tab by pressing <Delete> in
        NORMAL mode.
        
        It is possible to change the focus left from a given tab by pressing <Shift-F9>
        or changing the focus right by pressing <Shift-F10>. These Key-Commands work regardless
        of the mode in which the active AreaVi instance is in. These Key-Commands work on -1 mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <F8>
        Description: It pops a file selection window to load the contents of a file in a new tab.
        
        Mode: NORMAL
        Event: <F7>
        Description: It creates a new blanktab.
        
        Mode: NORMAL
        Event: <Delete>
        Description: It removes the focused tab.
        
        Mode: -1
        Event: <Shift-F9>
        Description: It changes the focus left from a tab.
        
        Mode: -1
        Event: <Shift-F10>
        Description: It changes the focus right from a tab.
    
    FUNCTIONS
        install(area)
        
        load_tab()
            It pops a askopenfilename window to drop
            the contents of a file into another tab's text area.
        
        remove_tab()
            It removes the selected tab.
    
    DATA
        ABORT = 'abort'
        ABORTRETRYIGNORE = 'abortretryignore'
        CANCEL = 'cancel'
        ERROR = 'error'
        IGNORE = 'ignore'
        INFO = 'info'
        NO = 'no'
        OK = 'ok'
        OKCANCEL = 'okcancel'
        QUESTION = 'question'
        RETRY = 'retry'
        RETRYCANCEL = 'retrycancel'
        WARNING = 'warning'
        YES = 'yes'
        YESNO = 'yesno'
        YESNOCANCEL = 'yesnocancel'
        root = <vyapp.app.App instance>

## Managing panes

    help(vyapp.plugins.panel)


    Help on module vyapp.plugins.panel in vyapp.plugins:
    
    NAME
        vyapp.plugins.panel
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/panel.py
    
    DESCRIPTION
        Overview
        ========
        
        Panels are a cool way to perform some tasks. This plugin implements Key-Commands to create horizontal/vertical
        panes.
        
        Usage
        =====
        
        The idea consists of a single vertical paned window in which it is possible to create
        horizontal paned windows. Inside these horizontal paned windows it is possible to add vertical panes.
        
        Let us suppose there is one pane named A opened in a given tab. The cursor is active in the
        pane AreaVi named A.
        
            -----
            | A |
            -----
        
        After pressing <F4> in NORMAL mode you will get.
            
        ------------
        | A  |  B  |
        ------------
        
        Suppose now the cursor is over A or B. If you press <F5> in NORMAL mode 
        then you will get.
        
        ------------
        | A  |  B  |
        ------------
        |    C     |
        ------------
        
        Now, suppose the cursor is over C then you press again <F4> in NORMAL mode.
        Then you will get.
        
        ------------
        | A  |  B  |
        ------------
        | C  |  D  |
        ------------
        
        
        Consider the case that you want to remove a given pane. For such
        you place the cursor over the pane then type <F6>.
        
        It is handy to move the cursor around panes. For changing the cursor
        one pane left you type <F9>, changing the cursor one pane right then type <F10>.
        The keys used to change the cursor up/down are <F11> and <F12>. These 
        Key-Commands work in -1 mode.
        
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <F4>
        Description: Add a vertical pane.
        
        Mode: NORMAL
        Event: <F5>
        Description: Add a horizontal pane.
        
        Mode: NORMAL
        Event: <F6> 
        Description: Remove a pane.
        
        Mode: -1
        Event: <F9>
        Description: Change the cursor one pane left.
        
        Mode: -1
        Event: <F10>
        Description: Change the cursor one pane right.
        
        Mode: -1
        Event: <F11>
        Description: Change the cursor one pane up.
        
        Mode: -1
        Event: <F12>
        Description: Change the cursor one pane down.
    
    FUNCTIONS
        add_horizontal_area(area)
            It creates a new horizontal area.
        
        add_vertical_area(area)
            It opens a vertical area.
        
        go_down_area(area)
        
        go_left_area(area)
        
        go_right_area(area)
        
        go_up_area(area)
        
        install(area)
        
        remove_area(area)
            It removes the focused area.
    


## Jump through words

    Help on module vyapp.plugins.match_word in vyapp.plugins:
    
    NAME
        vyapp.plugins.match_word
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/match_word.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements Key-Commands to make the cursor jump to the next/previous word as well as
        selecting a given word when the cursor is on.
        
        Usage
        =====
        
        The cursor jumps to the next occurence of a word by pressing <Key-bracketright> in NORMAL mode,
        in order to make the cursor jumps to the previous occurrence of a word you type 
        <Key-braceright> in NORMAL mode.
        
        It is useful to have a word whose cursor is placed on sometimes.
        For such just press <Key-bracketleft> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: 1
        Event: <Key-bracketright> 
        Description: Place the cursor at the beginning of the next word.
        
        
        Mode: 1
        Event: <Key-braceright> 
        Description: Place the cursor at the beginning of the previous word.
        
        
        Mode: 1
        Event: <Key-bracketleft> 
        Description: Add selection to a word where the cursor is placed on.
    
    FUNCTIONS
        install(area)
    


## Jumping through symbols

    Help on module vyapp.plugins.match_sym in vyapp.plugins:
    
    NAME
        vyapp.plugins.match_sym
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/match_sym.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements two Key-Commands to do quick jumps with the cursor to match 
        the symbols.
        
            ( ) { } [ ] : .
        
        Usage
        =====
        
        Suppose you are editing a python file.
        
            # blah.py
            def alpha():
                pass
            
            
            def beta():
                pass
            
        Consider the cursor is placed in the beginning of the file, after pressing <Key-p> in NORMAL mode
        it will make the cursor jump to the next occurence of one of the 
        
            ( ) { } [ ] : .
        
        chars. It is useful to go through function definitions/block of codes.
        You can make the cursor jump back by pressing <Key-O> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-P> 
        Description: Place the cursor at the next occurrence of ( ) { } [ ] : .
        
         
        Mode: NORMAL
        Event: <Key-O> 
        Description: Place the cursor at the next occurrence of ( ) { } [ ] : .
    
    FUNCTIONS
        install(area)
    
    
## Commenting blocks of code.

    Help on module vyapp.plugins.inline_comment in vyapp.plugins:
    
    NAME
        vyapp.plugins.inline_comment
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/inline_comment.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements Key-Commands to comment and uncomment blocks of code.
        
        Usage
        =====
        
        In order to comment/uncomment a block of code it is needed to first select the region.
        
        Open a programming file then select some lines with <Key-f> in NORMAL mode then
        switch to ALPHA mode with <Key-3>.
        
        Once it is in ALPHA mode then type <Key-e> to comment or <Key-r> to uncomment
        the selected block of text.
        
        The block of code will be commented based on the programming comment style of the language.
        
        Key-Commands
        ============
        
        Mode: ALPHA
        Event: <Key-e>
        Description: Add inline comments to a selected block of text.
        
        Mode: ALPHA
        Event: <Key-r>
        Description: Remove inline comments from a selected block of text.
    
    FUNCTIONS
        add_inline_comment(area)
            It adds inline comment to selected lines based on the file extesion.
        
        install(area)
        
        rm_inline_comment(area)
            It removes the inline comments.
    
    DATA
        DEFAULT = '#'
        TABLE = {'c': '//', 'c++': '//', 'java': '//', 'py': '#', 'sh': '#'}
    


## Selecting blocks of code between ( ) { } [ ]

    help(vyapp.plugins.select_sym_pair)


    Help on module vyapp.plugins.select_sym_pair in vyapp.plugins:
    
    NAME
        vyapp.plugins.select_sym_pair
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/select_sym_pair.py
    
    DESCRIPTION
        Overview
        ========
        This plugin implements a Key-Command to select text between pairs of () [] {}.
        
        Usage
        =====
        
        When the cursor is placed over one of the () [] {} and the key press event
        <Key-slash> happens in NORMAL mode then the text between the pair will be selected.
        
        Such a behavior is useful when dealing with some programming languages like lisp.
        
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-slash> 
        Description: Select text between pairs of ( ) [] {} when the cursor
        is placed over one of these characters.
    
    FUNCTIONS
        install(area)


## Adding selection to pieces of text

    help(vyapp.plugins.select_text)


    
    Help on module vyapp.plugins.select_text in vyapp.plugins:
    
    NAME
        vyapp.plugins.select_text
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/select_text.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements Key-Commands to select ranges of text to the beginning/end of the file from the
        cursor position.
        
        Usage
        =====
        
        A simple way to select all text from the cursor position to the end of the AreaVi instance is by
        pressing <Control-Key-2> in NORMAL mode. The same behavior can be achieved to select
        all text to the beginning of the AreaVi instance by pressing <Control-Key-1> in NORMAL mode as well.
        
        Another possibility is selecting all text of the AreaVi instance, for such just press 
        <Control-a> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Control-Key-1> 
        Description: Add selection from the cursor positon to the beginning of the file.
        
        
        Mode: NORMAL
        Event: <Control-Key-2> 
        Description: Add selection from the cursor position to the end of the file.
        
        
        Mode: NORMAL
        Event: <Control-a> 
        Description: Add selection from the beginning to the end of the file.
    
    FUNCTIONS
        install(area)
    


## How to redo/undo operations

    help(vyapp.plugins.undo)


    Help on module vyapp.plugins.undo in vyapp.plugins:
    
    NAME
        vyapp.plugins.undo
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/undo.py
    
    DESCRIPTION
        Mode: 1
        Event: <Key-comma> 
        Description: Do undo.
        
        
        Mode: 1
        Event: <Key-period> 
        Description: Do redo.
    
    FUNCTIONS
        install(area)
    

## Copying to the clipboard the complete file path of the file being edited.

    help(vyapp.plugins.clipboard)


    Help on module vyapp.plugins.clipboard in vyapp.plugins:
    
    NAME
        vyapp.plugins.clipboard
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/clipboard.py
    
    DESCRIPTION
        Overview
        ========
        
        It is handy to quickly get the absolute path of the file that is being edited. This plugin
        implements a Key-Command for that.
        
        Usage
        =====
        
        When a file is opened, vy holds a complete path for the file. It is possible
        to put such a complete path in the clipboard area for other purposes. For such
        switch to ALPHA mode by pressing <Key-3> in NORMAL mode then press <Key-u>.
        
        After pressing <Key-u> in ALPHA mode there will appear a msg on the status bar notifying that
        the complete path was copied to the clipboard.
        
        Key-Commands
        ============
        
        Mode: ALPHA
        Event: <Key-u>
        Description: Copies the complete path of the file to the clipboard.
    
    FUNCTIONS
        clip_ph(area)
            Sends filename path to clipboard.
        
        install(area)
    

## Block selection

    Help on module vyapp.plugins.block_selection in vyapp.plugins:
    
    NAME
        vyapp.plugins.block_selection
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/block_selection.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements block selection of text.
        
        Usage
        =====
        
        There are situations where range selection is not sufficient. It may be needed
        to select blocks of text. For such, switch to NORMAL mode then place the cursor
        over the starting of the block that needs to be selected then press <Control-V>
        to drop a mark at that place. 
        
        After pressing <Control-V> there will appear a msg on the statusbar telling the block selection mark
        was dropped.
        
        In order to add selection to the region you use the keys <Control-K>, <Control-J>,
        <Control-H>, <Control-L> in NORMAL mode to move the cursor around then adding selection to the region.
        
        Whenever <Control-V> in NORMAL mode is pressed the block selection mark will change it turns possible to have
        multiple regions of text selected.
        
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Control-K> 
        Description: Add block selection one line up.
        
        
        Mode: NORMAL
        Event: <Control-J>
        Description: Add block selection one line down.
        
        Mode: NORMAL
        Event: <Control-H>
        Description: Add block selection one char left.
        
        Mode: NORMAL
        Event: <Control-L>
        Description: Add block selection one char right.
    
    FUNCTIONS
        drop_start_mark(area)
        
        install(area)
    

## Range Selection

    help(vyapp.plugins.range_selection)


    Help on module vyapp.plugins.range_selection in vyapp.plugins:
    
    NAME
        vyapp.plugins.range_selection
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/range_selection.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements range selection.
        
        Usage
        =====
        
        First of all it is needed to drop a selection mark to start range selection.
        Switch to NORMAL mode then type <Control-v>.
        
        Once the selection mark is dropped you can start selection by using the keys <Control-h>,
        <Control-j>, <Control-k>, <Control-l> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Control-k> 
        Description: Add/remove selection one line up from the initial selection mark.
        
        
        Mode: NORMAL
        Event: <Control-j> 
        Description: Add/remove selection one line down from the initial selection mark.
        
        
        Mode: NORMAL
        Event: <Control-l> 
        Description: Add/remove selection one character right from the initial selection mark.
        
        
        Mode: NORMAL
        Event: <Control-h> 
        Description: Add/remove selection one character left from the initial selection mark.
        
        
        Mode: NORMAL
        Event: <Control-v> 
        Description: Drop a selection mark.
    
    FUNCTIONS
        drop_selection_mark(area)
        
        install(area)
    

## Scroll line up/down

    Help on module vyapp.plugins.scroll_line in vyapp.plugins:
    
    NAME
        vyapp.plugins.scroll_line
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/scroll_line.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements Key-Commands to scroll lines.
        
        Usage
        =====
        
        In order to scroll the document one line up you press <Key-w> in NORMAL mode.
        To scroll one line down press <Key-s> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-w> 
        Description: Scroll one line up.
        
        
        Mode: NORMAL
        Event: <Key-s> 
        Description: Scroll one line down.
    
    FUNCTIONS
        install(area)
    


## Scroll page up/down

    Help on module vyapp.plugins.scroll_page in vyapp.plugins:
    
    NAME
        vyapp.plugins.scroll_page
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/scroll_page.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin turns possible to scroll pages.
        
        Usage
        =====
        
        Press <Key-q> in NORMAL mode to scroll one page up.
        Press <Key-a> in NORMAL mode to scroll one page down.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-q> 
        Description: Scroll a page up.
        
        
        Mode: NORMAL
        Event: <Key-a> 
        Description: Scroll one page down.
    
    FUNCTIONS
        install(area)


## Adding selection to lines

    help(vyapp.plugins.select_line)


    Help on module vyapp.plugins.select_line in vyapp.plugins:
    
    NAME
        vyapp.plugins.select_line
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/select_line.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements Key-Commands to select lines and chunks of text inside a line.
        
        Usage
        =====
        
        Once in NORMAL mode if you press <Key-f> then the line whose cursor is on will be selected.
        
        In order to select a given range of the line from the cursor position you can type <Control-o> that
        will select the range of the line starting from the cursor position to the beginning of the line.
        
        In order to select a range of the line from the cursor position to the end of the line you type
        <Control-p> in NORMAL mode.
        
        Key-Commands
        ============
        
        Mode: NORMAL
        Event: <Key-f> 
        Description: Add selection to a line over the cursor.
        
        Mode: NORMAL
        Event: <Control-o> 
        Description: Add selection from the cursor position to the beginning of the line.
        
        
        Mode: NORMAL
        Event: <Control-p> 
        Description: Add selection from the cursor position to the end of the line.
    
    FUNCTIONS
        install(area)
    
## The syntax highlight plugin

## The python debugger plugin
shit












