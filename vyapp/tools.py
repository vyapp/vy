"""
This module implements a set of functions that are commonly used by plugins.
"""

from vyapp.app import root
from vyapp.areavi import AreaVi
from os.path import abspath
import sys


def get_area_tab_index(area):
    """
    This function returns the tab index that area is
    attached to.
    """

    return area.master.master.master

def set_line(area, line, col=0):
    """
    This function receives an AreaVi widget instance and a line number
    then sets the focus to the AreaVi widget and the cursor at line.
    """

    sys.stderr.write(area.filename + '\n')
    root.note.select(get_area_tab_index(area))
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

