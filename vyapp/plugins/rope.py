"""
Overview
========


Key-Commands
============

Namespace: rope

Mode: PYTHON
Event: <Key-R>
Description: 
"""

from vyapp.ask import Ask
from rope.base.project import Project
from vyapp.tools import get_project_root, error
from vyapp.areavi import AreaVi
from rope.refactor.rename import Rename
from rope.base.libutils import path_to_resource
from vyapp.app import root

class PythonRefactor(object):
    def __init__(self, area):
        self.area    = area
        area.install('rope', ('PYTHON', '<Key-R>', error(self.rename)),)

    def update_instances(self, updates):
        """
        After changes it updates all AreaVi instances which 
        were changed.
        """
        files = AreaVi.get_opened_files(root)
        print('\nRope - Renamed resource ..\n')

        for ind in updates:
            print('File:', ind.real_path)
            instance = files.get(ind.real_path)
            if instance:
                instance.load_data(ind.real_path)

    def rename(self, event):
        tmp0    = self.area.get('1.0', 'insert')
        offset  = len(tmp0)
        ask     = Ask()
        path    = get_project_root(self.area.filename)
        project = Project(path)
        mod     = path_to_resource(project, self.area.filename)
        renamer = Rename(project, mod, offset)
        changes = renamer.get_changes(ask.data)
        project.do(changes)

        updates  = changes.get_changed_resources()
        self.update_instances(updates)
        self.area.chmode('NORMAL')
        root.status.set_msg('Resources renamed!')
        project.close()

install = PythonRefactor

