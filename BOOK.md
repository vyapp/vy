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




























