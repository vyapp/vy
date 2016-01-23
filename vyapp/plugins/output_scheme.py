"""
Overview
========

This plugin implements Key-Commands to redirect the default python sys.stdout object
to an AreaVi instance. As it is possible to drop python code to vy in order
to affect the editor state, the python interpreter writes output to
sys.stdout. 

With this plugin it is possible to drop the output to a given 
Line.Col inside an AreaVi instance.

Usage
=====

It is possible to implement python functions to perform specific tasks then expose
these functions to be used when editing files.

Some functions may need to print stuff, this stuff will go to sys.stdout. Using
the Key-Command <Tab> in NORMAL mode it is possible to have sys.stdout redirected
to the given Line.Col.

This kind of mechanism is the kind of stuff that demands a nice example in order
to be fully explained.

Run vy from the terminal with.

    vy

then press <Tab> in NORMAL mode.

You will notice a msg on the status bar like.

    'Output redirected to 1.0'

That means whenever output is going to be written to sys.stdout it will be written
to the AreaVi instance in which you have set as sys.stdout.

Now, type <Key-semicolon> in NORMAL mode it will shows an input text field
in which you can insert python code to be executed.

Insert the following python code.

    for ind in xrange(3): print 'Number %s' % ind

then press <Enter>. The piece of code will be executed and the output will be appended
where the code mark was set.

You will end up with something like.

|none|
------------------------------
|Number 1                    |
|Number 2                    |
|Number 3                    |
|                            |
|                            |
|                            |
|                            |
------------------------------

Suppose you no more want to drop output from sys.stdout to an AreaVi instance 
then you can restore sys.stdout by pressing <Control-Tab> in NORMAL mode.
It will restore sys.stdout to the initial object.

Consider now that you want to delete all the output that was dropped in the
AreaVi instance without having to select all these contents.
For such, just switch to NORMAL mode then press <Control-W>.

Consider that you're generating some special kind of output from some python script,
then you just want to make vy forget about the output that was dropped until a given
moment then you press <Key-W>. So, if you press <Control-W> afterwards
it will not delete the dropped output.

It is possible to make output be dropped in more than one AreaVi instance.

Try the following, open vy, press <F4> in NORMAL mode, then press <Tab>
in the new pane, then press <F9> in NORMAL mode to make the cursor go left
to the previous pane, again press <Tab> in NORMAL mode.

Now, type <Key-semicolon> then insert 
    
    print 'VY'

It will print that msg on the two AreaVi instances.

|none|
------------------------------
|VY           |VY            |
|             |              |
|             |              |
|             |              |
|             |              |
|             |              |
|             |              |
------------------------------


In order to remove a given AreaVi instance from the list of AreaVi instances
that receive output from sys.stdout, switch to NORMAL mode then press <Control-w>.


Key-Commands
============

Mode: NORMAL
Event: <Control-W>
Description: Delete all the output dropped on an AreaVi instance.

Mode: NORMAL
Event: <Control-Tab>
Description: it restores sys.stdout.

Mode: NORMAL
Event: <Control-w> 
Description: It removes a given AreaVi instance from having output written in.

Mode: NORMAL
Event: <Tab>
Description: It redirects output from sys.stdout to a given AreaVi instance.
"""

from traceback import format_exc as debug
from vyapp.stdout import Stdout
from vyapp.tools import set_status_msg
from vyapp.exe import exec_quiet
from vyapp.ask import *
import sys

def redirect_stdout(area):
    try:
        sys.stdout.remove(area)
    except ValueError:
        pass
    sys.stdout.append(Stdout(area))
    set_status_msg('Output redirected to %s' % area.index('insert'))

def install(area):
    area.install(('NORMAL', '<Control-W>', lambda event: event.widget.delete_ranges(Stdout.TAG_CODE)),
           ('NORMAL', '<Control-Tab>', lambda event: sys.stdout.restore()),
           ('NORMAL', '<Key-W>', lambda event: event.widget.tag_delete(Stdout.TAG_CODE)),
           ('NORMAL', '<Control-w>', lambda event: exec_quiet(sys.stdout.remove, event.widget)),
           ('NORMAL', '<Tab>', lambda event: redirect_stdout(event.widget)))


