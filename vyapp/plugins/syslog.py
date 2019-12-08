"""
Overview
========

This plugin displays a Text window containing all the output of the
python interpreter underlying Vy. 

When code is run to change Vy state it may print out debugging 
information to sys.stdout. Such a data is captured
and shown on the CmdOutput window.

Key-Commands
============

Namespace: syslog
Mode: Global
Event: <Alt-q>
Description: Display sys.stdout log on window.
"""
from vyapp.widgets import TextWindow
import sys

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

class Syslog:
    def __init__(self, area):
        self.area = area
        area.install('syslog', 
        (-1, '<Alt-q>', self.view_log))

    def view_log(self, event):
        code_output.display()
        return 'break'
    
code_output = TextWindow('', title='Cmd Output')
code_output.withdraw()
sys.stdout.append(CmdOutput(code_output))
install = Syslog