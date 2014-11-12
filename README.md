vy
==

A vim-like in python made from scratch.

What is vy? 
It is an attempt of mine(Tau a.k.a Iury) to implement a vim-like editor in python.
I feel as i'm close to this goal since i have been using vy for all kind of tasks 
that i used vim in the past.

Why would one implement a vim-like in python? 
Well, python is such a powerful language, i used vim for years when i noticed vimscript wasn't
really cool and i couldn't use vim python plugin api in the way i would like.

Does vy mimic vim?
No, it is slightly similar, it has a standard mode, an insert mode and
some of the key-commands perform similar operations in vy and vim.

Vy supports an interesting feature, it is the capacity of talking to external processes
It is all thanks to untwisted although it could be done with any other library that supports a reactor
with a update function. The main idea behind to talking to external processes is the concept of e-scripts.

E-scripts are an interesting way of programming repeatitive tasks. The first time i had contact
with this abstraction was with one of my university teachers. It is worth reading about. He has
implemented eev that is a set of emacs keys to perform cool tasks as well as send stuff to external
processes. Consequently it turns easy the task of creating e-scripts to automatize repetitive tasks.

You can read more about e-scripts and eev in.

http://angg.twu.net/eev-intros/

The person who implemented eev implements e-scripts in a nice way, you can go
through some of the examples and learn a bit of how implementing e-scripts.


Install
=======
This is a short script to install the latest version of vy.

    cd /tmp
    git clone git@github.com:iogf/vy.git vy-code
    git clone git@github.com:iogf/untwisted.git untwisted-code 

    su
    cd /tmp/untwisted-code
    python setup.py install
    cd /tmp/vy-code
    python setup.py install

    apt-get install python-tk
    apt-get install pygments
    exit

    
Once you have installed vy and its dependencies.
Run on a terminal the following command.

    vy file1 file2 ...

Or just.

    vy


Usage
=====

Take a look at the file INTRO.md for a description of the basic
commands.


Videos
======

**Using pdb with vy:**
https://www.youtube.com/watch?v=Ahachd4_N9U

**Running python code on the fly:**
https://www.youtube.com/watch?v=Rav3iz-VCN0
    
**Formating text with vy:**
https://www.youtube.com/watch?v=5JUnUCl-E1w



Features
========
* A simple api once it is purely written in python
* Syntax highlight for all kind of langues supported by python-pygments.
* A very powerful api since it written in python
* Execute python code on the fly that affects the behavior of the editor.
* Talk to external processes like interpreters
* A powerful search scheme that permits formating text with regex and python code


Help
====
I hang out at irc.freenode.org in the channel #vy.
My nick there is Tau.

