"""
This module implements a set of functions that are commonly used by plugins.
"""

from traceback import print_exc as debug
from os.path import exists, dirname, join
from vyapp.app import root
from vyapp.areavi import AreaVi
from os.path import abspath
import sys

    
def findline(filename, line, col=0):
    files    = AreaVi.get_opened_files(root)
    filename = abspath(filename)

    try:
        area = files[filename]
    except KeyError:
        area = root.note.open(filename)
    else:
        pass
    finally:
        root.note.set_line(area, line)

def error(handle):
    def shell(*args, **kwargs):
        try:
            return handle(*args, **kwargs)
        except Exception as e:
            root.status.set_msg('Error :%s' % e)
            raise
    return shell

def get_project_root(path):
    """
    Return the project root or the file path.
    """

    # In case it receives '/file'
    # and there is '/__init__.py' file.
    if path == dirname(path):
        return path

    while True:
        tmp = dirname(path)
        if not exists(join(tmp, '__init__.py')):
            return path
        path = tmp


def exec_quiet(handle, *args, **kwargs):
    """
    """

    try:
        val = handle(*args, **kwargs)
    except Exception:
        pass
    else:
        return val

def exec_pipe(data, env):
    """
    This function is used to execute python code and it sets 
    the sys.stderr to sys.stdout so exceptions would be printed on sys.stdout. 
    After the code being executed then sys.stderr is restored to its 
    default value.

    The data argument is python code to be executed and env is a dictionary where
    the code will be executed.

    Note: It is mostly used to execute python code from vy.
    """

    # It has to be set before because
    # if some data code catches an exception
    # then prints use print_exc it will go to
    # sys.__stderr__.

    tmp        = sys.stderr
    sys.stderr = sys.stdout

    try:
    
        exec(data, env)
    except Exception:
        debug()
    finally:
        sys.stderr = tmp


def e_stop(handle):
    """
    This decorator is used to execute an event handle
    and stop propagation of the event through event classes.

    Let us say there is a handle on:

        <Key-u>

    Such an event is on mode -1, if there is a handle on the same
    event on mode NORMAL then both handles would be executed in case
    an exception occurs in the -1 handle. 

    It happens because the 'break' value is not propagated to the tkinter event loop.
    """

    def wrapper(*args, **kwargs):
       try:
           handle(*args, **kwargs)
       except Exception:
            debug()
       return 'break'
    return wrapper

def consume_iter(iterator, time=1):
    """
    This function receives an iterator that is consumed from tkinter update
    function. It is a way to have python code executed asynchronously.  Some
    plugins would perform heavy operations that could block tkinter mainloop,
    these plugins should write code that can be executed asynchronously using  
    iterators.

    Note: Some plugins like syntax highlighting would use this technique
    to highlight code. 
    """

    def cave():
        from vyapp.app import root
        try:
            next(iterator)
        except Exception:
            pass
        else:    
            root.after(time, cave)

    cave()


