
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
to insert data in the AreaVi instance. In order to switch to INSERT mode from NORMAL mode you press 

    <Key-i>.

The statusbar field Mode shows in which mode vy is in. Once you change to INSERT mode by pressing <Key-i> in NORMAL mode
it would appear on the status bar field Mode: INSERT. You can switch back to NORMAL mode by pressing 

    <Escape>.



Before dropping python commands to vy it is needed to set where the output should be printed. For such you need
to use the key <Tab> in NORMAL mode. Place the cursor in the AreaVi instance that you want to drop the output of the python commands
at the line.row then press <Tab> in NORMAL mode. It will show on the status bar that the output was redirected to that position.

After redirecting the output, you're done, just press <Key-semicolon> then type help(vyapp.plugins.plugin_name) it will
appear wherever you have set the output the plugin help.


Let us try with the most important plugin that is move_cursor.
Pick up the position in which you want the help to appear inside the active text area
with 

    <Tab> 

in NORMAL mode then type <Key-semicolon>

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

Now let us inspect other important plugin. Type 
    <Key-semicolon> 

in NORMAL mode then type 
    vyapp.plugins.io


Help on module vyapp.plugins.io in vyapp.plugins:

NAME
    vyapp.plugins.io

FILE
    /usr/local/lib/python2.7/dist-packages/vyapp/plugins/io.py

DESCRIPTION
    Overview
    ========
    
    This plugin implements basic Key-Commands to open/save files.
    
    Usage
    =====
    
    It is possible to pops a file window selection to load the contents of a file
    in a given AreaVi instance by pressing <Control-d>.
    
    After some changes to a opened file it is possible to save the contents of the file
    by pressing <Control-s> in NORMAL mode.
    
    The way to save the contents of an AreaVi instance as a different filename is by
    pressing <Shift-S> in NORMAL mode. It will open a file save dialog to pick up a name.
    
    Sometimes it is handy to just save and quit, for such just press <Control-Escape> in NORMAL mode.
    You can just quit without saving by pressing <Shift-Escape> in NORMAL mode as well.
    
    There is a Key-Command to clean all the text from a given active AreaVi instance. For such
    type <Key-D> in NORMAL mode.
    
    Key-Commands
    ============
    
    Mode: NORMAL
    Event: <Control-d>
    Description: It pops a file selection window to load the contents of a file.
    
    Mode: NORMAL
    Event: <Control-s>
    Description: It saves the content of the AreaVi instance into the opened file.
    
    Mode: NORMAL
    Event: <Shift-S>
    Description: It pops a save file dialog to save the contents of the active AreaVi
    instance with a different filename.
    
    Mode: NORMAL
    Event: <Key-D>
    Description: Clear all text of the active AreaVi instance.
    
    Mode: NORMAL
    Event: <Control-Escape>
    Description: Save and quit.
    
    Mode: NORMAL
    Event: <Shift-Escape>
    Description: Quit.

FUNCTIONS
    install(area)
    
    load(area)
        It pops a askopenfilename to find a file to drop
        the contents in the focused text area.
    
    save(area)
        It just saves the text area contents into the    
        actual opened file.
    
    save_as(area)
        It pops a asksaveasfilename window to save the contents of
        the text area.
    
    save_quit(area)
        It saves the contents of the text area then quits.

DATA
    ABORT = 'abort'
    ABORTRETRYIGNORE = 'abortretryignore'
    CANCEL = 'cancel'
    ERROR = 'error'
    IGNORE = 'ignore'
    INFO = 'info'
    NO = 'no'
    OK = 'ok'
    OKCANCEL = 'okcancel'
    QUESTION = 'question'
    RETRY = 'retry'
    RETRYCANCEL = 'retrycancel'
    WARNING = 'warning'
    YES = 'yes'
    YESNO = 'yesno'
    YESNOCANCEL = 'yesnocancel'
    root = <vyapp.app.App instance>











