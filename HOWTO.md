Introduction
============

In this HOWTO i'll follow some test cases to show all vy features and functionalities. 
I find it very useful to learn stuff from examples. The test cases varies from creating 
simple plain text files to sending stuff to the bash interpreter.

Create a file
=============

First of all, run vy by typing in a terminal.

    vy

It will launch vy interface. It will be initially in NORMAL mode. There is a statusbar 
field named Mode: in which the AreaVi instance that has the focus is in.


In order to insert chars it is needed to switch to INSERT mode. Make sure there is focus 
on the AreaVi/Text widget instance. Then press

    <Key-i>

It will make the focused AreaVi instance change its mode to INSERT mode. Once in INSERT mode 
it is possible to insert chars in the AreaVi instance.

Type the following piece of text in it.

    The universe is a bag of dices. 
    God just plays the dices continously.
    All kind of combinations happens infinitely.

Now, switch back to NORMAL mode by pressing.

    <Escape>

In order to save the contents of the AreaVi instance, press

    <Shift-s>    

It will show a save dialog window. Save this file as 
    
    universe-secret

Now you have edited your first file with vy !


Open a file from an open dialog window
=====================================

First run vy, make sure the AreaVi instance in which you want to load the contents 
of the file is focused. then press

    <Control-d>

in NORMAL mode. It will show an open dialog window. Pick up the file created 
in the previous section.

    universe-secret

After pressing 'open', it will load the

    universe-secret

file contents in the focused AreaVi instance.


Save the contents of an opened file
===================================

There is a handy way to save the contents of a file that was opened 
then edited. Let us edit our 

    universe-secret

file. Run vy then press

    <Control-d>

in NORMAL mode. Pick up the file. Then press

    <Key-i>

in NORMAL mode to switch to INSERT mode. Then insert the following 
text in the end of the file.

    God may not play dices.

Switch back to NORMAL mode by pressing.

    <Escape>

Now, press

    <Control-s>

in NORMAL mode. If the folder has permissions for writting then will 
appear a msg on the statusbar "Data Saved".

Moving the cursor around
========================

This the most important aspect of a modal editor, the cursor movements.
It is what turns modal editors very handy.

First open our file

    universe-secret

by pressing 

    <Control-d>

in NORMAL mode.

Then try pressing 

it will move the cursor left.
    <Key-h>

it will move the cursor down.
    <Key-j>

It will move the cursor up.
    <Key-k>

It will move the cursor right.
    <Key-l>

Try getting familiar with these Key-Commands. There will not last
much until you get used to these Key-Commands.

Move cursor to the beginning/end of a line
==========================================

Sometimes when editing a line, we notice we want to edit the beginning or 
the end of the line being edited. 

That is when we need two special Key-Commands. These two Key-commands make 
the cursor jump to the beginning or to the end of the cursor line.
The cursor line is the line whose cursor is placed on.

Open a file with some lines, place the cursor in the middle of a line.
Switch to NORMAL mode then press.

    <Key-p>

It will make the cursor jump to the end of the cursor line. So, you can switch to INSERT mode
or other suitable mode in order to perform the desired editting.

Try again switching to NORMAL mode then pressing

    <Key-o>

It will make the cursor jump to the beginning of the cursor line. It will spare you a lot 
of time.

Move cursor to the beginning/end of an AreaVi instance
======================================================

Open a file then place the cursor in the middle of the AreaVi instance.
Switch NORMAL mode then press 

Move the cursor to the beginning of the file.

    <Key-1>

Move the cursor to the end of the file.

    <Key-2>


Move a word left/right
======================

Sometimes it is useful to make the cursor jump back/next to the previous/next word.
Open a text file then switch to NORMAL mode.

Once in NORMAL mode, then press.

    <Key-bracketright>

That is ']'.

To jump to the previous word from the cursor position, switch to NORMAL mode then press

    <Key-braceright>

That is '}' or 

    <Shift-bracketright>

It is possible to select a word when the cursor is on by pressing


    <Key-bracketleft>

That is '['. This is very handy sometimes.

Paste text from the clipboard
=============================

It is one of the most important things an editor has to do. 
Select some text from the browser/other editor then copy it to the clipboard.

Then open vy, give the focus to an AreaVi instance, place the cursor
at the position that you want to paste the text then press.

    <Key-r>

In NORMAL mode. Such a Key-Command is meant to paste text from the clipboard one line down.

The Key-Command

    <Key-t>

in NORMAL mode is meant to paste text to the end of the cursor line.

The Key-command

    <Key-e>

in NORMAL mode is meant to paste text one line up from the cursor line.

Try these commands until getting comfortable !


Copy text to the clipboard
==========================

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












