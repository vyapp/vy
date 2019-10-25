"""
Overview
========

Integrates with python rope refactoring tools. It allows users
to rename variables, methods, classes, modules and also move python resources
easily.

Key-Commands
============

Namespace: rope

Mode: PYTHON
Event: <Key-R>
Description: Rename a given python resource. Place the cursor
over the resource string on the AreaVi instance then issue  the keycommand 
to perform the renaming along the whole project. 
"""

from vyapp.ask import Ask
from rope.base.project import Project
from vyapp.tools import get_project_root, error
from vyapp.areavi import AreaVi
from rope.refactor.rename import Rename
from rope.base.libutils import path_to_resource
from rope.base.change import MoveResource
from vyapp.app import root
from rope.base import libutils
from rope.refactor.move import create_move

class PythonRefactor(object):
    def __init__(self, area):
        self.area  = area
        self.files = None
        area.install('rope', ('PYTHON', '<Key-R>', error(self.get_rename_data)),
        ('PYTHON', '<Key-A>', self.static_analysis),
        ('PYTHON', '<Key-M>', error(self.get_move_data)))

    def get_root_path(self):
        if self.area.project:
            return self.area.project
        return get_project_root(self.area.filename)

    def static_analysis(self, event):
        path    = self.get_root_path()
        project = Project(path)
        mod     = path_to_resource(project, self.area.filename)

        libutils.analyze_module(project, mod)
        project.close()

    def get_move_data(self, event):
        ask = Ask()
        if ask.data:
            self.move(ask.data)

    def move(self, name):
        """
        """
        tmp0    = self.area.get('1.0', 'insert')
        offset  = len(tmp0)

        path    = self.get_root_path()
        project = Project(path)

        project = Project(path)
        mod     = path_to_resource(project, self.area.filename)
        mover   = create_move(project, mod, offset)
        destin  = path_to_resource(project, name)
        changes = mover.get_changes(destin)
        project.do(changes)

        self.update_instances(changes)
        project.close()

        self.area.chmode('NORMAL')
        root.status.set_msg('Resources moved!')

        
    def update_instances(self, changes):
        """
        After changes it updates all AreaVi instances which 
        were changed.
        """

        # Avoid having to calculate it multiple times.
        self.files = AreaVi.get_opened_files(root)
        for ind in changes.changes:
            if isinstance(ind, (MoveResource,)):
                self.on_move_resource(ind)
            else:
                self.on_general_case(ind)

    def on_general_case(self, change):
        """
        Should be called when self.files is updated.
        """

        for ind in change.get_changed_resources():
           instance = self.files.get(ind.real_path)
           if instance:
               instance.load_data(ind.real_path)
   
    def on_move_resource(self, change):
        """
        Should be called when self.files is updated.
        """
        old, new = change.get_changed_resources()
        instance = self.files.get(old.real_path)

        # When the file is not updated then no need to load it.
        if instance:
            instance.load_data(new.real_path)

    def get_rename_data(self, event):
        ask = Ask()
        if ask.data:
            self.rename(ask.data)

    def rename(self, name):
        tmp0    = self.area.get('1.0', 'insert')
        offset  = len(tmp0)
        path    = self.get_root_path()
        project = Project(path)
        mod     = path_to_resource(project, self.area.filename)
        renamer = Rename(project, mod, offset)
        changes = renamer.get_changes(name)
        project.do(changes)

        self.update_instances(changes)

        print('\nRope - Renamed resource ..\n')
        print(changes.get_description())
        self.area.chmode('NORMAL')
        root.status.set_msg('Resources renamed!')
        project.close()

install = PythonRefactor

