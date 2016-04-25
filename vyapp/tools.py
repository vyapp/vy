"""
This module implements a set of functions that are commonly used by plugins.
"""

from vyapp.app import root
from vyapp.areavi import AreaVi


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

    from vyapp.app import root
    import sys
    sys.stderr.write(area.filename + '\n')
    root.note.select(get_area_tab_index(area))
    area.focus()
    area.setcur(line)

def set_status_msg(msg):
    """
    It sets the statusbar msg.
    """

    from vyapp.app import root
    root.status.set_msg(msg)

def set_status_line(line):
    """
    It sets the statusbar line field.
    """

    from vyapp.app import root
    root.status.set_line(line)

def set_status_col(col):
    """
    It sets the statusbar col field.
    """

    from vyapp.app import root
    root.status.set_column(col)

def set_status_mode(mode):
    """
    It sets the statusbar mode field.
    """

    from vyapp.app import root
    root.status.set_mode(mode)

def match_sub_pattern(pattern, lst):
    pattern = buffer(pattern)
    for indi in lst:
        for indj in xrange(0, len(pattern)):
                if indi.startswith(pattern[indj:]):
                    yield indi, indj
                    


