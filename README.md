![vy](vy.png) vy
================

A powerful modal editor written in python.

vy is a modal editor with a very modular architecture. Everything is very minimalistic and modular. 
vy is built on top of Tkinter which is one of the most productive graphical toolkits. It permits vy
to have such a great programming interface for plugins. It is pretty straightfoward to implement a plugin for vy.

There is no need for a mouse with vy, everything is made from the keyboard. There are tons of key commands to help 
you spare a lot of time when programming or just editing some text. vy has a powerful set of key commands that
permits you to quickly switch the cursor to a given position. 

There is a simple but powerful scheme for finding patterns of text as well as replacing ranges of text with regular 
expressions. It is possible to select regions of text then perform matching operations inside such regions; 
such a feature lets you format some documents more easily with no expense of time.

The syntax highlighting plugin is very minimalistic and extremely fast. It supports syntax highlighting 
for all languages that python-pygments supports. The source code of the syntax highlighting plugin is about 
80 lines of code. It is faster than the syntax highlighting plugins of both vim and emacs. :)

The Python auto completion plugin is about 70 lines of code and it is incredibly simple to implement
auto completion for other languages.

There is a powerful SCREEN_SEARCH mode that permits making the cursor jump to positions in the visible region of the file 
that match a given pattern. Such a plugin spares a lot of time in almost all situations.

The ISEARCH mode allows a form of fuzzy search whose input is a set of words, with the effect of finding lines which contain the words in any order. 
This kind of search permits to implement e-script files with sections organized by tags.
This scheme of organization permits one to find quickly a region of the file that performs some action
when dropped to the bash interpreter through vy. It is handy when finding specific sections in documentations as well.

There are plugins for highlighting pairs of (), [], {} as well as selecting the text between these pairs 
It is very useful when playing with function definitions in some languages like LISP.

vy has a plugin that implements a mode to quickly jump backwards/forwards to a given character. It is possible
to go through some blocks of code very fast as well as quickly edit some pieces of text. Such a plugin
uses very handy keys.

It is possible to easily implement new syntax highlighting themes that work for all languages.
The syntax highlighting plugin permits you to set specific background/colour for a language tokens type.

vy is written in pure Python; it permits you to drop Python code to the interpreter that affects the editor state.
Python is such an amazing language it turns vy such a powerful application because its plugin API is high level naturally.

The set of keys used in vy was carefully chosen to be handy although it is possible to make vy look like vim or emacs since
there is a high level of modularity in vy.

There is a simple and consistent terminal-like plugin in vy. It is possible to talk to external processes through bash.
Such a feature is very handy when dealing with interpreters. One can just drop pieces of code to a given interpreter 
through bash then check the results. Another important point of such a feature consists in implementing e-scripts 
to automate tasks in UNIX-like systems. It is possible to run an SSH process on top of bash then send commands and receive 
output from vy: it lets you access files over SSH on another machine.

E-scripts are a very handy way to automate some tasks. Such tasks can be pushing stuff onto GitHub, adding users 
to a UNIX-like system, a set of steps to set up a system, adjusting the system sound volume, etc. 

vy implements a Python debugger plugin that permits debugging Python code easily and in a very cool way. 
One can set break points, remove break points, run the code then see the cursor jumping to the line 
that is being executed and much more. It is pretty straightfoward to implement debuggers for other languages.

It is possible to open multiple vertical/horizontal areas to edit different files. Such a feature makes it possible
to edit multiple files in a given tab. vy supports multiple tabs as well.

vy has a very well defined scheme for user plugins. One can easily develop a plugin then make vy load it.
There is a vyrc file written in Python that is very well documented and organized to make it simple to load
plugins and set stuff at startup. You can take the best out of vy with no need to learn some odd language
like vimscript or emacs LISP; since vy is written in Python, you use Python to develop for it.

All built-in functions are well documented, which simplifies the process of plugin development as well as personalizing stuff.
The plugins are documented: the documentation can be accessed from vy by dropping Python code to the interpreter.

The plugins implement keycommands or Python functions. The complete reference for a set of keycommands that a plugin implements 
can be accessed from a Python interpreter instance or from vy.
    
    help(vyapp.plugins.plugin_name)

One could implement as many modes as needed. This is very useful for specific situations. There could exist modes 
for ircclient, filemanagers, browsing specific type of files, generating LaTeX code, etc.

Screenshots
===========

**Tabs, panes, terminal-like, Python autocompletion**
![screenshot-1](screenshot-1.jpg)

**Dynamically extending the editor through Python**
![screenshot-2](screenshot-2.jpg)

**E-scripts**
![screenshot-3](screenshot-3.jpg)


A video
=======

https://youtu.be/0bBKOFdQKzo

Install from pip
================
    
    pip install untwisted
    pip install pygments
    pip install jedi
    pip install vy


Install from git
================

vy requires Python 2.7 to run.

This is a short script to install vy from the git repository.

    pip install pygments
    pip install jedi

    cd /tmp
    git clone https://github.com/iogf/vy.git vy-code
    git clone https://github.com/iogf/untwisted.git untwisted-code

    cd /tmp/untwisted-code
    python setup.py install
    cd /tmp/vy-code
    python setup.py install

Once you have installed vy and its dependencies,
run in a terminal the following command:

    vy file1 file2 ...

Or just:

    vy

Upgrade
=======

As vy is in development there may occur some changes to the vyrc file format, it is important to remove
your ~/.vy directory before a new installation in order to upgrade to a new version.


Documentation
=============

**The Vy Book**

[BOOK.md](BOOK.md)


Help
====

I hang out at irc.freenode.org in the channel #vy.
My nick there is Tau.

vy Facebook group:
https://www.facebook.com/groups/525968624207147/





