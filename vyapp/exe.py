"""

"""

from traceback import print_exc as debug
import sys

def execute(handle, *args, **kwargs):
    """

    """

    try:
        val = handle(*args, **kwargs)
    except Exception:
        debug()
    else:
        return val

def burn(chain, event, opt = None):
    """

    """

    for ind in chain:
        val = execute(ind, event)

        if val == True:    opt = True
        elif val == False: opt = False

    return opt

def exec_quiet(handle, *args, **kwargs):
    """

    """

    try:
        val = handle(*args, **kwargs)
    except Exception:
        pass
    else:
        return val

def exc(data, env):
    """

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



