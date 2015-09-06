
Introduction
============

Vy is a powerful editor, it is powerful because it is written in python on top of tkinter that is one of the most productive
graphical toolkits ever. It is also powerful because it was designed with code clarity and modularity in mind. Everything
in vy is based on a modular approach. Everything is modular.

Vy is written in pure python, it gives the possibility of taking all power of vy with python, with no need for learning
a non mainstream language like vimscript or emacs lisp. It is possible to drop python code to vy then affect the state
of the editor in real time. 

Vy changes the way of the python interpreter instance that runs vy outputs stuff. It substitutes sys.stdout for a class that
manages where the interpreter should output data. In this way it is possible to redirect to different AreaVi instances
the output of what the interpreter should print to the real sys.stdout.

Vy implements mechanisms to drop python code to the python interpreter. The simplest mechanism is through
a Key-Command in NORMAL mode.

This INTRO goes through all standard cases of using vy as an editor/ide.

What is a modal editor?
======================

A modal editor is an editor that can be in different states. It performs different operations/tasks/actions
from each state it is in. When vy is NORMAL mode and you type <Key-j> it will make the cursor jump one line down.
When it is in INSERT mode and you type <Key-j> it will merely insert the character 'j' at the cursor position.

Vy differently from vim can have as many modes as it is needed. It means you can implement new modes
that perform all kind of actions/operations.

The AreaVi/Text widget events
=============================

What is a Key-Command?
======================

Along this intro i'll use some terms like Key-Commands, AreaVi instances. A Key-Command is
an event mapped to a handle/function. One way to generate an event is by pressing a key.

A Key-Command happens when there is a handle mapped to an event like 
    
    <Key-i>

It means when you press 'i' in a given mode, vy will call a handle mapped to that event that corresponds to the
mode in which vy is in.

It is possible to have multiple AreaVi instances that are in different modes. The mode statusbar field
shows in which mode the AreaVi instance that has focus is in.

An AreaVi instance is a class instance of the Tkinter Text widget from which AreaVi inherits from.
AreaVi implements new features that turn the Text tkinter widget more powerful.

Running vy
==========

Once vy is installed then open a terminal then type.

    vy

That is enough to have vy running. Notice that if you attempt to open an inexisting file
it will throw an exception informing that the file doesnt exist.

The statusbar
=============

The vy statusbar has fields to show messages, display the mode in which vy is in, show cursor line and column.
Some Key-Commands display messages to inform the user of the success of an operation.

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


The basic cursor movements
==========================

You can save a lot of time by using some movement commands. These are the basic commands to learn.
Run vy, it will be in NORMAL mode, press <Key-i> to switch to INSERT mode. Insert some
text in the AreaVi then switch back to NORMAL mode by pressing <Escape>.

Now that you have got some text in the AreaVi you can play with the Key-Commands to move the cursor
up, down, left, right.

Move the cursor left by pressing
    
    <Key-h>

Move the cursor right by pressing

    <Key-l>


Move the cursor up by pressing

    <Key-k>

Moving the cursor down by pressing

    <Key-j>

Practice these Key-Commands until you get used to them.


Open a file
===========

There is a way to open a file dialog window to pick a file. For such switch to NORMAL
by pressing 

    <Escape>

then press

    <Control-d>

It will open a file dialog window in which you can select a file to be opened.

Saving file changes
===================

There is a handy Key-Command to save file changes. Open a file, switch to INSERT
mode by pressing 

    <Key-i>

then insert some lines. Switch to NORMAL mode by pressing 

    <Escape>

then press

    <Control-s>

In case of failure or success a msg would appear on the statusbar.

Save as dialog window
=====================

It is possible to save a file with a new name by opening a save as dialog window.
Switch to NORMAL mode then press

    <Shift-s>

Open a file from command line
=============================

Pass the filenames to vy as arguments on the command line.

    vy file1 file2 file3 file4 ...

It would open four tabs.

Move cursor to the beginning of the line
========================================

Suppose you are editing the end a line then you decide you need to edit the beginning of the line.
You could spend some time by moving it character by character but that doesn't sound cool. There is 
a better way. Switch to NORMAL mode then press

    <Key-p>

Move cursor to the end of the line
==================================

Suppose now you are editing the end of the line then you decide to edit the beginning of the line. 
Just switch to NORMAL mode then press

    <Key-o>


Move cursor to the beginning of the file
========================================

This Key-Command spares a lot of time. Imagine as painful it would be move character by character
until the beginning of a big file when you were editting the end of it.
Switch to NORMAL mode then press

    <Key-1>

It will make the cursor jump to the beginning of the file.

Move cursor to the end of the file
==================================

