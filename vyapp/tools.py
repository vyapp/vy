"""
This module implements a set of functions that are commonly used by plugins.
"""

from traceback import print_exc as debug
from os.path import exists, dirname, join
from vyapp.app import root
from vyapp.areavi import AreaVi
from os.path import abspath
import sys

    
def set_line(area, line, col=0):
    """
    This function receives an AreaVi widget instance and a line number
    then sets the focus to the AreaVi widget and the cursor at line.
    """

    sys.stderr.write(area.filename + '\n')
    root.note.select(area.master.master.master)
    area.focus()
    area.setcur(line, col)

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
        set_line(area, line)

def match_sub_pattern(pattern, lst):
    # pattern = buffer(pattern)
    for indi in lst:
        for indj in range(0, len(pattern)):
                if indi.startswith(pattern[indj:]):
                    yield indi, indj
                    

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

