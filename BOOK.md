Table of Contents
=================

  * [Introduction](#introduction)
  * [How to read this book?](#how-to-read-this-book)
  * [What is a modal editor?](#what-is-a-modal-editor)
  * [What is a keycommand?](#what-is-a-keycommand)
  * [Running vy](#running-vy)
  * [The statusbar](#the-statusbar)
  * [Basic Modes](#basic-modes)
  * [Other modes](#other-modes)
      * [The global mode](#the-global-mode)
      * [The ALPHA mode](#the-alpha-mode)
      * [The BETA mode](#the-beta-mode)
      * [The GAMMA mode](#the-gamma-mode)
      * [The DELTA mode](#the-delta-mode)
  * [Common keycommands](#common-keycommands)
      * [Basic movements](#basic-movements)
      * [Opening files](#opening-files)
      * [Saving file changes](#saving-file-changes)
      * [Save as dialog window](#save-as-dialog-window)
      * [Open a file from command line](#open-a-file-from-command-line)
      * [Move cursor to the beginning of the line](#move-cursor-to-the-beginning-of-the-line)
      * [Move cursor to the end of the line](#move-cursor-to-the-end-of-the-line)
      * [Move cursor to the beginning of the file](#move-cursor-to-the-beginning-of-the-file)
      * [Move cursor to the end of the file](#move-cursor-to-the-end-of-the-file)
      * [Move forward one word](#move-forward-one-word)
      * [Move backward one word](#move-backward-one-word)
      * [Search forward for ( ) \{ \} [ ] : \.](#search-forward-for--------)
      * [Search backward for ( ) \{ \} [ ] : \.](#search-backward-for--------)
      * [Scroll one line up](#scroll-one-line-up)
      * [Scroll one line down](#scroll-one-line-down)
      * [Scroll one page up](#scroll-one-page-up)
      * [Scroll one page down](#scroll-one-page-down)
      * [Insert a blank line up](#insert-a-blank-line-up)
      * [Insert a blank line down](#insert-a-blank-line-down)
      * [Toggle line selection](#toggle-line-selection)
      * [Select a word](#select-a-word)
      * [Select text between pairs () \{\} []](#select-text-between-pairs---)
      * [Drop a range selection mark](#drop-a-range-selection-mark)
      * [Add/remove range selection one line up](#addremove-range-selection-one-line-up)
      * [Add/remove range selection one line down](#addremove-range-selection-one-line-down)
      * [Add/remove range selection one char left](#addremove-range-selection-one-char-left)
      * [Add/remove range selection one char right](#addremove-range-selection-one-char-right)
      * [Drop a block selection mark](#drop-a-block-selection-mark)
      * [Add/remove block selection one line up](#addremove-block-selection-one-line-up)
      * [Add/remove block selection one line down](#addremove-block-selection-one-line-down)
      * [Add/remove block selection one char left](#addremove-block-selection-one-char-left)
      * [Add/remove block selection one char right](#addremove-block-selection-one-char-right)
      * [Paste text one line up](#paste-text-one-line-up)
      * [Paste text one line down](#paste-text-one-line-down)
      * [Paste text in the cursor position](#paste-text-in-the-cursor-position)
      * [Copy selected text](#copy-selected-text)
      * [Delete selected text](#delete-selected-text)
      * [Delete a char](#delete-a-char)
      * [Delete a line](#delete-a-line)
      * [Delete a word](#delete-a-word)
      * [Highlight pairs of () [] \{\}](#highlight-pairs-of---)
      * [Shade a line](#shade-a-line)
      * [Jump to the previous shaded line](#jump-to-the-previous-shaded-line)
      * [Jump to the next shaded line](#jump-to-the-next-shaded-line)
      * [Undo](#undo)
      * [Redo](#redo)
      * [Jump to a given Line\.Col position](#jump-to-a-given-linecol-position)
  * [JUMP\_NEXT mode](#jump_next-mode)
      * [Switch to JUMP\_NEXT mode](#switch-to-jump_next-mode)
      * [Switch to INSERT mode from JUMP\_NEXT mode](#switch-to-insert-mode-from-jump_next-mode)
      * [Select a range of text in JUMP\_NEXT mode](#select-a-range-of-text-in-jump_next-mode)
  * [JUMP\_BACK mode](#jump_back-mode)
      * [Switch to JUMP\_BACK mode](#switch-to-jump_back-mode)
      * [Switch to INSERT mode from JUMP\_BACK mode](#switch-to-insert-mode-from-jump_back-mode)
      * [Select a range of text in JUMP\_BACK mode](#select-a-range-of-text-in-jump_back-mode)
  * [Tabs](#tabs)
      * [Create a new tab](#create-a-new-tab)
      * [Open a file in a new tab](#open-a-file-in-a-new-tab)
      * [Move focus one tab left](#move-focus-one-tab-left)
      * [Move focus one tab right](#move-focus-one-tab-right)
      * [Move focus to a specific tab](#move-focus-to-a-specific-tab)
      * [Remove a tab](#remove-a-tab)
  * [Panes](#panes)
      * [Move focus one pane up](#move-focus-one-pane-up)
      * [Move focus one pane down](#move-focus-one-pane-down)
      * [Move focus one pane left](#move-focus-one-pane-left)
      * [Move focus one pane right](#move-focus-one-pane-right)
      * [Remove a pane](#remove-a-pane)
  * [Command line](#command-line)
      * [Opening files in panes/tabs from command line](#opening-files-in-panestabs-from-command-line)
  * [The screen search feature](#the-screen-search-feature)
  * [ISearch](#isearch)
  * [Search scheme](#search-scheme)
      * [Set a search pattern](#set-a-search-pattern)
      * [Set a replacement pattern](#set-a-replacement-pattern)
      * [Search up](#search-up)
      * [Search down](#search-down)
      * [Unshade matched patterns](#unshade-matched-patterns)
      * [Replace up](#replace-up)
      * [Replace down](#replace-down)
      * [Replace on](#replace-on)
      * [Search patterns inside selected text](#search-patterns-inside-selected-text)
      * [Replace matched patterns inside selected text](#replace-matched-patterns-inside-selected-text)
  * [Code execution](#code-execution)
      * [Execute Inline Python](#execute-inline-python)
      * [Set output targets](#set-output-targets)
      * [Remove output targets](#remove-output-targets)
      * [Restore the sys\.stdout object](#restore-the-sysstdout-object)
      * [Delete text that was dropped at an AreaVi instance fom sys\.stdout](#delete-text-that-was-dropped-at-an-areavi-instance-fom-sysstdout)
      * [Set an AreaVi instance as target for commands](#set-an-areavi-instance-as-target-for-commands)
      * [Execute selected regions of python code](#execute-selected-regions-of-python-code)
      * [The scope of plugin functions](#the-scope-of-plugin-functions)
  * [Getting help](#getting-help)
      * [List installed plugins](#list-installed-plugins)
      * [Print plugin help](#print-plugin-help)
  * [Syntax highlight](#syntax-highlight)
      * [Highlighting code](#highlighting-code)
      * [Changing syntax highlight style](#changing-syntax-highlight-style)
      * [Creating new syntax highlight styles](#creating-new-syntax-highlight-styles)
  * [Mode switch](#mode-switch)
  * [The PDB mode](#the-pdb-mode)
      * [Getting ready to debug a python application](#getting-ready-to-debug-a-python-application)
      * [Switch to PDB mode](#switch-to-pdb-mode)
      * [Start a process](#start-a-process)
      * [Start a process with command line arguments](#start-a-process-with-command-line-arguments)
      * [Set a break point](#set-a-break-point)
      * [Set a temporary break point](#set-a-temporary-break-point)
      * [Remove a breakpoint](#remove-a-breakpoint)
      * [Clear all break points](#clear-all-break-points)
      * [Run code step by step](#run-code-step-by-step)
      * [Stop at the next breakpoint](#stop-at-the-next-breakpoint)
      * [Print a stack trace most recent frame at the bottom](#print-a-stack-trace-most-recent-frame-at-the-bottom)
      * [Execute selected text in the current context](#execute-selected-text-in-the-current-context)
      * [Evaluate selected text in the current context](#evaluate-selected-text-in-the-current-context)
      * [Inject python code to be executed in the current context](#inject-python-code-to-be-executed-in-the-current-context)
      * [Inject python code to be evaluated in the current context](#inject-python-code-to-be-evaluated-in-the-current-context)
      * [Terminate the process](#terminate-the-process)
  * [The IRC mode](#the-irc-mode)
      * [Connect to an irc network](#connect-to-an-irc-network)
      * [Switch to IRC mode](#switch-to-irc-mode)
      * [Send IRC commands](#send-irc-commands)
      * [Identify nick](#identify-nick)
      * [Join a channel](#join-a-channel)
      * [Part from a channel](#part-from-a-channel)
      * [Change nick](#change-nick)
      * [Query an user](#query-an-user)
      * [Set IRC network output position](#set-irc-network-output-position)
      * [Create shortcut functions for IRC networks](#create-shortcut-functions-for-irc-networks)
  * [The ibash plugin](#the-ibash-plugin)
      * [First steps](#first-steps)
      * [Send a code line](#send-a-code-line)
      * [Send a SIGINT signal](#send-a-sigint-signal)
      * [Send a SIGQUIT signal](#send-a-sigquit-signal)
      * [Send code lines](#send-code-lines)
      * [Run a command as root](#run-a-command-as-root)
      * [Run a bash process as root](#run-a-bash-process-as-root)
      * [Starting processes](#starting-processes)
      * [Restart the bash process](#restart-the-bash-process)
  * [Misc](#misc)
      * [Word completion](#word-completion)
      * [Copy the opened file path to the clipboard](#copy-the-opened-file-path-to-the-clipboard)
      * [The python autocomplete plugin](#the-python-autocomplete-plugin)
      * [Comment a block of code](#comment-a-block-of-code)
      * [Uncomment a block of code](#uncomment-a-block-of-code)
  * [The plugin API](#the-plugin-api)
      * [The vyrc, plugin system and user plugin space](#the-vyrc-plugin-system-and-user-plugin-space)
      * [A help on Tkinter events](#a-help-on-tkinter-events)
      * [Playing with AreaVi widget](#playing-with-areavi-widget)
      * [What is a AreaVi/Text widget index?](#what-is-a-areavitext-widget-index)
      * [What are marks?](#what-are-marks)
      * [The basic AreaVi/Text widget marks](#the-basic-areavitext-widget-marks)
      * [What are tags?](#what-are-tags)
      * [The 'sel' tag and AreaVi\.tag\_add/AreaVi\.tag\_remove method](#the-sel-tag-and-areavitag_addareavitag_remove-method)
      * [The AreaVi\.tag\_ranges method](#the-areavitag_ranges-method)
      * [The AreaVi\.tag\_config method](#the-areavitag_config-method)
      * [The AreaVi\.search method](#the-areavisearch-method)
      * [The AreaVi\.find method](#the-areavifind-method)
      * [The AreaVi\.load\_data method](#the-areaviload_data-method)
      * [The AreaVi\.save\_data method](#the-areavisave_data-method)
      * [Vy Global Mode](#vy-global-mode)
      * [The AreaVi\.add\_mode and AreaVi\.chmode methods](#the-areaviadd_mode-and-areavichmode-methods)


Introduction
============

The vy editor is one of the most powerful text editors around. It has a great plugin API, a nifty scheme of keystrokes
and it is extremely efficient in terms of hardware resources. The vy power comes at a cost, however: When getting
started users face a sleep learning curve.

How to read this book?
======================

This book goes through all standard cases of using vy as an editor/ide. It describes some possible
scenaries in which the keycommands are useful as well as explain step by step how to use the keycommands.

This book should work as a complete introduction and a reference for vy editor. It covers all cases from
keystrokes to implementing new plugins. 

What is a modal editor?
=======================

A modal editor is an editor that can be in different states. It performs different actions
from each state it is in. When vy is NORMAL mode and you press:

    <Key-j> 

it will make the cursor jump one line down. When it is in INSERT mode and you press:

    <Key-j> 

it will merely insert the character 'j' at the cursor position.

The vy editor permits the implementation of new modes, it means that there could exist modes for
programming languages, filemanagers etc.

What is a keycommand?
=====================

Along this intro i'll use some terms like keycommands, AreaVi instances. A keycommand is a mapping 
between a keystroke event and a python function. When a key that generates an event is pressed and 
such an event is mapped to a function then a keycommand is performed.

A keycommand happens when there is a handle mapped to an event like:
    
    <Key-i>

It means when you press 'i' in a given mode, vy will call a handle mapped to that event that corresponds to the
mode in which vy is in.

It is possible to have multiple AreaVi instances that are in different modes. The mode statusbar field
shows in which mode the AreaVi instance that has focus is in.

An AreaVi instance is a class instance of the Tkinter Text widget from which AreaVi inherits from.
AreaVi implements new features that turn the Text widget more powerful.

Consider the following keycommand below:

    <Control-h>

In order to execute the code mapped to that event one would keep the Control key pressed
then press the key 'h'.

Consider now:

    <Control-H>

What does it mean? It means that to perform the keycommand above then one would keep the key Control pressed
then press 'H'.

Running vy
==========

Once vy is installed then open a terminal then type.

    vy

That is enough to have vy running. Notice that if you attempt to open an inexisting file
it will throw an exception informing that the file doesnt exist.

The statusbar
=============

The vy statusbar has fields to show messages, display the mode in which vy is in, show cursor line and column.
Some keycommands display messages to inform the user of the success of an operation.

Basic Modes
===========

The basic two modes of vy are NORMAL and INSERT. The NORMAL mode is in which vy starts. The INSERT mode is used
to insert data in the AreaVi instance. In order to switch to INSERT mode from NORMAL mode you press: 

    <Key-i>

The statusbar mode field shows in which mode vy is in. Once you change to INSERT mode by pressing <Key-i> in NORMAL mode
it would appear on the statusbar mode field: INSERT. You can switch back to NORMAL mode by pressing:

    <Escape>

The NORMAL mode is where most basic functinonalities are implemented in. This mode offers all kind of handy keycommands
like opening files, saving files, making the cursor jump to positions, searching pattern of text, replacing ranges
of text etc.

Other modes
===========

### The global mode

The global mode is a mode that if there is a handle/function mapped to an event in such a mode
then such a handle will be called no matter in which mode is in.

***

### The ALPHA mode

The ALPHA mode implements some keycommands that aren't very often used.
Switch to NORMAL mode then press:

    <Key-3>

It will appear in the statusbar mode field that vy is in ALPHA mode.
You can switch back to NORMAL mode by pressing:

    <Escape>

***


### The BETA mode

The BETA mode is an extra mode that may be used to implement extra functionalities. The PDB mode
is implemented in BETA mode.

In order to switch to BETA mode, press the key below in NORMAL mode:

    <Key-4>

***

### The GAMMA mode

The GAMMA mode is an extra mode. It is implemented in NORMAL mode:

    <Key-5>

It would get vy in GAMMA mode.

***

### The DELTA mode

DELTA is an auxiliary mode as ALPHA, BETA, GAMMA are. It is implemented in NORMAL mode:

    <Key-6>

It would get vy in DELTA mode.

***

Common keycommands
==================

### Basic movements

You can save a lot of time by using some keycommands. These are the basic keycommands to learn.
Run vy, it will be in NORMAL mode. 

Press the keycommand below to switch to INSERT mode:

    <Key-i> 

Insert some text in the AreaVi then switch back to NORMAL mode by pressing:

    <Escape>

Now that you have got some text then you can play with the keycommands below.

Move the cursor left by pressing:
    
    <Key-h>

Move the cursor right by pressing:

    <Key-l>


Move the cursor up by pressing:

    <Key-k>

Moving the cursor down by pressing:

    <Key-j>

***

### Opening files

There is a way to open a file dialog window to pick a file. For such switch to NORMAL
by pressing:

    <Escape>

Then press:

    <Control-d>

It will open a file dialog window in which you can select a file to be edited.

***

### Saving file changes

There is a handy keycommand to save file changes. Open a file, switch to INSERT
mode by pressing:

    <Key-i>

Insert some lines. Switch to NORMAL mode by pressing:

    <Escape>

Then press:

    <Control-s>

In case of failure or success a msg would appear on the statusbar.

***

### Save as dialog window

It is possible to save a file with a new name by opening a save as dialog window.
Switch to NORMAL mode then press:

    <Shift-s>

### Open a file from command line

Pass the filenames to vy as arguments on the command line:

    vy file1 file2 file3 file4 ...

It would open four tabs.

***

### Move cursor to the beginning of the line

Suppose you are editing the end a line then you decide you need to edit the beginning of the line.
You could spend some time by moving it character by character but that doesn't sound cool. 

Switch to NORMAL mode then press:

    <Key-p>

***

### Move cursor to the end of the line

Suppose now you are editing the end of the line then you decide to edit the beginning of the line. 

Switch to NORMAL mode then press:

    <Key-o>

***

### Move cursor to the beginning of the file

This keycommand spares a lot of time. Imagine as painful it would be moving the cursor
character by character until the beginning of a big file when you were editting the end of it.

Switch to NORMAL mode then press:

    <Key-1>

It will make the cursor jump to the beginning of the file.

***

### Move cursor to the end of the file

As there is a keycommand to move the cursor to the beginning of a file there should exist one
to move the cursor to the end of a file as well. For such, switch to NORMAL mode then press:

    <Key-2>

***

### Move forward one word

You can save a lot of time by using this keycommand correctly. Sometimes it is faster
to move the cursor foward some words than using other means. Switch to NORMAL mode
then press:

    <Key-bracketright>

That will place the cursor on the first char of the next word.

***

### Move backward one word

Suppose you have finished writting a phrase then you notice that one of the previous words of the
phrase has a typo. What do you do? Well, you switch to NORMAL mode then press:

    <Key-braceright>

It will place the cursor on the first char of the previous word.
    
***

### Search forward for ( ) { } [ ] : .

I use this keycommand to spare time when looking for typos in programming files 
or jumping quickly through blocks of code in java/c.

Switch to NORMAL mode then press:

    <Key-P>

It will put the cursor on the next occurrence of one of the:

    () {} [] : .

***

### Search backward for ( ) { } [ ] : .

This keycommand is used more than its friend, i use it whenever i'm finishing to write
some statement then i notice i made a typo in the middle of the line.

Switch to NORMAL mode then press:

    <Key-O>

That would put the cursor on the previous occurrence of the symbols.

***

### Scroll one line up

The keycommand to scroll one line up is implemented in NORMAL mode. Open a file with
some pages then press:

    <Key-w>

It will scroll one line up. The cursor wouldn't change its position as long it remains
visible.

***

### Scroll one line down

This keycommand is implemented in NORMAL mode as the one to scroll one line up.
Open a file with a considerable number of pages then press:

    <Key-s>

The cursor would remain at its position as long it stays visible.    

***

### Scroll one page up

This keycommand works in NORMAL mode, open a file with some pages then press the keycommand below
to make the cursor jump to the end of the file:

    <Key-2>

Then press:

    <Key-q>

***

### Scroll one page down

In NORMAL mode, open some big file then try pressing:

    <Key-a>

***

### Insert a blank line up

This command works in NORMAL mode, it inserts a blank line above the cursor position
then puts vy in INSERT mode. 

Put the cursor over a non blank line then press:

    <Key-n>

***

### Insert a blank line down

As the keycommand to insert a blank line up, this one works in NORMAL mode. 
Put the cursor over a line then press:

    <Key-m>

It will insert a blank line below the cursor line then put vy in INSERT mode.

***

### Toggle line selection

Sometimes one is interested to copy just the line which the cursor is on. This keycommand
selects the line.

Switch to NORMAL mode then put the cursor over a line then press:

    <Key-f>

If you press the same keystroke then the line will be unselected.

***

### Select a word

It is possible to select a word when the cursor is on by pressing:


    <Key-bracketleft>

That is '['. This is very handy sometimes.

***

### Select text between pairs () {} []

I used this keycommand a lot when i was playing with scheme. It selects
the text between matching pairs of the symbols below:

    () {} []

Place the cursor on one of the symbols above, considering it is a matching pair, then 
press:

    <Key-slash>

***

### Drop a range selection mark

A range selection mark is a mark in the text to be used to add selection up/down/right/left.
In order to drop a range selection mark, switch to NORMAL mode then press:

    <Control-v>

It will appear a msg on the statusbar saying that mark selection was dropped at the cursor
position. The keycommands to add selection up/down/left/right use this mark as a reference.

***

### Add/remove range selection one line up

Once a range selection mark was dropped, press the below keycommand in NORMAL mode:

    <Control-k>

It will select/unselect one line up from the range selection mark position.

***

### Add/remove range selection one line down

There is a keycommand to add/remove range selection one line down, such a keycommand works in NORMAL mode as well.
Drop a selection range mark then press:

    <Control-j>

That will add/remove range selection one line down from the range selection mark position.

***

### Add/remove range selection one char left

The keycommand below add/remove selection from the range selection mark:

    <Control-h>

***

### Add/remove range selection one char right

The keycommand below add/remove selection from the range selection mark position:

    <Control-l>

***

### Drop a block selection mark

Block selection works with a mark as range selection does. In order to drop a block selection
mark, switch to NORMAL mode then press:

    <Control-V>

It will appear a msg on the statusbar saying that a block selection mark was dropped at the cursor position.

***

### Add/remove block selection one line up

Once a block selection mark was dropped, press the keycommand below in NORMAL mode to add/remove block selection one line up:

    <Control-K>

***

### Add/remove block selection one line down

Switch to NORMAL mode then press:

    <Control-J>

You need to have first dropped a block selection mark.

***

### Add/remove block selection one char left

This command works as well in NORMAL mode, supposing you have dropped a block selection mark.

Press:

    <Control-H>
***

### Add/remove block selection one char right

Make sure you have dropped a block selection mark then press:

    <Control-L>

### Paste text one line up

In order to better understand how to paste text one line up, place the cursor at a given line
then select it by pressing the keycommand below in NORMAL mode:

    <Key-f>

Then copy the line with.

    <Key-y>

Place the cursor one line down from where to paste the text then press:

    <Key-e>

That will paste the copied text at the beginning of the line above the cursor.

***

### Paste text one line down

Switch to NORMAL mode, place the cursor in the middle of a line then press:

    <Control-P>

The above keycommand will select a range of the line from the cursor position 
to the end of the line.

Then copy the selected text by pressing:

    <Key-y>

Now that there is text in the clipboard, press:

    <Key-r>

It will paste the selected range of the line at the beginning of the next line.

***

### Paste text in the cursor position

Switch to NORMAL mode, place the cursor in the middle of a line then press the below command 
to copy a range of text from the cursor position to the end of line:

    <Control-o>

Press the keycommand below to copy the selected text to the clipboard:

    <Key-y>

Then move the cursor to a given position then press:

    <Key-t>

It will paste the copied text in the cursor position.

***

### Copy selected text

The keycommand to copy text to the clipboard is:

    <Key-y>

in NORMAL mode. In order to have text copied to the clipboard it is needed
to select some text. You can do it in so many different ways with vy.

Open a file then switch to NORMAL mode. Place the cursor over a line
then press the key below to select the entire line:

    <Key-f>

Then press:

    <Key-y>

The line will be copied to the clipboard.

***

### Delete selected text

There is a keycommand that deletes all selected text. Switch to NORMAL mode,
place the cursor over a line then press the keycommand below to select the line:

    <Key-f>

Move the cursor around then select some other lines.
Now, press:

    <Key-d>

You will notice all the selected text was deleted.

***

### Delete a char

I don't use this command very much but its useful sometimes.
Switch to NORMAL mode, then place the cursor over a character.

Now, try to press a few times the keycommand:

    <Key-z>

***

### Delete a line

I use this one a lot. Switch to NORMAL mode then place the cursor at a given line, then press:

    <Key-x>

It will delete the line.

***

### Delete a word

There is not a specific command to delete a word although it is achievable
by selecting the word in which the cursor is placed on. For such press:

    <Key-bracketleft>

in NORMAL mode then press:

    <Key-d>

It will delete the selected text that is a word.

***

### Highlight pairs of () [] {}

Vy will highlight pairs of () [] {} whenever the cursor is placed on
one of these chars.

***

### Shade a line

Sometimes we need to create marks to remember text positions. The way to create a mark
in vy is by shading a line. Switch to NORMAL mode, then place the cursor on the desired line
and press the keycommand below to switch to ALPHA mode:

    <Key-3>

Once in ALPHA mode, press:

    <Key-q>

It will shade the line, in order to unshade just press again the same Key-Comamnd.

***

### Jump to the previous shaded line

This is useful to remember positions of the text. Switch to ALPHA mode by pressing:

    <Key-3>

then press:

    <Key-a>

It will make the cursor jump to the previous shaded line.

***

### Jump to the next shaded line

This makes the cursor jump to the next shaded line. Switch to ALPHA mode
then shade a line that is in the middle of the file, then switch back to NORMAL mode.

Press:

    <Key-1>

to make the cursor jump to the beginning of the file. Now, switch back to ALPHA mode
then press:

    <Key-s>

It will make the cursor jump to the next shaded line.

***

### Undo 

After some keycommand is performed you can undo the text changes by pressing in NORMAL mode the 
keycommand below:

    <Key-comma>


***

### Redo

Consider the situation that you have performed some keycommands then decided to undo the
text operations but you notice you just were mistaken when undoing the text operations. What would you do?
Well, i would press in NORMAL mode the following keycommand below:

    <Key-period>

***

### Jump to a given Line.Col position

Switch to NORMAL mode, then press:

    <F3>

It will appear an inputbox widget in which you can insert the desired position
to place the cursor on. Try inserting the following values

    3

    4 

    4.2

    2.3

In a file with more than 5 lines.

***

JUMP_NEXT mode
==============

There are circumstance that some keycommands wouldn't work well to place the cursor
at the desired position. This mode will solve the problem. 

When vy is in JUMP_NEXT mode and you press some key then the cursor will be placed on the 
next char that corresponds such a key.

### Switch to JUMP_NEXT mode

Turn the NORMAL mode on, then press:

    <Key-v>

It will appear JUMP_NEXT in the statusbar mode field. 

Press some key that maps to a printable character that is ahead of the cursor position 
then the cursor will jump to the corresponding char.

### Switch to INSERT mode from JUMP_NEXT mode

When in JUMP_NEXT mode it is possible to switch to INSERT mode by pressing:

    <Tab>

It spares some time in some occasions.

***

### Select a range of text in JUMP_NEXT mode

When in JUMP_NEXT mode it is possible to press:

    <Control-v>

It will select the range of text between the initial cursor position to the current cursor position.
It drops a range selection mark when it enters JUMP_NEXT mode.

***

JUMP_BACK mode
==============

This mode performs the opposite of the JUMP_NEXT, it places the cursor on the previous occurrence
of a char. 

### Switch to JUMP_BACK mode

Switch to NORMAL mode then press:

    <Key-c>

Vy will be in JUMP_BACK mode. Press some key that maps to a printable char then
the cursor will jump to the previous occurrence of the char.

### Switch to INSERT mode from JUMP_BACK mode

In order to spare some time when in JUMP_BACK mode it is possible to press:

    <Tab>

Then get in INSERT mode.

***

### Select a range of text in JUMP_BACK mode

When in JUMP_BACK mode it is possible to press:

    <Control-v>

It will select the range of text between the initial cursor position to the current cursor position.
It drops a range selection mark when it enters JUMP_BACK mode.

***

Tabs
====

### Create a new tab

Switch to NORMAL mode then press:

    <F7>

### Open a file in a new tab

In order to open a file in a new tab, switch to NORMAL mode then press:

    <F8>

It shows a file dialog window to select a file to be opened in a new tab.

***

### Move focus one tab left

It is possible to open files in multiple tabs, there is a handy keycommand to move the focus
between tabs. For moving focus one tab left, press the keycommand below regardless of the mode
that vy is in. The keycommand below works in GLOBAL mode it is a mode whose events have their handles
called regardless of the mode in which an AreaVi instance is in:

    <Alt-o>

***

### Move focus one tab right

In order to move the focus one tab right, press the keycommand below:

    <Alt-p>

***

### Move focus to a specific tab

Imagine that there are a lot of opened tabs it would spend some time to get a specific tab 
focused by moving focus one by one. This keycommand solves that problem.

The keycommand below is used to move focus to a tab whose title matches a given pattern.

    <Alt-i>

It will open an input text area to type part of the tab title. 

### Remove a tab

In order to remove the focused tab, press in NORMAL mode the keycommand below:

    <Delete>

***

Panes
=====

### Move focus one pane up

It is possible to have more than one file opened per tab, to move the focus
one pane up, press:

    <Key-K>

in NORMAL mode.

***

### Move focus one pane down

In order to move focus one pane down, switch to NORMAL mode then press:


    <Key-J>

***

### Move focus one pane left

Switch to NORMAL mode then press:

    <Key-H>

to move the focus one pane left.

***

### Move focus one pane right

In order to move focus one pane right, switch to NORMAL mode then press:

    <Key-L>

***

### Remove a pane

The way to remove a focused pane is by pressing:

    <F6>

in NORMAL mode.

***

Command line
============

### Opening files in panes/tabs from command line

It is possible to open files from command lines in different panes/tabs.

Consider you have three files, alpha, beta, gamma.

if you type in a terminal:

    vy -l "[[['alpha', 'beta'], ['gamma']]]"

The vy editor will open these three files in one tab.
It will look like:

    |Alpha|
    ----------------
    | alpha | beta |
    ----------------    
    |    gamma     |
    ----------------
    
If you hve four files, alpha, beta, gamma, zeta
then you type:

    vy -l "[[['alpha', 'beta'], ['gamma']], [['zeta']]]"


It will open alpha, beta, gamma in a tab and zeta in other tab:

    |Alpha|zeta|
    ----------------
    | alpha | beta |
    ----------------    
    |    gamma     |
    ----------------


If you switch the focused tab with <Shift-F10| to the right then you will get:

    |Alpha|zeta|
    ----------------
    |              |
    |     zeta     |
    |              |
    ----------------


It is useful when dealing with some scheme of files. I use vy as a terminal like
because i use e-scripts to automatize all kind of tasks like pushing onto github etc.
So, i keep a quick-esc.sh file in which i open two panes, one for the file quick-esc.sh
and one for /dev/null like:

    vy -l "[[['/home/tau/lib/esc-code/bash/cmd-esc.sh', '/dev/null']]]"
   

***


The screen search feature
=========================

This is an awesome feature in which one can do searches through the visible region of the document. It does searches
from the beginning of the visible region of the document until the end of the visible region. Such a feature
permits quickly placing the cursor at the desired position in the visible region of the document.

Consider the following piece of text.

    1 The text contains hyperlinks between the two parts, allowing you to quickly
    2 jump between the description of an editing task and a precise explanation of
    3 the commands and options used for it.  Use these two commands:
    
    4 Press  CTRL-]  to jump to a subject under the cursor.
    5 Press  CTRL-O  to jump back (repeat to go further back).
    
    6 Many links are in vertical bars, like this: |bars|.  The bars themselves may
    7 be hidden or invisible, see below.  An option name, like 'number', a command
    8 in double quotes like ":write" and any other word can alsooo be used as a link.
    9 Try it out: Move the cursor to  CTRL-]  and press CTRL-] on it.
    
Suppose the cursor is placed at the first line, you decide you need to fix the word 'alsooo' whose line index is 8.
What do you do? Well, you could jump to the line index 8 then go word by word. The  best way to place the cursor over the 
word 'alsooo' is using the screen search feature. 

In order to better elucidade the situation, run vy then copy the text shown above to an AreaVi instance then switch
to NORMAL mode and press:

    <Key-g>

You will notice that an inputbox widget was displayed. Try typing the sequence of characters below:
    
    in als

It will place the cursor at the beginning of the word 'alsooo' :)

You can make the cursor jump to the next possible match by pressing:

    <Control-j>

If you want to go back to the previous match:

    <Control-k>

If you think you typed wrong pattern you can delete a char from it with:

    <BackSpace>

You can switch back to NORMAL mode by pressing:

    <Escape>

The cursor will remain at the matched pattern position.

***

ISearch
=======

Isearch is a vy plugin that permits to find occurrences of word patterns along the text
regardless of the order of the words in the input.

Consider an AreaVi instance with the following data:

~~~
word1 word2 word3 word4 word10
word5 word6 word7 word8 word11 word2
word1 word3 word7 word4 word15
word3 word2 word5 word8
~~~

If you press the key command below in NORMAL mode.

    <Key-0>

It will show up an input box where it is possible to type text. 
Type the following sequence of words then press <Return>.

~~~
word4 word1
~~~

It will highlight the first phrase in which the words 'word4' and 'word1' appear on.
The keycommand below is used to highlight the next possible match:

    <Control-j>

While this one is used to go back to the previous match:

    <Control-k>   


If you give the input:

~~~
word2 word5 word11
~~~

It would highlight the first line in which the words 'word2', 'word5', 'word11' appear regardless of the order.
Use the keycommands to highligh the next lines

Search scheme
=============

### Set a search pattern

Vy uses tcl regex scheme, you can insert a regex pattern to be used later by switching to NORMAL mode
then pressing:

    <Control-q>

It will open an input text widget in which you can insert a regex pattern.

***

### Set a replacement pattern

After setting a pattern for search you can set a string to replace the occurrence of the search pattern.
You achieve it by switching to NORMAL mode then pressing:

    <Control-Q>

***

### Search up

Once a search pattern is set, it is possible to make the cursor jump to the previous occurence of the pattern
from the cursor position by pressing:

    <Control-Up>

In NORMAL mode.


***

### Search down

After having set a search pattern, press the keycommand below in NORMAL mode:

    <Control-Down>

It will make the cursor jump to the next occurrence of the pattern.

***

### Unshade matched patterns

After a pattern is matched it gets shaded, in order to unshade them, press:

    <Key-Q>

In NORMAL mode.

***

### Replace up

Once a replacement text was set, press the keycommand below in NORMAL mode to replace all occurrences
of the search pattern found up the cursor position:

    <Shift-Up>

***

### Replace down

Set a replacement and a search pattern, then press the keycommand below in NORMAL mode:

    <Shift-Down>

That will replace all occurrences of the pattern down the cursor position.

***

### Replace on

Set a pattern and a replacement for the pattern. Make the cursor jump back/next to the pattern. 
Once the cursor is positioned at the pattern then press the keycommand below in NORMAL mode:

    <Control-Right>

The matched pattern will be replaced for the previously set replacement. This keycommand is
specially useful when one doesn't know which matched pattern should be replaced really.

***

### Search patterns inside selected text

This is a powerful feature. One could select ranges of text then do
searches inside these ranges. The matched patterns will be highlighed.

First, use range selection or block selection or whatever other kind of selection to select some
region. Set a search pattern then switch to NORMAL mode and press:

    <Control-Left>

The matched patterns will be highlighed.

***

### Replace matched patterns inside selected text

Once a pattern is set, a replacement is set, then one can do replacement for the matched patterns
inside a selected region by pressing the keycommand below in NORMAL mode:

    <Shift-Right>

***

Code execution
==============

### Execute Inline Python

Before dropping python commands to vy it is needed to set where the output should be printed. For such you need
to use a keycommand. Place the cursor in the AreaVi instance that you want to drop the output of the python commands
at the line.row then press:

    <Tab> 

in NORMAL mode. It will show on the status bar that the output was redirected to that position.

After redirecting the output, you're done, just press:

    <Key-semicolon>

in NORMAL mode. It will appear an input text widget where you can drop python commands to vy 
whose output will be dropped at the AreaVi instance position that you have set as output target.

Try inserting the following python code:

~~~python
    print 'Hello from vy'
~~~

After you press enter, the AreaVi instance from where you issued the event in NORMAL mode will regain 
the focus and the output from the command will be dropped at the position that you have set
as target output.

Try now typing other commands like:

~~~python
for ind in xrange(10):
    print ind
~~~

Switch to INSERT mode by pressing:

    <Key-i>

or 'i' in NORMAL mode, insert some blank lines then
switch back to NORMAL mode by pressing:

    <Escape>

Then try picking up a different position where to drop python code output by pressing:

    <Tab>

in NORMAL mode.

You will notice that it is possible to set different places where to drop python code output.
It is particularly useful in some situations.

When dealing with vim, one drops vim commands to vim, when dealing with vy one inserts
python functions. You can define your own python functions inside plugins to perform 
all kind of different tasks.

Vy offers a consistent plugin interface with a powerful scheme to affect the state of the editor
through python code.

***

### Set output targets

The default sys.stdout object is replaced by a new class that redirects the output of python code
to AreaVi instances. It is possible to make output of python code be dropped over multiple AreaVi
instances by switching the focus to the AreaVi instance then pressing

    <Tab>

in NORMAL mode. Once an output target is added then a message at the statusbar
will show the row and col at where python code output will be dropped.

### Remove output targets

When it is no more needed to have output of python code dropped over a given AreaVi instance then
switch the focus to the AreaVi instance and press:

    <Control-w>

in NORMAL mode.


### Restore the sys.stdout object

When it is needed to have the sys.stdout object restored to its default value, just switch
to NORMAL mode then press:

    <Control-Tab>

### Delete text that was dropped at an AreaVi instance fom sys.stdout

Switch the focus to the AreaVi instance that the text was dropped from sys.stdout
then press in NORMAL mode:

    <Control-W>

***

### Set an AreaVi instance as target for commands

Some of vy plugins expose some functions/commands that work on the concept of an AreaVi target. Some functions operate on
AreaVi instances, an example is the CPPaste() function that posts code onto codepad.org. Code that is executed
using the key command below in NORMAL mode it has the last AreaVi instance that had focus as target:


    <Key-semicolon>


But code that is executed from selected regions of text can have a different AreaVi instance as target to operate on.
In order to set an AreaVi instance as target, switch to NORMAL mode then press:

    <Control-E>

The msg 'Target set!' would appear on the status bar. Once the target is set then it is possible
to execute python functions from selected regions of text that operate on the AreaVi instance that was set
as target. 

Try setting a command target then executing CPPaste() from other AreaVi instance with the following command
in NORMAL mode after having selected the text 'CPPaste()':

    <Control-e>

***

### Execute selected regions of python code

Select a region of text that corresponds to python code then switch to NORMAL mode and press:

    <Control-e>

Make sure you have set an output target in case of the code producing some output. In
order to set an output target, switch to the areavi instance that will be the output target
then switch to NORMAL mode and press:

    <Tab>

***

### The scope of plugin functions

It is possible to expose python functions to be executed through vy. These functions can perform all kind of
tasks like posting code onto codepad or capitalizing selected text. These functions are implemented in modules
that expose up in.

~~~python
vyapp.plugins.ENV
~~~

When code is executed through the key commands below then it is executed in the dictionary shown above:

    <Control-e>

or:

    <Key-semicolon>

***

Getting help
============

Every plugin implemented in vy is self documented. A good way to get help 
is through the help python function and dir function.

### List installed plugins

Set an output target on an AreaVi instance then execute the python code below:

~~~python
print dir(vyapp.plugins)
~~~

### Print plugin help

In order to get builtin help for the main_jumps plugin one would set the output 
target on an AreaVi instance then run the python code below:

~~~python
help(vyapp.plugins.main_jumps) 
~~~

Then it will output the docs for the plugin.

    Help on module vyapp.plugins.main_jumps in vyapp.plugins:
    
    NAME
        vyapp.plugins.main_jumps
    
    FILE
        /usr/local/lib/python2.7/dist-packages/vyapp/plugins/main_jumps.py
    
    DESCRIPTION
        Overview
        ========
        
        This plugin implements the basic cursor movements.
        
        Usage
        =====
        
        The way to move the cursor up is by pressing <Key-k>, to move the cursor down <Key-j>,
        to move the cursor left <Key-h>, to move the cursor right <Key-l>. These events
        work in NORMAL mode.
        
        keycommands
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

***

Syntax highlight
================

### Highlighting code

The vy syntax highlight plugin works for all languages that python pygments library works for.
In order to highligh the inserted text based on the file extension, just press:

    <Escape>

### Changing syntax highlight style

The vy syntax highlight plugin uses pygments to highlight source code so it is possible to use
python pygments styles with vy. Check out python pygments syntax highlight styles.

In the vyrc file, comment the lines that import the default style and do the import of the
desired style as shown below.

~~~python
# default style.
# from vyapp.plugins.syntax.styles.vy import VyStyle
# autoload(vyapp.plugins.syntax.spider, VyStyle())

from pygments.styles.tango import TangoStyle
autoload(vyapp.plugins.syntax.spider, TangoStyle())
~~~

***

### Creating new syntax highlight styles

It is possible to implement new syntax highlight styles and do the import from the vyrc file.
As vy uses python pygments to do syntax highlight, check out creation of new styles from python
pygments.

***

Mode switch
===========

The NORMAL mode is the mode in which most editing keycommands are implemented, it is possible
to use the keycommand:

    <Escape>

when in NORMAL mode to get in another mode. It spares some keycommands when dealing with modes
that demand more than two keycommands to get in. 

Suppose that one needs to use a set of keycommands that is implemented in a mode X
whose keycommand to get in the mode X is implemented in the mode Y. Sometimes
it will be needed to use editing keycommands by switching to NORMAL mode, if it is
needed to switch back to mode X then the user will have to switch to Y then to X.
In order to spare keycommands in such a situation, it is possible to use
the keycommand:

    <Alt-Escape>

That works in GLOBAL mode, it i means regardless of the mode in which the AreaVi instance is in
then the keycommand handle will be executed. When the user is in mode X and press the keycommand above
then the current AreaVi instance mode will be yielded then whenever the user press:

    <Escape>

in NORMAL mode it will get the AreaVi instance in X mode. In order to get back
the standard behavior, just press:

    <Alt-Escape>

in NORMAL mode.

***

The PDB mode
============

The PDB mode is a mode used to debug python applications. It is possible to set breakpoints and run code step by step.
The cursor follow the program flow and breakpoints turn into shaded lines. It follows the flow even through multiple packages/modules.

### Getting ready to debug a python application

In order to use PDB mode it is needed to create areavi instances and setting them as output targets for the debugger process.
Consider the basic python application shown below.

Create the following dir:

~~~
mkdir mytest
cd mytest
~~~

Then put the two files below inside mytest folder:

~~~python
# alpha.py

def func_alpha(n):
    import beta
    return beta.func_beta(n)

func_alpha(10)
~~~

~~~python
# beta.py

def func_beta(m):
    m = m + 1
    return m

~~~

Open these two files in two tabs by pressing:

    <F8> 

in NORMAL mode. Create a vertical/horizontal area for each one of the vy tabs that were created. For such, 
switch the focus to the tab that has alpha.py then press:

    <F4> 

in NORMAL mode, it will open a vertical areavi instance.  Switch the focus to that areavi instance then 
make it an output target by pressing: 

    <Tab> 

in NORMAL mode. Switch the focus to the tab that has beta.py opened then press:

    <F4> 

to create a vertical area to set output target on by pressing:

    <Tab> 

as it was done with the tab having alpha.py.

Once the output targets were set on the areavi instances it is possible now to read the debug output
on these areavi instances. Now it is possible to send debug commands to the process and watch the flow of the program.


### Switch to PDB mode

The PDB mode is implemented in BETA mode. Once having set output targets for the debug process, it is time to set vy
on PDB mode, for such, switch to BETA mode by pressing:

    <Key-4> 

In NORMAL mode then: 

    <Key-p> 

in BETA mode.

### Start a process

Once in PDB mode it is possible to start a python process through the debugger by pressing:

    <Key-1> 

in PDB mode. It is important to notice that using this key command there is no way to pass command line arguments. Once
the process was successful started then the debugger will output information about the program flow on
the output targets that were set.

### Start a process with command line arguments

It is possible to pass command line arguments to the python application by pressing:

    <Key-2> 

in PDB mode. The arguments are split using shlex module.

### Set a break point

The line over the cursor is set as a breakpoint if the keycommand:

    <Key-b> 

is issued in PDB mode. The line will be shaded then it is possible to run other keycommands like:

    <Key-c> 

That means 'continue'.

### Set a temporary break point

In order to set a temporary breakpoint, press:

    <Key-B> 

in PDB mode, the line cursor line will be shaded and when the debugger hits that breakpoint the line will be unshaded.

### Remove a breakpoint

In order to remove a breakpoint that was set it is enough to place the cursor over the line
then press: 

    <Control-c> 

in PDB mode. The line will be unshaded.

### Clear all break points

In PDB mode it is enough to press:

    <Control-C> 

then it will clear all breakpoints, all the lines will be unshaded.

### Run code step by step

The keycommand:

    <Key-s> 

in PDB mode is used to execute code step by step. It sends a '(s)tep' to the debugger.
it basically executes the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).

### Stop at the next breakpoint

In order to stop at the next breakpoint, press:

    <Key-c> 

in PDB mode. It sends a '(c)ontinue' to the debugger process.

### Print a stack trace most recent frame at the bottom

Press the keycommand:

    <Key-w> 

in PDB mode. It will send a '(w)here' to the debugger process.

### Execute selected text in the current context

Sometimes it is interesting to execute some statements of the python program that is being debugged
in some contexts/scope, for such, select the statement text then press:

    <Key-e> 

in PDB mode. The statement text will be sent to the debugger process then will be executed.

### Evaluate selected text in the current context

Sometimes it is useful to evaluate some expressions that appear in the python program that is being debugged,
such expressions will be evaluated in the current scope of the debugger process. Select the expression text
then press:

    <Key-p> 

in PDB mode.

### Inject python code to be executed in the current context

It is very useful to change the state of variables or even redefinie functions in some scopes
when debugging an application, through this keycommand it is possible to inject python code
to be executed. For such, press:

    <Key-r> 

in PDB mode, it will appear an inputbox where to insert the statement text.

### Inject python code to be evaluated in the current context

In order to inject code to be evaluated in some contexts/scope, press:

    <Key-x> 

in PDB mode. It will open an inputbox where to type the expression text to be evaluated.

### Terminate the process

When the debugging process has finished it is possible to terminate the process by pressing:

    <Key-q> 

in PDB mode.

The IRC mode
============

Vy implements vyirc that is an irc client plugin. It is such an amazing plugin that permits easily to connect
to an irc network. It is possible to connect to more than one network, channels turn into tabs, irc servers turn into tabs as well.

### Connect to an irc network

Vyirc implements the following class constructor that is defined below:

~~~python
IrcMode(addr='irc.freenode.org', port=6667, user='vy vy vy :vyirc', nick='vyirc', 
             irccmd='PRIVMSG nickserv :identify nick_password', channels=['#vy'])
~~~

In order to connect to an irc network, switch to NORMAL mode then press:

    <Key-semicolon>

to instantiate the class described above. It would open a tab with an irc connectinon tied to it, the new tab will be in IRC mode.

If there is someone using your nick, it will be needed to send the command below to the IRC server:

~~~
NICK new_nick
~~~

For such, switch to the IRC connection tab then press:

    <Control-e> 

In IRC mode.

***

### Switch to IRC mode

After having executed the function IrcMode and opening an irc connection then it is possible
to put the areavi instance tied to the connection in IRC mode by switching the focus to that
areavi instance then switching to GAMMA mode and pressing:

    <Key-i>

When the areavi instance is in IRC mode then it is possible to use keycommands to send IRC commands
by pressing:

    <Control-e>

***

### Send IRC commands

Vy implements a keycommand to send raw irc commands to the irc server. It shows an inputbox where to type irc commands.
Switch to an irc connection tab or an irc channel tab then press:

    <Control-e> 

In IRC mode. 

***

### Identify nick

In order to identify nick once having opened an irc connection, just switch to IRC mode by pressing:

    <Control-e>

Then type:

~~~
PRIVMSG nickserv :IDENTIFY nick_password
~~~

Some irc networks uses the command below:

~~~
NickServ identify nick_password
~~~

***

### Join a channel

Press:

    <Control-e> 

In IRC mode then type:

~~~
JOIN #channel
~~~

***

### Part from a channel

Just switch to IRC mode, press:

    <Control-e>

Then type:

~~~
PART #channel
~~~

***

### Change nick

In IRC mode, press:

    <Control-e>

Then type:

~~~
NICK new_nick
~~~

### Query an user

Switch to one of the IRC network tabs then press:

    <Control-c> 

in IRC mode to type the nick of the user. 
It will create a new tab whose title is the user's nick.

***

### Set IRC network output position

The keycommand to reset the position where data coming from
the IRC network is dropped on is:

    <F1>

In IRC mode.

### Create shortcut functions for IRC networks

It is possible to create shortcut functions to connect to IRC networks by importing the IrcMode class
from your vyrc file then defining a new function that instantiates the IrcMode class with defined arguments.
The scheme is better described below.

**The vyrc file**

~~~python
# The vy irc mode.
from vyapp.plugins.vyirc import IrcMode

# Here, the network connections can be defined. 
def irc_freenode(addr='irc.freenode.org', port=6667, user='vy vy vy :vyirc', nick='vyirc', 
             irccmd='PRIVMSG nickserv :identify nick_password', channels=['#vy']):
    IrcMode(addr, port, user, nick, irccmd, channels)

def irc_arcamens(addr='irc.arcamens.com', port=6667, user='vy vy vy :vyirc', nick='vyirc', 
             irccmd='PRIVMSG nickserv :identify nick_password', channels=['#arcamens']):
    IrcMode(addr, port, user, nick, irccmd, channels)
~~~

After adding the piece of code above in your vyrc file then it is possible to instantiate new IRC connections
to irc.freenode.org by executing the function irc_freenode either from:
    
    <Control-e>

or

    <Key-semicolon>

The ibash plugin
================

The ibash plugin is a python module that permits to talk to the bash interpreter. It is possible
to execute commands through bash and start some processes like a python interpreter, maxima etc.

### First steps

The ibash plugin uses the scheme of output target. 
It is needed to set an AreaVi instance as output target to be able to read output
from commands that are sent to the bash interpreter.

First of all, pick up an AreaVi instance that you want to read output from bash commands or processes.
Once you have decided where to read output from commands, switch the focus to the AreaVi instance
then press in NORMAL mode:

    <Tab> 

After setting a set of output targets then it is possible to send
commands to the bash interpreter and read the commands output.

### Send a code line

This is the most used feature of the ibash plugin, consider it was already set an output target
and you want to send the command below to the bash interpreter:

~~~
ls -la
~~~

How would you proceed?
you would place the cursor over that line then press:

    <F1>

in NORMAL mode or in INSERT mode. When the keycommand above happens in NORMAL mode, the code line
over the cursor is sent to the bash interpreter and the cursor is placed one line down. When it happens
in INSERT mode, the code line is sent to the bash and a newline is inserted down the cursor position. It is
means that either in NORMAL mode or in INSERT mode it is possible to drop code to the bash interpreter;
Such a behavior is useful when dealing with e-scripts or when using vy as a terminal-like.

### Send a SIGINT signal

It is possible to start processes that run on top of the bash process, in such a situation it will be useful
to send unix signals to the child processes like SIGINT. For such, switch to NORMAL mode then press:

    <Control-C>

### Send a SIGQUIT signal

It is possible to send a SIGQUIT to the bash process by switching to NORMAL mode then pressing:

    <Control-backslash>

### Send code lines

Sometimes it will be useful to drop entire regions of code to the bash interpreter, for such, select
the region that needs to be sent to the bash interpreter then press the keycommand below in NORMAL mode:

    <Control-Return>

### Run a command as root

Sometimes it is interesting to run commands as root, for such it is needed to have set the 
environment variable SUDO_ASKPASS.

Check out if it is already set with:

~~~
echo $SUDO_ASKPASS
~~~

If it is not set then it is needed to check where vy askpass script is located.

~~~
whereis askpass
~~~

Issue the command below to have the SUDO_ASKPASS permanently set.

~~~
echo 'export SUDO_ASKPASS=path/askpass' >> ~/.bashrc
~~~

The path is the folder where askpass script is located. It is generally located in /usr/bin.

Now it is possible to run commands with:

~~~
sudo command
~~~

The askpass program will show up asking for the password then the command will be run as root.

### Run a bash process as root

It is useful to run a bash process as root sometimes, for such, drop the command below to the bash interpreter:

~~~
sudo bash -i
~~~

It will run a bash process with different permissions on top of the bash process.

### Starting processes

Some processes like the python interpreter when started through the ibash plugin would have
the output correctly outputed over the AreaVi instance that was set as target by passing some
special arguments. An example follows:

~~~
tee >(python -i -u)
~~~

When the python interpreter is started through tee and with -i and -u it adjusts the correct scheme of
buffering. The -i argument means that the python interpreter would run in interactive mode.

### Restart the bash process

Sometimes it is needed to restart the bash process, for such, switch to NORMAL mode then press:

    <Control-F1>

Misc
====

### Word completion

In INSERT mode it is useful to have completion of words. The word completion
searches for all possible combinations in all the opened files.

Write down a word that you know to appear in one of the opened files by vy, place
the cursor at the end of such a word then press the keycommand below in INSERT mode:

    <Control-q>

If you keep pressing it other possible combinations will appear.

***

### Copy the opened file path to the clipboard

Consider opening a file with:

~~~
vy /tmp/tmpfile
~~~

Then switch the focus to the AreaVi instance that maps to the file above and in NORMAL mode, press:

    <Key-u>

It will appear on the statusbar a msg saying the file path was copied to the clipboard.
Try pasting it somewhere.

***

### The python autocomplete plugin

Vy uses jedi python library to implement auto completion for python code. Whenever a python file
is opened in vy it turns possible to type a python object name following a period then pressing:

    <Control-period>

It will open a small window with the possible attributes of the object.

***

### Comment a block of code

There is a keycommand in ALPHA mode to comment a block of code based on the
extension of the file being edited. It will add inline comments to the selected region
of text when the keycommand below is pressed in ALPHA mode:

    <Key-e>

I use this keycommand with the keycommand to select lines in NORMAL mode.

### Uncomment a block of code

Once a block of code is commented you can uncomment it by selectiong the lines then pressing the
keycommand below in ALPHA mode:

    <Key-r>

***

The plugin API
==============

This GUIDE goes through some of the most important aspects of the plugin api and vy common features. For a better
understanding of how vy works and how to implement more sophisticated plugins it is needed to read Tkinter docs on
the Text/AreaVi widget class. 

### The vyrc, plugin system and user plugin space

The vyrc file consists of a sequence of python statements whose purpose is loading plugins and configuring preferences.
Some plugins receive arguments, these arguments modify their behavior in some aspects. An example of such a plugin is
listed below:

~~~python

# Shifting blocks of code.
import vyapp.plugins.shift
autoload(vyapp.plugins.shift, width=4, char=' ')

~~~

The statements above tell python to import the plugin vyapp.plugins.shift then pass it as argument to the autoload function.
That function is responsible by adding the vyapp.plugins.shift module to the list of modules that should be loaded whenever
an AreaVi instance is created. 

The vyapp.plugins.shift module implements keycommands to shift selected text to the left/right.

Every vy plugin has an install function that is called with an AreaVi instance whenever it is created.
The arguments passed to the function autoload will be passed to the install method defined inside the plugin module.

Let us create a real example in order to elucidade the topics so far explained.

Create a file named show_hello in your ~/.vy folder, write the following piece of code in it:

~~~python
def install(area, name):
    # The AreaVi insert method inserts text in a given index.
    area.insert('1.0', name)
~~~

Open your ~/.vy/vyrc file then add the following piece of code:

~~~python
import show_hello
autoload(show_hello, 'YOU NAME HERE')
~~~

Save the file then run vy. You will notice your name inserted in an AreaVi instance whenever one is
created. Try opening some vertical panes and tabs to test what happens.

The most important statements of the vyrc file are the following:

~~~python
##############################################################################
# User plugin space.

import sys
from os.path import expanduser, join
sys.path.append(join(expanduser('~'), '.vy'))
##############################################################################
# Functions used to load the plugins.
from vyapp.plugins import autoload, autocall

##############################################################################
~~~

The first three statements tells python to add your ~/.vy folder to the list of places in which python should look for
imports. The remaining ones just import the autoload function and autocall function to be used afterwards. The autocall
function receives as first argument a python function instead of a python module. Such a function is useful to set up
some aspects of appearence for some Tkinter widgets.

The show_hello plugin could be rewritten with autocall function. It would be enough to define the following function inside
the ~/.vyrc file:

~~~python
def show_hello(area, name):
    area.insert('1.0', name)
autocall(show_hello, 'YOUR NAME HERE')
~~~

There are some kinds of imports which don't demand the autoload function. These are statements that import
command modules/plugins. These modules define python functions that are exposed in the vyapp.plugins.ENV 
environment. This dict is used by vy as environment variable when python code is dropped. 

Example from ~/.vy/vyrc:

~~~python
# Command plugins.
# Post files quickly with codepad.
from vyapp.plugins import codepad
~~~

It is possible to drop python code to vy through the keycommand below in NORMAL mode:

    <Key-semicolon>

or by selecting a region of text that consists of python code then pressing in NORMAL mode:

    <Key-e>

An example of vy plugin that exposes functions in vyapp.plugins.ENV is shown below:

~~~python

# ~/.vy/insert_date.py

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
import time

def date():
    AreaVi.ACTIVE.insert('insert', time.strftime("%d/%m/%Y"))

ENV['date'] = date

~~~

Once the file ~/.vy/insert_date.py has been created with the code above, add the following statement to the ~/vy/.vyrc:

~~~python
import insert_date
~~~

Run vy then press the keycommand below in NORMAL mode to drop python code:
    
    <Key-semicolon>

Move the vy cursor to a position where you would like to insert current date then drop the following statement:

~~~python
date()
~~~

Now, you have created your first vy command plugin !

The vyrc file is executed using vyapp.plugins.ENV as environment, it means that whatever it is defined inside ~/.vy/vyrc
it will be defined in vyapp.plugins.ENV. It means the vy command created by the plugin above could be  defined 
inside the ~/.vy/vyrc file by defining the date function inside the ~/vy/.vyrc file although it doesn't sound good.

### A help on Tkinter events

Tkinter is an event driven based library, it means that tkinter has a mainloop that processes events then dispatch them. 
There are handles/functions that are mapped to these events, whenever an event occurs a handle is called with an object
that characterizes the event.

The kind of events that are used in most with vy are the ones that happen when a key is pressed. A set of common events
that happen when keys get pressed is shown below:

    It means that the key 'h' was pressed while the Control key is kept pressed.
    <Control-h> 

    It means that the key 'F1' was pressed.
    <F1>

    It means that the key 'h' was pressed regardless of it being released.
    <KeyPress-h>

    It means that the key 'h' was released.
    <KeyRelease-h>
    
    The return key/enter.
    <Return>

    The key '1' was pressed.
    <Key-1>

Other events that may be interesting are:

    It happens when an widget gets focus, like when you click on it with the mouse.
    <FocusIn>

    When an widget loses focus.
    <FocusOut>

    It happens when a file is loaded in a given AreaVi instance.
    <<LoadData>>

    It happens when data is saved in a given AreaVi instance.
    <<SaveData>>

These events are passed as strings to the Widget.bind method. The AreaVi class inherits such a method
but it uses another method to map events to callbacks.

### Playing with AreaVi widget

The AreaVi widget is a class that inherits from the Tkinter Text widget, it implements other methods that turn
the Text widget class more powerful. Vy is a modal editor, all the scheme of modes in vy is defined inside the AreaVi
class. 

The AreaVi class is a Tkinter widget, so whenever an event on an AreaVi instance happens Tkinter mainloop dispatches it
to the event handles. The best way to examplify what happens is with an example shown below:

~~~python
from vyapp.areavi import *

def key_pressed(event):
    print 'Some key was pressed.'


area = AreaVi('None')
area.pack(expand=True, fill=BOTH)

# It creates the INSERT mode.
area.add_mode('INSERT', opt=True)

# It changes the AreaVi instance mode to INSERT.
area.chmode('INSERT')

# It maps the handle key_pressed to the event <Key-i> when area is in INSERT mode.
area.hook('INSERT', '<Key-i>', key_pressed)

# Now try this one. The msg wouldn't be printed since the AreaVi instance is in
# INSERT mode. It would be needed to put the AreaVi instance in ALPHA mode by calling
# area.chmode('ALPHA')
area.hook('ALPHA', '<Key-j>', key_pressed)

# Switch now to ALPHA mode by calling area.chmode('ALPHA') then try pressing <Key-j>.
~~~

The example above should be run through a python interpreter in interactive mode in order to better understand what is happening
as well as testing the code with different values. 


### What is a AreaVi/Text widget index?

An index is a string of the type shown below:

    'Line.Col'

Such a string corresponds to a position of the AreaVi instance. The example below should elucidate better than
any definition. Such an example should be run through an interactive session:

~~~python
from vyapp.areavi import *
area = AreaVi('None')
area.pack(expand=True, fill=BOTH)

# Insert the text at the position 1.0, it means
# at the line 1 and col 0.
area.insert('1.0', 'THIS IS A STRING')

# Now try this one. It will insert the char '#' at line 1 and col 4.
area.insert('1.4', '#')

# This one deletes a range of text.
area.delete('1.4', '1.5')

# Try other examples.
~~~

### What are marks?

Marks are strings that corresponds to positions of the AreaVi instance. The marks can 
change its position according to text being deleted or inserted.

Consider the following example:

~~~python
from vyapp.areavi import *
area = AreaVi('None')
area.pack(expand=True, fill=BOTH)
area.insert('1.0', 'cool\n')

# Set a mark named 'm' at the position '1.2'.
area.mark_set('m', '1.2')
area.insert('1.0', 'that ')

# It will print 1.7. It means that the mark position
# has changed when the text 'that' was inserted.
# The area.index method returns the index of a given mark.
print area.index('m')
~~~

### The basic AreaVi/Text widget marks

The most basic marks are the 'insert' one which corresponds
to the position in which the cursor is in, and 'end' mark that
is used to insert text at the end of the text.

There are other important marks as 'insert lineend' that maps
the end of the cursor line, the 'insert linestart' that maps the 
beginning of the cursor line.

Example:

~~~python
# It would insert the string 'alpha' to the end of the cursor line.
area.insert('insert lineend', 'alpha')

# It would delete the entire line that is under the cursor.

area.delete('insert linestart, 'insert lineend')

# It gives the index 'Line.Col' for the end of the cursor line.
area.index('insert lineend')
~~~

There are other kind of possible marks used line. 'insert +1c' that corresponds to 1 character
after the cursor position. The example below shows better:

~~~python
# It deletes the char at the cursor position.
area.delete('insert', 'insert +1c')

# It deletes the second character ahead the cursor position.
area.delete('insert +1c', 'insert +2c')
~~~

You could use a negative index like 'insert -1c' that means one char back the cursor position.
Other possible marks are 'insert linestart +1c' that means one char after the beginning of the cursor line.

Example:

~~~python
# It deletes the first char of the cursor line.
area.delete('insert linestart', 'insert linestart +1c')
~~~

Try playing with 'insert lineend -1c' as well. It is possible to have marks relative to lines, this is very useful.
You could try the following marks 'insert +1l' and 'insert -1l' these means one line down the cursor position
and one line up the cursor position. You could even have stuff like 'insert +1l linestart +1c' that means one line
down the cursor position and one char ahead the beginning of the line down the cursor position :P

Try:

~~~python
area.delete('insert +1l linestart', 'insert +1l linestart +1c')
~~~

You could use an index instead of a mark like '4.3 +1l' as well.:

~~~python
# It would insert the char '#' at the position 3.3'.
area.insert('2.3 +1l', '#')
~~~

These examples should be played interactively. Make sure to change the cursor position
along the examples to check what happens when the statements are executed.

### What are tags?

A tag has a name and two index's, a tag is mapped to a range of text. It is possible to set some options for these ranges of text, such options
are background, color, font, font size and even to map handles to events that happen when the mouse is over them. It is even possible
to add a handle to an event that maps a key press when the cursor is in the tag range.


### The 'sel' tag and AreaVi.tag_add/AreaVi.tag_remove method

The 'sel' tag is a built-in tag that corresponds to text selection, it can be added to ranges of text when needed, the text's background
will be modified. Try the following piece of code below:

~~~python
area = AreaVi('None')
area.pack(expand=True, fill=BOTH)
area.insert('1.0', 'alpha')

# It will add the tag 'sel' from the beginning of the text to the end.
area.tag_add('sel', '1.0', 'end')

# Look at the text in the AreaVi instance now, it will be selected.
# Inserting the following statement will unslect the text/remove the tag 'sel' from the beginning to the end.
area.tag_remove('sel', '1.0', 'end')
~~~

### The AreaVi.tag_ranges method

Consider you have added a lot of tags to a lot of ranges of text, you want to know which ranges are binded to a given tag. This method
will give you the answer. See the example below that adds the 'sel' tag to three ranges then retrieves back the index's.

Example:

~~~python
area.insert('1.0', 'a' * 100) 
area.tag_add('sel', '1.0', '1.4')
area.tag_add('sel', '1.11', '1.20')
area.tag_add('sel', '1.30', '1.50')

for ind in area.tag_ranges('sel'):
    print ind

# It will print.
# 1.0
# 1.4
# 1.11
# 1.20
# 1.30
# 1.50

The items that area.tag_ranges generate are textindex objects that implement a __str__ method.
~~~

### The AreaVi.tag_config method

It is possible to specify options for tags as mentioned before, it is needed to use the AreaVi.tag_config method.
The example below examplifies:

~~~python
area.insert('1.0', 'a' * 50)
# It adds the tag 'alpha' to the range '1.0', '1.10'.
area.tag_add('alpha', '1.0', '1.10')
# It sets the background/color/font for the specified range.
area.tag_config('alpha', background='blue', foreground='green', font=('Monospace', 8, 'bold'))
~~~

### The AreaVi.search method

This method performs search on the AreaVi instance's text. It is possible to pass regex to the method and a range in which
the search should be performed.

Example:

~~~python
from Tkinter import *

area = AreaVi('None')
area.pack(expand=True, fill=BOTH)

count = IntVar()
area.insert('1.0', 'this is cool')

# It performs the search in the range '1.0', 'end'.
index = area.search('o{1,2}', '1.0', 'end', regexp=True, count=count)

print index, count.get()
# It would print.
# 1.9, 2
# The count.get() yields the length of the matched pattern.
~~~


### The AreaVi.find method

This method receives basically the same arguments that AreaVi.search. It returns an iterable object
with all the matched patterns in the given range.

Example:

~~~python
area.insert('1.0', 'o' * 3 + 'a' * 4 + 'o' * 4)
for match, pos0, pos1 in area.find('o+', '1.0', 'end', regexp=True):
    print match, pos0, pos1

# It would print what it has been matched and the range of the match.
~~~

### The AreaVi.load_data method

This method of the class AreaVi is used to dump the contents of a file into an AreaVi instance.
This method spawns a virtual event whose name is:

    <<LoadData>>

Another virtual event that is spawned is:

    <<Load-type>> 

where type is the file type that is determined by the mimetypes.guess_type method.
It is useful when needing to have handles called when a given file type is loaded.


### The AreaVi.save_data method

This method is used to dump the contents of an AreaVi instance into a file. It spawns
the virtual event below:

    <<SaveData>>

as well as the virtual event:

    <<Save-type>>

where type is is the file type determined by the function guess_type form the standard module
mimetypes.


### Vy Global Mode

The vy global mode is the '-1', such a mode dispatches events regardless of the mode in which an AreaVi instance is in.
Consider the following situation in which an AreaVi instance is in mode 'NORMAL' and the event below happens:
    
    <Key-i>

If there is a handle mapped to that event in the global mode then the handle will be called with the event object.

Like:

~~~python
def handle(event):
    pass

# It would make handle be called no matter the mode in which vy is in.
area.hook('-1', '<Key-i>', handle)
~~~



### The AreaVi.add_mode and AreaVi.chmode methods

It possible to create as many modes as one want, it is enough to call the AreaVi.add_mode method
with the name of the method and an argument named opt that tells vy about the type of the mode.

Example:

~~~python
# The opt argument being true means it is possible to insert text from the keyboard events
# in the AreaVi instance. it is like the INSERT mode but under a different name.
area.add_mode('MODE_NAME', opt=True)
# It makes the AreaVi instance switch to the a mode regardless of it having the opt
# argument set to True.
area.chmode('NEW_MODE_NAME')
~~~









