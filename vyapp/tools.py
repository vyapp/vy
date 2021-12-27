"""
This module implements a set of functions that are commonly used by plugins.
"""

from traceback import print_exc as debug
from os.path import exists, dirname, join
from vyapp.app import root
from vyapp.areavi import AreaVi
from os.path import abspath
import sys

    
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


