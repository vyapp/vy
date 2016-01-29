"""
Overview
========

This module implements commands to save file and load files into AreaVi instances.

Usage
=====

It is needed to set a target for command in order to use the functions that are
implemented in this module.

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

ENV['ss'] = lambda filename: AreaVi.ACTIVE.save_data_as(filename)
ENV['lo'] = lambda filename: AreaVi.ACTIVE.load_data(filename)


