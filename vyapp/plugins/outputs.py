"""
Overview
========

This plugin implements Key-Commands to redirect the default python sys.stdout object
to an AreaVi instance. As it is possible to drop python code to vy in order
to affect the editor state, the python interpreter writes output to
sys.stdout. 

With this plugin it is possible to drop the output to a given 
Line.Col inside an AreaVi instance.

Key-Commands
============

Namespace: outputs

Mode: Global
Event: <Control-Alt-bracketleft>
Description: it restores sys.stdout.

Mode: Global
Event: <Alt-braceleft> 
Description: It removes a given AreaVi instance from 
having output written in.

Mode: Global
Event: <Alt-bracketleft>
Description: It redirects output from sys.stdout to 
a given AreaVi instance.
"""

from vyapp.app import root
import sys

class Stdout(object):    
    """
    This class is used to wrap an AreaVi widget to be 
    used as stdout channel.
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

        If it occurs an exception when writing to some
        of the supposed fd's then it is removed from    
        the list of fd's. 

        Consider the situation
        that an areavi instance is added then
        destroyed. It will throw an exception
        when writing to that areavi.
        """

        for ind in self.base[:]: 
            try:
                ind.write(data)
            except Exception:
                self.base.remove(ind)

class OutputController(object):
    sys.stdout = Transmitter(sys.__stdout__)

    def __init__(self, area):
        self.area = area
        area.install('outputs', (-1, '<Alt-bracketleft>', self.add_output),
        (-1, '<Alt-braceleft>', self.rm_output),
        (-1, '<Control-Alt-bracketleft>',  self.restore_output))
    
    def add_output(self, event):
        try:
            sys.stdout.remove(self.area)
        except ValueError:
            pass
    
        sys.stdout.append(Stdout(self.area))
        root.status.set_msg('Output set on: %s' % \
        self.area.index('insert'))
        return 'break'
    
    def rm_output(self, event):
        try:
            sys.stdout.remove(self.area)
        except Exception:
            root.status.set_msg('Output removed!')
        else:
            root.status.set_msg('Output removed!')
        return 'break'
    
    def restore_output(self, event):
        sys.stdout.restore()
        root.status.set_msg('Stdout restored!')
        return 'break'
    
install = OutputController




