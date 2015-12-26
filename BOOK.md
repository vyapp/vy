Table of Contents
=================

  * [Introduction](#introduction)
  * [What is a modal editor?](#what-is-a-modal-editor)
  * [What is a Key-Command?](#what-is-a-key-command)
  * [Running vy](#running-vy)
  * [The statusbar](#the-statusbar)
  * [Basic Modes](#basic-modes)
  * [The basic cases](#the-basic-cases)
      * [The basic cursor movements](#the-basic-cursor-movements)
      * [Open a file](#open-a-file)
      * [Save file changes](#save-file-changes)
      * [Save as dialog window](#save-as-dialog-window)
      * [Open a file from command line](#open-a-file-from-command-line)
      * [Move cursor to the beginning of the line](#move-cursor-to-the-beginning-of-the-line)
      * [Move cursor to the end of the line](#move-cursor-to-the-end-of-the-line)
      * [Move cursor to the beginning of the file](#move-cursor-to-the-beginning-of-the-file)
      * [Move cursor to the end of the file](#move-cursor-to-the-end-of-the-file)
      * [Move forward one word](#move-forward-one-word)
      * [Move backward one word](#move-backward-one-word)
      * [Search forward for ( ) { } [ ] : .](#search-forward-for--------)
      * [Search backward for ( ) { } [ ] : .](#search-backward-for--------)
      * [JUMP_NEXT mode](#jump_next-mode)
      * [JUMP_BACK mode](#jump_back-mode)
      * [Scroll one line up](#scroll-one-line-up)
      * [Scroll one line down](#scroll-one-line-down)
      * [Scroll one page up](#scroll-one-page-up)
      * [Scroll one page down](#scroll-one-page-down)
      * [Insert a blank line up](#insert-a-blank-line-up)
      * [Insert a blank line down](#insert-a-blank-line-down)
      * [Toggle line selection](#toggle-line-selection)
      * [Select a word](#select-a-word)
      * [Select text between pairs () {} []](#select-text-between-pairs---)
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
      * [Highlight pairs of () [] {}](#highlight-pairs-of---)
      * [The ALPHA mode](#the-alpha-mode)
      * [Shade a line](#shade-a-line)
      * [Jump to the previous shaded line](#jump-to-the-previous-shaded-line)
      * [Jump to the next shaded line](#jump-to-the-next-shaded-line)
      * [Comment a block of code](#comment-a-block-of-code)
      * [Uncomment a block of code](#uncomment-a-block-of-code)
      * [Undo](#undo)
      * [Redo](#redo)
      * [Jump to a given Line.Col position](#jump-to-a-given-linecol-position)
      * [The SCREEN_SEARCH mode](#the-screen_search-mode)
      * [Set a search pattern](#set-a-search-pattern)
      * [Set a replacement pattern](#set-a-replacement-pattern)
      * [Search up](#search-up)
      * [Search down](#search-down)
      * [Unshade matched patterns](#unshade-matched-patterns)
      * [Replace up](#replace-up)
      * [Replace down](#replace-down)
      * [Replace on](#replace-on)
      * [Search selected text](#search-selected-text)
      * [Replace pattern inside selected text](#replace-pattern-inside-selected-text)
      * [Word completion](#word-completion)
      * [Opening files in panes/tabs from command line](#opening-files-in-panestabs-from-command-line)
      * [Syntax highlight](#syntax-highlight)
      * [Copy the opened file path to the clipboard](#copy-the-opened-file-path-to-the-clipboard)
      * [Execute Inline Python](#execute-inline-python)
      * [Getting help](#getting-help)
      * [Set an AreaVi instance as target for commands](#set-an-areavi-instance-as-target-for-commands)
      * [Execute selected regions of python code](#execute-selected-regions-of-python-code)
      * [The global mode](#the-global-mode)
      * [Move focus one tab left](#move-focus-one-tab-left)
      * [Move focus one tab right](#move-focus-one-tab-right)
      * [Move focus one pane up](#move-focus-one-pane-up)
      * [Move focus one pane down](#move-focus-one-pane-down)
      * [Move focus one pane up](#move-focus-one-pane-up-1)
      * [The BETA mode](#the-beta-mode)
      * [The python autocomplete plugin](#the-python-autocomplete-plugin)
  * [The vyrc file](#the-vyrc-file)
  * [The basic functions](#the-basic-functions)
  * [Using vy as a terminal](#using-vy-as-a-terminal)
  * [E-scripts](#e-scripts)
  * [The plugin API](#the-plugin-api)
      * [The vyrc, plugin system and user plugin space](#the-vyrc-plugin-system-and-user-plugin-space)
      * [A help on Tkinter events](#a-help-on-tkinter-events)
      * [Playing with AreaVi widget](#playing-with-areavi-widget)
      * [What is a AreaVi/Text widget index?](#what-is-a-areavitext-widget-index)
      * [What are marks?](#what-are-marks)
      * [The basic AreaVi/Text widget marks](#the-basic-areavitext-widget-marks)
      * [What are tags?](#what-are-tags)
      * [The 'sel' tag and AreaVi.tag_add/AreaVi.tag_remove method](#the-sel-tag-and-areavitag_addareavitag_remove-method)
      * [The AreaVi.tag_ranges method](#the-areavitag_ranges-method)
      * [The AreaVi.tag_config method](#the-areavitag_config-method)
      * [The AreaVi.search method](#the-areavisearch-method)
      * [The AreaVi.find method](#the-areavifind-method)
      * [The AreaVi virtual events](#the-areavi-virtual-events)
      * [The AreaVi.load_data method](#the-areaviload_data-method)
      * [The AreaVi.save_data method](#the-areavisave_data-method)
      * [Vy Global Mode](#vy-global-mode)
      * [The AreaVi.add_mode and AreaVi.chmode methods](#the-areaviadd_mode-and-areavichmode-methods)
      * [The sys.stdout object](#the-sysstdout-object)
      * [The CompleteWindow class](#the-completewindow-class)
      * [A simple plugin](#a-simple-plugin)
      * [A Word Checker plugin](#a-word-checker-plugin)
      * [Count Phrase Words plugin](#count-phrase-words-plugin)
      * [The AreaVi.ACTIVE attribute](#the-areaviactive-attribute)
      * [A simple email sender plugin](#a-simple-email-sender-plugin)


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

This book goes through all standard cases of using vy as an editor/ide. I'll describe some possible
scenaries in which the Key-Commands are useful as well as explain step by step how to use the Key-Commands.

What is a modal editor?
======================

A modal editor is an editor that can be in different states. It performs different operations/tasks/actions
from each state it is in. When vy is NORMAL mode and you type 

    <Key-j> 

it will make the cursor jump one line down. When it is in INSERT mode and you type 

    <Key-j> 

it will merely insert the character 'j' at the cursor position.

Vy differently from vim can have as many modes as it is needed. It means you can implement new modes
that perform all kind of actions/operations.

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

Consider the following Key-Command below.

    <Control-h>

In order to execute the code mapped to that event one would keep the key Control pressed
then press the key 'h'.

Consider now.

    <Control-H>

What does it mean? It means that to get the handle mapped to that event one would keep the key control pressed
as well as the Shift key then press the key 'h'.

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


The basic cases
===============

### The basic cursor movements

You can save a lot of time by using some movement commands. These are the basic commands to learn.
Run vy, it will be in NORMAL mode. 

Press the Key-Command below to switch to INSERT mode.

    <Key-i> 

Insert some text in the AreaVi then switch back to NORMAL mode by pressing 

    <Escape>

Now that you have got some text then you can play with the Key-Commands to move the cursor.

Move the cursor left by pressing.
    
    <Key-h>

Move the cursor right by pressing.

    <Key-l>


Move the cursor up by pressing.

    <Key-k>

Moving the cursor down by pressing.

    <Key-j>

Practice these Key-Commands until you get used to them.

***

### Open a file

There is a way to open a file dialog window to pick a file. For such switch to NORMAL
by pressing. 

    <Escape>

Then press.

    <Control-d>

It will open a file dialog window in which you can select a file to be opened.

***

### Save file changes

There is a handy Key-Command to save file changes. Open a file, switch to INSERT
mode by pressing.

    <Key-i>

Insert some lines. Switch to NORMAL mode by pressing.

    <Escape>

Then press.

    <Control-s>

In case of failure or success a msg would appear on the statusbar.

***

### Save as dialog window

It is possible to save a file with a new name by opening a save as dialog window.
Switch to NORMAL mode then press

    <Shift-s>

### Open a file from command line

Pass the filenames to vy as arguments on the command line.

    vy file1 file2 file3 file4 ...

It would open four tabs.

***

### Move cursor to the beginning of the line

Suppose you are editing the end a line then you decide you need to edit the beginning of the line.
You could spend some time by moving it character by character but that doesn't sound cool. 

Switch to NORMAL mode then press.

    <Key-p>

***

### Move cursor to the end of the line

Suppose now you are editing the end of the line then you decide to edit the beginning of the line. 

Switch to NORMAL mode then press.

    <Key-o>

***

### Move cursor to the beginning of the file

This Key-Command spares a lot of time. Imagine as painful it would be moving the cursor
character by character until the beginning of a big file when you were editting the end of it.

Switch to NORMAL mode then press.

    <Key-1>

It will make the cursor jump to the beginning of the file.

***

### Move cursor to the end of the file

As there is a Key-Command to move the cursor to the beginning of a file there should exist one
to move the cursor to the end of a file as well. For such, switch to NORMAL mode then press.

    <Key-2>

***

### Move forward one word

You can save a lot of time by using this Key-Command correctly. Sometimes it is faster
to move the cursor foward some words than using other means. Switch to NORMAL mode
then press.

    <Key-bracketright>

That will place the cursor on the first char of the next word.

***

### Move backward one word

Suppose you have finished writting a phrase then you notice that one of the previous words of the
phrase has a typo. What do you do? Well, you switch to NORMAL mode then press.

    <Key-braceright>

It will place the cursor on the first char of the previous word.
    
***

### Search forward for ( ) { } [ ] : .

I use this Key-Command to spare time when looking for typos in programming files 
or jumping quickly through blocks of code in java/c.

Switch to NORMAL mode then press.

    <Key-P>

It will put the cursor on the next occurrence of one of the

    () {} [] : .

***

### Search backward for ( ) { } [ ] : .

This Key-Command is used more than its friend, i use it whenever i'm finishing to write
some statement then i notice i made a typo in the middle of the line.

Switch to NORMAL mode then press.

    <Key-O>

That would put the cursor on the previous occurrence of the symbols.


***

### JUMP_NEXT mode

There are circumstance that some Key-Commands wouldn't work well to place the cursor
at the desired position. This mode will solve the problem. 

When vy is in JUMP_NEXT mode and you press some key then the cursor will be placed on the 
next char that corresponds such a key.

Turn the NORMAL mode on, then press.

    <Key-v>

It will appear JUMP_NEXT in the statusbar mode field. 

Press some key that maps to a printable character that is ahead of the cursor position 
then the cursor will jump to the corresponding char.

***

### JUMP_BACK mode

This mode performs the opposite of the JUMP_NEXT, it places the cursor on the previous occurrence
of a char. 

Switch to NORMAL mode then press.

    <Key-c>

Vy will be in JUMP_BACK mode. Press some key that maps to a printable char then
the cursor will jump to the previous occurrence of the char.

***

### Scroll one line up

The Key-Command to scroll one line up is implemented in NORMAL mode. Open a file with
some pages then press.

    <Key-w>

It will scroll one line up. The cursor wouldn't change its position as long it remains
visible.

***

### Scroll one line down

This Key-Command is implemented in NORMAL mode as the one to scroll one line up.
Open a file with a considerable number of pages then press.

    <Key-s>

The cursor would remain at its position as long it stays visible.    

***

### Scroll one page up

This Key-Command works in NORMAL mode, open a file with some pages then press the Key-Command below
to make the cursor jump to the end of the file.

    <Key-2>

Then press.

    <Key-q>

***

### Scroll one page down

In NORMAL mode, open some big file then try pressing.

    <Key-a>

***

### Insert a blank line up

This command works in NORMAL mode, it inserts a blank line above the cursor position
then puts vy in INSERT mode. 

Put the cursor over a non blank line then press.

    <Key-n>

***

### Insert a blank line down

As the Key-Command to insert a blank line up, this one works in NORMAL mode. 
Put the cursor over a line then press.

    <Key-m>

It will insert a blank line below the cursor line then put vy in INSERT mode.

***

### Toggle line selection

Sometimes one is interested to copy just the line which the cursor is on. This Key-Command
selects the line.

Switch to NORMAL mode then put the cursor over a line then press.

    <Key-f>

If you press the same keystroke then the line will be unselected.

***

### Select a word

It is possible to select a word when the cursor is on by pressing


    <Key-bracketleft>

That is '['. This is very handy sometimes.

***

### Select text between pairs () {} []

I used this Key-Command a lot when i was playing with scheme. It selects
the text between matching pairs of the symbols below.

    () {} []

Place the cursor on one of the symbols above, considering it is a matching pair, then 
press.

    <Key-slash>

***

### Drop a range selection mark

A range selection mark is a mark in the text to be used to add selection up/down/right/left.
In order to drop a range selection mark, switch to NORMAL mode then press.

    <Control-v>

It will appear a msg on the statusbar saying that mark selection was dropped at the cursor
position. The Key-Commands to add selection up/down/left/right use this mark as a reference.

***

### Add/remove range selection one line up

Once a range selection mark was dropped, press the below Key-Command in NORMAL mode.

    <Control-k>

It will select/unselect one line up from the range selection mark position.

***

### Add/remove range selection one line down

There is a Key-Command to add/remove range selection one line down, such a Key-Command works in NORMAL mode as well.
Drop a selection range mark then press.

    <Control-j>

That will add/remove range selection one line down from the range selection mark position.

***

### Add/remove range selection one char left

The Key-Command below add/remove selection from the range selection mark.

    <Control-h>

***

### Add/remove range selection one char right

The Key-Command below add/remove selection from the range selection mark position.

    <Control-l>

***

### Drop a block selection mark

Block selection works with a mark as range selection does. In order to drop a block selection
mark, switch to NORMAL mode then press.

    <Control-V>

It will appear a msg on the statusbar saying that a block selection mark was dropped at the cursor position.

***

### Add/remove block selection one line up

Once a block selection mark was dropped, press the Key-Command below in NORMAL mode to add/remove block selection one line up.

    <Control-K>

***

### Add/remove block selection one line down

Switch to NORMAL mode then press.

    <Control-J>

You need to have first dropped a block selection mark.

***

### Add/remove block selection one char left

This command works as well in NORMAL mode, supposing you have dropped a block selection mark.

Press.

    <Control-H>
***

### Add/remove block selection one char right

Make sure you have dropped a block selection mark then press.

    <Control-L>

### Paste text one line up

Switch to NORMAL mode, place the cursor on a line then press.

    <Key-f>

to select the line, then copy the line with.

    <Key-y>

Place the cursor over some other line then press.

    <Key-e>

That will paste the copied text at the beginning of the line above the cursor.

***

### Paste text one line down

Switch to NORMAL mode, place the cursor in the middle of a line then press.

    <Control-P>

The above Key-Command will select a range of the line from the cursor position 
to the end of the line.

Then copy the selected text by pressing.

    <Key-y>

Now that there is text in the clipboard, press.

    <Key-r>

It will paste the selected range of the line at the beginning of the next line.

***

### Paste text in the cursor position

Switch to NORMAL mode, place the cursor in the middle of a line then press the below command 
to copy a range of text from the cursor position to the end of line.

    <Control-o>

Press the Key-Command below to copy the selected text to the clipboard.

    <Key-y>

Then move the cursor to a given position then press.

    <Key-t>

It will paste the copied text in the cursor position.

***

### Copy selected text

The Key-Command to copy text to the clipboard is

    <Key-y>

in NORMAL mode. In order to have text copied to the clipboard it is needed
to select some text. You can do it in so many different ways with vy.

Open a file then switch to NORMAL mode. Place the cursor over a line
then press the key below to select the entire line.

    <Key-f>

Then press.

    <Key-y>

The line will be copied to the clipboard.

***

### Delete selected text

There is a Key-Command that deletes all selected text. Switch to NORMAL mode,
place the cursor over a line then press the Key-Command below to select the line.

    <Key-f>

Move the cursor around then select some other lines.
Now, press.

    <Key-d>

You will notice all the selected text was deleted.

***

### Delete a char

I don't use this command very much but its useful sometimes.
Switch to NORMAL mode, then place the cursor over a character.

Now, try to press a few times the command.

    <Key-z>

***

### Delete a line

I use this one a lot. Switch to NORMAL mode then place the cursor on a line, then press.

    <Key-x>

It will delete the line.

***

### Delete a word

There is not a specific command to delete a word although it is achievable
by selecting the word in which the cursor is placed on. For such press.

    <Key-bracketleft>

in NORMAL mode then press.

    <Key-d>

It will delete the selected text that is a word.

***

### Highlight pairs of () [] {}

Vy will highlight pairs of () [] {} whenever the cursor is placed on
one of these chars.

***

### The ALPHA mode

The ALPHA mode implements some Key-Commands that aren't very often used.
Switch to NORMAL mode then press.

    <Key-3>

It will appear in the statusbar mode field that vy is in ALPHA mode.
You can switch back to NORMAL mode by pressing.

    <Escape>

This mode implements Key-Commands to comment/uncomment blocks of code, drop marks at
specific positions, shade lines and a few other features.

***

### Shade a line

Sometimes we need to create marks to remember text positions. The way to create a mark
in vy is by shading a line. Switch to NORMAL mode, then place the cursor on the desired line
and press key below to switch to ALPHA mode.

    <Key-3>

Once in ALPHA mode, press.

    <Key-q>

It will shade the line, in order to unshade just press again the same Key-Comamnd.

***

### Jump to the previous shaded line

This is useful to remember positions of the text. Switch to ALPHA mode by pressing

    <Key-3>

then press

    <Key-a>

It will make the cursor jump to the previous shaded line.

***

### Jump to the next shaded line

This makes the cursor jump to the next shaded line. Switch to ALPHA mode
then shade a line that is in the middle of the file, then switch back to NORMAL mode.

Press

    <Key-1>

to make the cursor jump to the beginning of the file. Now, switch back to ALPHA mode
then press

    <Key-s>

It will make the cursor jump to the next shaded line.

***

### Comment a block of code

There is a Key-Command in ALPHA mode to comment a block of code based on the
extension of the file being edited. It will add inline comments to the selected region
of text when the Key-Command below is pressed in ALPHA mode.

    <Key-e>

I use this Key-Command with the Key-Command to select lines in NORMAL mode.

### Uncomment a block of code

Once a block of code is commented you can uncomment it by selectiong the lines then pressing the
Key-Command below in ALPHA mode.

    <Control-r>

This Key-Command is specially useful when you want to rewrite some blocks of code without
deleting what you have written.

***

### Undo 

After some Key-Command is performed you can undo the text changes by pressing in NORMAL mode the 
Key-Command below.

    <Key-comma>


***

### Redo

Consider the situation that you have performed some Key-Commands then decided to undo the
text operations but you notice you just were mistaken when undoing the text operations. What would you do?
Well, i would press in NORMAL mode the following Key-Command below.

    <Key-period>

***

### Jump to a given Line.Col position

Switch to NORMAL mode, then press

    <F3>

It will appear an input text widget in which you can insert the desired position
to place the cursor on. Try inserting the following values

    3

    4 

    4.2

    2.3

In a file with more than 5 lines.

***

### The SCREEN_SEARCH mode

This is an awesome mode in which one can do searches through the visible region of the document. It does searches
from the beginning of the visible region of the document until the end of the visible region.
The regex pattern of the search consists of.

    sequence_of_char_1(.+)sequence_of_char_2(.+)sequence_of_char_3(.+) ...

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
What do you do? Well, you could jump to the line index 8 then go word by word. But you would spare some time. The 
best way to place the cursor over the word 'alsooo' is using the SCREEN_SEARCH mode. You first press the Key-Command
below in NORMAL mode to switch to SCREEN_SEARCH mode.

    <Key-backslash>


Now, every keystroke will become part of a pattern search. Try typping the sequence
    
    in als

It will place the cursor at the beginning of the word 'alsooo' :)
You can make the cursor jump to the next possible match by pressing in SCREEN_SEARCH mode 

    <Tab>

If you want to go back to the previous match

    <Control-Tab>

If you think you typed wrong pattern you can delete a char from it with

    <BackSpace>

You can switch back to NORMAL mode by pressing

    <Escape>

The cursor will remain at the end of the match position.

***

### Set a search pattern

Vy uses tcl regex scheme, you can insert a regex pattern to be used later by switching to NORMAL mode
then pressing.

    <Control-q>

It will open an input text field in which you can insert a regex then press

    <Return>

to set it.

***

### Set a replacement pattern

After setting a pattern for search you can set a string to replace the occurrence of the search pattern.
You achieve it by switching to NORMAL mode then pressing.

    <Control-Q>

Insert the replacement then press

    <Return>

***

### Search up

Once a search pattern is set, it is possible to make the cursor jump to the previous occurence of the pattern
from the cursor position by pressing.

    <Control-Up>

In NORMAL mode.


***

### Search down

Switch to NORMAL mode then set a search pattern.
Press.

    <Control-Down>

It will make the cursor jump to the next occurrence of the pattern.

***

### Unshade matched patterns

After a pattern is matched it gets shaded, in order to unshade them, press.

    <Key-Q>

In NORMAL mode.

***

### Replace up

Once a replacement text was set, press the Key-Command below in NORMAL mode to replace all occurrences
of the search pattern found up.

    <Shift-Up>

***

### Replace down

Set a replacement and a search pattern, then press the Key-Command below in NORMAL mode.

    <Shift-Down>

That will replace all occurrences of the pattern down the cursor position.

***

### Replace on

Set a pattern and a replacement for the pattern. Make the cursor jump back/next to the pattern. 
Once the cursor is positioned at the pattern then press the Key-Command below in NORMAL mode.

    <Control-Right>

The matched pattern will be replaced for the previously set replacement. This Key-Command is
specially useful when one doesn't know which matched pattern should be replaced really.

***

### Search selected text

This is a Key-Command that is powerful. One could select ranges of text then do
searches inside these ranges. The matched patterns will be highlighed.

First, use range selection or block selection or whatever other kind of selection to select some
region. Then switch to NORMAL mode.

Press.

    <Control-Left>

The matched patterns will be highlighed.

***

### Replace pattern inside selected text

Once a pattern is set, a replacement is set, then one can do replacement for the matched patterns
inside a selected region by pressing the Key-Command below in NORMAL mode.

    <Shift-Right>

***

### Word completion

In INSERT momde it is useful to have completion of words. The word completion
searches for all possible combinations in all the opened files.

Write down a word that you know to appear in one of the opened files by vy, place
the cursor at the end of such a word then press the Key-Command below in INSERT mode.

    <Control-q>

If you keep pressing it other possible combinations will appear.


***


### Opening files in panes/tabs from command line

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
   

***

### Syntax highlight

The vy syntax highlight plugin works for all languages that python pygments library works for.
In order to highligh the inserted text based on the file extension, just press.

    <Escape>

***

### Copy the opened file path to the clipboard

Sometimes this command is useful, switch to ALPHA mode then press.

    <Key-u>

It will appear on the statusbar a msg saying the file path was copied to the clipboard.
Try pasting it somewhere.

***

### Execute Inline Python

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


***

### Getting help 

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

***

### Set an AreaVi instance as target for commands


***

### Execute selected regions of python code


***


### The global mode

The global mode is a mode that if there is a handle/function mapped to an event in such a mode
then such a handle will be called no matter in which mode is in.

### Move focus one tab left

***

### Move focus one tab right

***

### Move focus one pane up

***

### Move focus one pane down

***

### Move focus one pane up

***

### The BETA mode

***

### The python autocomplete plugin

***

The vyrc file
=============

The basic functions
===================

Using vy as a terminal
======================

E-scripts
=========

The plugin API
==============

This GUIDE goes through some of the most important aspects of the plugin api and vy common features. For a better
understanding of how vy works and how to implement more sophisticated plugins it is needed to read Tkinter docs on
the Text/AreaVi widget class. 

### The vyrc, plugin system and user plugin space

The vyrc file consists of a sequence of python statements whose purpose is loading plugins and configuring preferences.
Some plugins receive arguments, these arguments modify their behavior in some aspects. An example of such a plugin is
listed below.

~~~python

# Shifting blocks of code.
import vyapp.plugins.shift
autoload(vyapp.plugins.shift, width=4, char=' ')

~~~

The statements above tell python to import the plugin vyapp.plugins.shift then pass it as argument to the autoload function.
That function is responsible by adding the vyapp.plugins.shift module to the list of modules that should be loaded whenever
an AreaVi instance is created. 

The vyapp.plugins.shift module implements Key-Commands to shift selected text to the left/right.

Every vy plugin has an install function that is called with an AreaVi instance whenever it is created.
The arguments passed to the function autoload will be passed to the install method defined inside the plugin module.

Let us create a real example in order to elucidade the topics so far explained.

Create a file named show_hello in your ~/.vy folder, write the following piece of code in it.

~~~python

def install(area, name):
    # The AreaVi insert method inserts text in a given index.
    area.insert('1.0', name)

~~~

Open your ~/.vy/vyrc file then add the following piece of code.

~~~python

import show_hello
autoload(show_hello, 'YOU NAME HERE')

~~~

Save the file then run vy. You will notice your name inserted in an AreaVi instance whenever one is
created. Try opening some vertical panes and tabs to test what happens.

The most important statements of the vyrc file are the following.

~~~python

import sys
from os.path import expanduser
sys.path.append('%s/.vy/' % expanduser('~'))
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
the ~/.vyrc file.

~~~python

def show_hello(area, name):
    area.insert('1.0', name)
autocall(show_hello, 'YOUR NAME HERE')

~~~

There are some kinds of imports which don't demand the autoload function. These are statements that import
command modules/plugins. These modules define python functions that are exposed in the vyapp.plugins.ENV 
environment. This dict is used by vy as environment variable when python code is dropped. 
variable.

~~~python

# Command plugins.
# Post files quickly with codepad.
from vyapp.plugins import codepad

~~~

It is possible to drop python code to vy through the Key-Command below in NORMAL mode.

    <Key-semicolon>

or by selecting a region of text that consists of python code then pressing in NORMAL mode.

    <Key-e>


An example of vy plugin that exposes functions in vyapp.plugins.ENV is shown below.

~~~python

# ~/.vy/insert_date.py

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
import time

def date():
    AreaVi.ACTIVE.insert('insert', time.strftime("%d/%m/%Y"))

ENV['date'] = date

~~~

Add the followin statement to the ~/vy/.vyrc once the file ~/.vy/insert_date.py has been created with the code above .

~~~python

import insert_date

~~~

Run vy then press the Key-Command below in NORMAL mode to drop python code.
    
    <Key-semicolon>

Move the vy cursor to a position where you would like to insert current date then drop the following statement.

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
that happen when keys get pressed is shown below.

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

Other events that may be interesting are.

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
to the event handles. The best way to examplify what happens is with an example shown below.

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

An index is a string of the type shown below.

    'Line.Col'

Such a string corresponds to a position of the AreaVi instance. The example below should elucidate better than
any definition. Such an example should be run through an interactive session.

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

Consider the following example.

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

~~~python

# It would insert the string 'alpha' to the end of the cursor line.
area.insert('insert lineend', 'alpha')

# It would delete the entire line that is under the cursor.

area.delete('insert linestart, 'insert lineend')

# It gives the index 'Line.Col' for the end of the cursor line.

area.index('insert lineend')

~~~

There are other kind of possible marks used line. 'insert +1c' that corresponds to 1 character
after the cursor position. The example below show better.

~~~python

# It deletes the char at the cursor position.
area.delete('insert', 'insert +1c')

# It deletes the second character ahead the cursor position.
area.delete('insert +1c', 'insert +2c')

~~~

You could use a negative index like 'insert -1c' that means one char back the cursor position.
Other possible marks are 'insert linestart +1c' that means one char after the beginning of the cursor line.

~~~python

# It deletes the first char of the cursor line.
area.delete('insert linestart', 'insert linestart +1c')

~~~

Try playing with 'insert lineend -1c' as well. It is possible to have marks relative to lines, this is very useful.
You could try the following marks 'insert +1l' and 'insert -1l' these means one line down the cursor position
and one line up the cursor position. You could even have stuff like 'insert +1l linestart +1c' that means one line
down the cursor position and one char ahead the beginning of the line down the cursor position :P

~~~python

area.delete('insert +1l linestart', 'insert +1l linestart +1c')

~~~

You could use an index instead of a mark like '4.3 +1l' as well.

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
will be modified. Try the following piece of code below.

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
The example below examplifies.

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

~~~python

area.insert('1.0', 'o' * 3 + 'a' * 4 + 'o' * 4)
for match, pos0, pos1 in area.find('o+', '1.0', 'end', regexp=True):
    print match, pos0, pos1

# It would print what it has been matched and the range of the match.

~~~

### The AreaVi virtual events

### The AreaVi.load_data method

### The AreaVi.save_data method

### Vy Global Mode

The vy global mode is the '-1', such a mode dispatches events regardless of the mode in which an AreaVi instance is in.
Consider the following situation in which an AreaVi instance is in mode 'NORMAL' and the event below happens.
    
    <Key-i>

If there is a handle mapped to that event in the global mode then the handle will be called with the event object.

~~~python

def handle(event):
    pass

# It would make handle be called no matter the mode in which vy is in.
area.hook('-1', '<Key-i>', handle)

~~~



### The AreaVi.add_mode and AreaVi.chmode methods

It possible to create as many modes as one want, it is enough to call the AreaVi.add_mode method
with the name of the method and an argument named opt that tells vy about the type of the mode.

~~~python

# The opt argument being true means it is possible to insert text from the keyboard events
# in the AreaVi instance. it is like the INSERT mode but under a different name.
area.add_mode('MODE_NAME', opt=True)
# It makes the AreaVi instance switch to the a mode regardless of it having the opt
# argument set to True.
area.chmode('NEW_MODE_NAME')

~~~

### The sys.stdout object

### The CompleteWindow class

### A simple plugin

### A Word Checker plugin

### Count Phrase Words plugin

### The AreaVi.ACTIVE attribute

### A simple email sender plugin









