
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

The AreaVi/Text widget events
=============================

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

Running vy
==========

The statusbar
=============

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


Moving the cursor around
========================

Open a file
===========

Saving file changes
===================

Save as dialog window
=====================

Open a file from command line
=============================

Move cursor to the beginning of the line
========================================

Move cursor to the end of the line
==================================

Move cursor to the beginning of the file
========================================

Move cursor to the end of the file
==================================

Move forward one word
=====================

Move backward one word
======================

Moving forward to the next occurence of () {} []
================================================

Moving backward to the next occurrence of () {} []
==================================================

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

