As there is a Key-Command to move the cursor to the beginning of a file there should exist one
to move the cursor to the end of a file as well. For such, switch to NORMAL mode then press

    <Key-2>

Move forward one word
=====================

You can save a lot of time by using this Key-Command correctly. Sometimes it is faster
to move the cursor foward some words than using other means. Switch to NORMAL mode
then press

    <Key-bracketright>

that will place the cursor at the first char of the next word.

Move backward one word
======================

Suppose you have finished writting a phrase then you notice that one of the previous words of the
phrase has a typo. What do you do? Well, you switch to NORMAL mode then press

    <Key-braceright>

It will place the cursor at the first char of the previous word.
    
Moving forward to the next occurence of ( ) { } [ ] : .
=======================================================

This Key-Command spares some time when coding. Switch to NORMAL mode then press

    <Key-P>

Moving backward to the next occurrence of ( ) { } [ ] : .
=========================================================

As it is possible to move foward it is as well to move backward. For such, switch to NORMAL mode
then press

    <Key-O>

Next symbol search
==================

Previous symbol search
======================

Scrolling one line up
=====================

Scrolling one line down
=======================

Scrolling one page up
=====================

Scrolling one page down
=======================

Inserting a blank line up
=========================

Insertng a blank line down
==========================

Selecting a char
================

Selecting a line
================

Selecting a word
================

It is possible to select a word when the cursor is on by pressing


    <Key-bracketleft>

That is '['. This is very handy sometimes.

Selecting text between matching pairs () {} []
==============================================

Pasting selected text one line up
=================================

The Key-command

    <Key-e>

in NORMAL mode is meant to paste text one line up from the cursor line.


Pasting selected text one line down
===================================

The Key-Command

    <Key-r>

In NORMAL mode. 


Pasting selected text at the cursor position
============================================

The Key-Command

    <Key-t>

in NORMAL mode is meant to paste text at the cursor position.


Copying text
============

The Key-Command to copy text to the clipboard without cutting it is 

    <Key-y>

in NORMAL mode. In order to have text copied to the clipboard it is needed
to select some text. You can do it in so many different ways with vy.

For purposes of examplifying, open a file then
switch to NORMAL mode. Place the cursor over a line
then press

    <Key-f>

It will select the entire line, once it is selected.
Then press

    <Key-y>

The line will be copied to the clipboard, then you can paste it outside vy.

Deleting selected text
======================

Deleting a char
===============

Deleting a line
===============

Deleting a word
===============

Highlighting parenthesis
========================

Vy will highlight pairs of () [] {} whenever the cursor is placed on
one of these chars.

Creating marks/shading lines
============================

Undo/redo
=========

Placing the cursor at a given line.col
======================================

Quick pattern search
====================

Setting a pattern for search
============================

Setting a pattern for replacement
=================================

Searching a pattern up
======================

Searching a pattern down
========================

Replacing a pattern up
====================

Replacing a pattern down
======================

Replacing a pattern at the cursor position
==========================================

Searching a pattern inside a selected region
============================================

Replacing a pattern inside a selected region
============================================

Completing words
================


Opening files in panes/tabs from command line
=============================================

It is possible to open files from command lines in different panes/tabs.

Consider you have three files, alpha, beta, gamma.

if you type in a terminal

    vy -l "[[['alpha', 'beta'], ['gamma']]]"

Vy will open these three files in one tab.
It will look like.

    |Alpha|
    ----------------
    | alpha | beta |
    ----------------    
    |    gamma     |
    ----------------
    
If you hve four files, alpha, beta, gamma, zeta
then you type.

    vy -l "[[['alpha', 'beta'], ['gamma']], [['zeta']]]"


It will open alpha, beta, gamma in a tab and zeta in other tab.

    |Alpha|zeta|
    ----------------
    | alpha | beta |
    ----------------    
    |    gamma     |
    ----------------


If you switch the focused tab with <Shift-F10| to the right..


you will get.

    |Alpha|zeta|
    ----------------
    |              |
    |     zeta     |
    |              |
    ----------------


It is useful when dealing with some scheme of files. I use vy as a terminal like
because i use e-scripts to automatize all kind of tasks like pushing onto github etc.
So, i keep a quick-esc.sh file in which i open two panes, one for the file quick-esc.sh
and one for /dev/null.

    vy -l "[[['/home/tau/lib/esc-code/bash/cmd-esc.sh', '/dev/null']]]"
   

Syntax highlight
================

Commenting blocks of code
=========================

Copying to the clipboard the filename of the file being edited
==============================================================

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


Getting help 
============

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


The ALPHA mode
==============

The BETA mode
==============

The vyrc file
=============


Using vy as a terminal
======================

E-scripts
=========



















