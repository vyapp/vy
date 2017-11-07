"""
Overview
========

This plugin attempt to set the actual project attribute
for the current AreaVi instance. It tries to find
project folders like .git, .svn, .hg or a ._ that's
a vy project file.

"""

from os.path import exists, dirname, join
from vyapp.app import root
from vyapp.ask import Ask

def get_sentinel_file(path, *args):
    """
    """

    tmp = path
    while True:
        tmp = dirname(tmp)
        for ind in args:
            if exists(join(tmp, ind)):
                return tmp
            elif tmp == dirname(tmp):
                return ''
            
class Project(object):
    SENTINELS = ['.git', '.svn', '.hg', '._']

    def  __init__(self, area):
        self.area  = area
        area.install('fstmt', 
        (-1, '<<LoadData>>', self.auto),
        (-1, '<<SaveData>>', self.auto))

    def auto(self, event):
        """    
        Set the project root automatically.
        """

        self.area.project = get_sentinel_file(
        self.area.filename, *Project.SENTINELS)

install = Project





