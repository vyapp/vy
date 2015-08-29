
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


The basic two modes of vy are NORMAL and INSERT. The normal mode is in which vy starts. The INSERT mode is used
to insert data in the AreaVi instance. In order to switch to INSERT mode from NORMAL mode you press <Key-i>.

The statusbar field Mode shows in which mode vy is in. Once you change to INSERT mode by pressing <Key-i> in NORMAL mode
it would appear on the status bar field Mode: INSERT. You can switch back to NORMAL mode by pressing <Escape>.


The most useful Key-Command to learn is the <Key-semicolon> in NORMAL mode or ';'. With such a Key-Command you can
drop python code to vy, then execute cool stuff like getting help from the plugins.
After pressing <key-semicolon> in NORMAL mode, it will appear an input area where you can insert python code.

Before dropping python commands to vy it is needed to set where the output should be printed. For such you need
to use the key <Tab> in NORMAL mode. Place the cursor in the AreaVi instance that you want to drop the output of the python commands
at the line.row then press <Tab> in NORMAL mode. It will show on the status bar that the output was redirected to that position.

After redirecting the output, you're done, just press <Key-semicolon> then type help(vyapp.plugins.plugin_name) it will
appear wherever you have set the output the plugin help.


Let us try with the most important plugin that is move_cursor.
Pick up the position in which you want the help to appear inside the active text area
with <Tab> in NORMAL mode then type <Key-semicolon>

    help(vyapp.plugins.move_cursor)


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





