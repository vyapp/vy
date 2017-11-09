"""
Overview
========

Plugins that rely on the attribute project of AreaVi instances
should use AreaVi.HOME as last resource of information.
"""

from vyapp.areavi import AreaVi
from vyapp.app import root
from vyapp.ask import Ask

class Home(object):
    def  __init__(self, area):
        self.area = area
        area.install('fstmt', 
        ('NORMAL', '<Key-X>', self.set_home))

    def set_home(self, event):
        """    
        Set the AreaVi home dir.
        """

        root.status.set_msg('Set home dir!')
        ask         = Ask(self.area.filename)
        AreaVi.HOME = ask.data

install = Home

