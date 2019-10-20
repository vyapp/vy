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
from vyapp.widgets import TextWindow
import sys

class Stdout:    
    """
    This class is used to wrap an AreaVi widget to be 
    used as stdout channel.
    """

    def __init__(self, area):
        self.area = area
        self.area.mark_set('(CODE_MARK)', 'insert')

    def write(self, data):
        """
        This method is called to write data to the AreaVi widget.
        """

        index0 = self.area.index('(CODE_MARK)')
        self.area.insert('(CODE_MARK)', data)
        self.area.see('insert')

    def __eq__(self, other):
        return self.area == other

class Transmitter:
    """
    This class would replace sys.stdout. It is used to dispatch
    data that is written to sys.stdout, the data is dispatched to its
    child objects that have a write method.
    """

    def __init__(self, default):
        self.base    = [default]
        self.default = default

    def flush(self):
        pass

    def restore(self):
        """
        It clears all children and restores the default
        child.
        """
        self.base.clear()
        self.base.append(self.default)

    def append(self, fd):
        try:
            self.base.remove(fd)
        except ValueError:
            pass
        finally:
            self.base.append(fd)

    def discard(self, fd):
        try:
            self.base.remove(fd)
        except ValueError:
            pass

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
                self.base.discard(ind)


class CmdOutput:    
    """
    """

    def __init__(self, win):
        self.win = win

    def write(self, data):
        self.win.text.insert('end', data)
        self.win.text.see('end')

    def __eq__(self, other):
        return self.win.text == other

class OutputController:
    def __init__(self, area):
        self.area = area
    
        area.install('outputs', (-1, '<Alt-bracketleft>', self.add_output),
        (-1, '<Alt-braceleft>', self.rm_output),
        (-1, '<Alt-bracketright>', self.view_log),
        (-1, '<Control-Alt-bracketleft>',  self.restore_output))
    
    def view_log(self, event):
        code_output.display()
        return 'break'

    def add_output(self, event):
        sys.stdout.append(Stdout(self.area))
        root.status.set_msg('Output set on: %s' % self.area.index('insert'))
        return 'break'
    
    def rm_output(self, event):
        sys.stdout.discard(self.area)
        root.status.set_msg('Output removed!')
        return 'break'
    
    def restore_output(self, event):
        sys.stdout.restore()
        root.status.set_msg('Stdout restored!')
        return 'break'

sys.stdout  = Transmitter(sys.__stdout__)
code_output = TextWindow('', title='Cmd Output')
code_output.withdraw()
sys.stdout.append(CmdOutput(code_output))
install = OutputController

