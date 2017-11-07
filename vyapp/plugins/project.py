"""
Overview
========


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
                return path
            
class Project(object):
    SENTINELS = ['.git', '.svn', '.hg', '._']

    def  __init__(self, area):
        self.area  = area
        area.install('fstmt', 
        (-1, '<<LoadData>>', self.auto),
        (-1, '<Key-X>', self.manual),
        (-1, '<<SaveData>>', self.auto))

    def auto(self, event):
        """    
        Set the project root automatically.
        """

        self.area.project = get_sentinel_file(
            self.area.filename, *Project.SENTINELS)

    def manual(self, event):
        """    
        Set the project root manually.
        """

        root.status.set_msg('Set project root!')
        ask       = Ask(self.area.filename)
        self.area.project = ask.data

install = Project



