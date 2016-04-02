![vy](vy.png) vy
================

A powerful modal editor written in python.

vy is a modal editor with a very modular architecture. Everything is very minimalistic and modular. 
vy is built on top of Tkinter which is one of the most productive graphical toolkits; It permits vy
to have such a great programming interface for plugins. Python is such an amazing language;
it turns vy such a powerful application because its plugin API is high level naturally.

In vy it is easy to create modes like it is in emacs, modes that support programming languages, 
provide all kind of functionalities that varies from accessing irc or email checking.

There is no need for a mouse with vy, everything is made from the keyboard. There are tons of key commands to help 
you spare a lot of time when programming or just editing some text. vy has a handy set of key commands that
permits you to quickly switch the cursor to a given position. 

There is a smart feature that permits making the cursor jump to positions in the visible region of the file 
that match a given pattern. Such a plugin spares a lot of time in almost all situations.

vy has a plugin that implements a mode to quickly jump backwards/forwards to a given character. It is possible
to go through some blocks of code very fast as well as quickly edit some pieces of text. 

The set of keys used in vy was carefully chosen to be handy although it is possible to make vy look like vim or emacs since
there is a high level of modularity in vy.

There are key commands for highlighting pairs of (), [], {} as well as selecting the text between these pairs. 
It is very useful when playing with function definitions in some languages like LISP. There are
key commands to make the cursor jump words backwards/forwards, selecting a word, selecting a line, selecting
all text, everything that vim does and a lot more but with a better scheme of keys.

There is a powerful scheme for finding patterns of text as well as replacing ranges of text with regular 
expressions. It is possible to select regions of text then perform matching operations inside such regions; 
Such a feature lets you format some documents more easily with no expense of time.

There are ways to perform fuzzy searches whose input is a set of words, with the effect of finding lines which contain the words in any order;
Such a feature turns it simple browsing documentation of functions/commands as well as finding specific sections in large files.

The syntax highlighting plugin is very minimalistic and extremely fast. It supports syntax highlighting 
for all languages that python-pygments supports. The source code of the syntax highlighting plugin is about 
120 lines of code. It is faster than the syntax highlighting plugins of both vim and emacs. :)
It is possible to easily implement new syntax highlighting themes that work for all languages because it uses
python pygments styles scheme.

There is a simple and consistent terminal-like plugin in vy that turns it possible to talk to external processes.
Such a feature is very handy when dealing with interpreters. One can just drop pieces of code to an interpreter
then check the results. It is possible to run an SSH process then send commands and receive 
output from vy: it lets you access files over SSH on another machine.

The features of talking to proccesses and vy powerful fuzzy search schemes it makes vy a perfect tool to deal with
E-scripts. E-scripts are a very handy way to automate some tasks. Such tasks can be pushing stuff onto GitHub, adding users 
to a UNIX-like system, a set of steps to set up a system, etc. 

vy implements a Python debugger plugin and auto completion that permits debugging Python code easily and in a very cool way. 
One can set break points, remove break points, run the code then see the cursor jumping to the line 
that is being executed and much more.

It is possible to open multiple vertical/horizontal panes to edit different files. Such a feature makes it possible
to edit multiple files in a given tab. vy supports multiple tabs as well with a handy scheme of keys
to switch focus between tabs and panes. 

vy has a very well defined scheme for user plugins. One can easily develop a plugin then make vy load it.
There is a vyrc file written in Python that is very well documented and organized to make it simple to load
plugins and set stuff at startup. You can take the best out of vy with no need to learn some odd language
like vimscript or emacs LISP; since vy is written in Python, you use Python to develop for it.

All built-in functions are well documented, which simplifies the process of plugin development as well as personalizing stuff.
The plugins are documented: the documentation can be accessed from vy by dropping Python code to the interpreter.

The plugins implement keycommands or Python functions. The complete reference for a set of key commands that a plugin implements 
can be accessed from a Python interpreter instance or from vy.
    
    help(vyapp.plugins.plugin_name)


Screenshots
===========

**Tabs, panes, terminal-like, Python autocompletion**
![screenshot-1](screenshot-1.jpg)

**Dynamically extending the editor through Python**
![screenshot-2](screenshot-2.jpg)


A video
=======

https://youtu.be/0bBKOFdQKzo

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

The vy Book
===========

[BOOK.md](BOOK.md)


Help
====

I hang out at irc.freenode.org in the channel #vy.
My nick there is Tau.

Facebook group:
https://www.facebook.com/groups/525968624207147/












