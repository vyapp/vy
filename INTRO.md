
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


**Obs: This remains implementing docs for other key commands. These are the basic ones. **


