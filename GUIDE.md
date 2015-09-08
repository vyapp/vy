Introduction
============


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

or by selection a region of text that consists of python code then pressing in NORMAL mode.

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

A help on Tkinter events
========================

A help on the AreaVi widget
===========================

### Playing with AreaVi widget

### What are marks?

### The basic Text widget marks

### What are tags?

### The SEL tag

### The tag_add method

### The tag_remove method

### The tag_ranges method

### The AreaVi.search method

### The AreaVi.find method

### The AreaVi virtual events

### The AreaVi.load_data method

### The AreaVi.save_data method

The vy scheme
=============

### Vy Mode System

### Vy Global Mode

### A simple plugin example

### The creation of new modes

### How to switch to a mode

### The sys.stdout object

### The CompleteWindow class

Complete Examples
=================

### A Word Checker plugin

### Count Phrase Words plugin

### The AreaVi.ACTIVE attribute

### A simple email sender plugin



