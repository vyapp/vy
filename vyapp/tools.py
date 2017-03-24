"""
This module implements a set of functions that are commonly used by plugins.
"""

from vyapp.app import root
import sys


def get_area_tab_index(area):
    """
    This function returns the tab index that area is
    attached to.
    """

    return area.master.master.master

def set_line(area, line):
    """
    This function receives an AreaVi widget instance and a line number
    then sets the focus to the AreaVi widget and the cursor at line.
    """

    sys.stderr.write(area.filename + '\n')
    root.note.select(get_area_tab_index(area))
    area.focus()
    area.setcur(line)

    root.status.set_msg(msg)

def match_sub_pattern(pattern, lst):
    pattern = buffer(pattern)
    for indi in lst:
        for indj in xrange(0, len(pattern)):
                if indi.startswith(pattern[indj:]):
                    yield indi, indj
                    






