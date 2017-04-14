"""
Overview
========

This module implements commands to save file and load files into AreaVi instances.

Commands
========

Command: ss(filename)
Description: It dumps the AreaVi command target's content into a file whose name is
specified.
filename = The name of the file.

Command: lo(filename)
Description: Load the contents of filename into the AreaVi command target.
"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.app import root

ENV['s'] = lambda : AreaVi.ACTIVE.save_data()
ENV['q'] = lambda : root.quit()
ENV['ss'] = lambda filename: AreaVi.ACTIVE.save_data_as(filename)
ENV['lo'] = lambda filename: AreaVi.ACTIVE.load_data(filename)
ENV['to'] = lambda filename: root.note.load([ [filename] ])
ENV['vsplit'] = lambda : AreaVi.ACTIVE.master.master.master.create()
ENV['hsplit'] = lambda : AreaVi.ACTIVE.master.master.create()


        






