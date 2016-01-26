"""
This module implements the scheme of output target for vy. Plugins that demand writting to
sys.stdout would write to sys.stdout and have the content dispatched to a sequence of
objects that have a write method.
"""

import sys

class Stdout(object):    
    """
    This class is used to wrap an AreaVi widget to be used as stdout channel.
    """

    TAG_CODE = 'code'
    def __init__(self, area):
        # I am selecting from the beginning to the start of a line
        # below to the insert cursor so i add a line
        # to the end of the line below to the cursor then
        # the code_mark will be after the sel mark.
        # this was a pain in the ass to notice.
        self.area = area
        self.area.mark_set('code_mark', 'insert')

    def write(self, data):
        """
        This method is called to write data to the AreaVi widget.
        """

        index0 = self.area.index('code_mark')
        self.area.insert('code_mark', data)
        self.area.tag_add(self.TAG_CODE, index0, 'code_mark')
        self.area.see('insert')

    def __eq__(self, other):
        return self.area == other

class Transmitter(object):
    """
    This class would replace sys.stdout. It is used to dispatch
    data that is written to sys.stdout, the data is dispatched to its
    child objects that have a write method.
    """

    def __init__(self, default):
        self.base    = [default]
        self.default = default

    def restore(self):
        """
        It clears all children and restores the default
        child.
        """

        del self.base[:]
        self.base.append(self.default)

    def append(self, fd):
        """
        It appends a new child.
        """

        self.base.append(fd)

    def remove(self, fd):
        """
        It removes a given child.
        """

        self.base.remove(fd)

    def write(self, data):
        """
        This method is used to dispatch data to the
        children.
        """

        for ind in self.base: 
            ind.write(data)

def echo(data): 
    """
    It writes data to sys.stdout.
    """

    sys.stdout.write(data)    



