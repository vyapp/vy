"""
This file implements functions that are used by plugins 
to execute python code from vy.
"""

from traceback import print_exc as debug
import sys

def execute(handle, *args, **kwargs):
    """
    It executes handle and avoids throwing a exception but it prints the exception.

    Example:

    def func(a, b):
        return a/b

    # It wouldnt throw an exception.
    r = execute(func, 1, 0)

    # It would print None.
    print r

    """

    try:
        val = handle(*args, **kwargs)
    except Exception:
        debug()
    else:
        return val

def exec_quiet(handle, *args, **kwargs):
    """
    Like exe.execute but doesnt print the exception.
    """

    try:
        val = handle(*args, **kwargs)
    except Exception:
        pass
    else:
        return val

def exc(data, env):
    """
    This function is used to execute python code and it sets 
    the sys.stderr to sys.stdout so exceptions would be printed on sys.stdout. 
    After the code being executed then sys.stderr is restored to its 
    default value.

    The data argument is python code to be executed and env is a dictionary where
    the code will be executed.

    Note: It is mostly used to execute python code from vy.
    """

    import sys
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





