"""
Overview
========

This module implements functions to adjust AreaVi widget encoding.


Commands
========

Command: charset(name)
Description: Set the default encoding to save files.
name = The name of the encoding.

Command: decode(name)
Description: Adjust an AreaVi widget text encoding.
name = The name of the encoding.
"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.app import root

def decode(name):
    try:
        AreaVi.ACTIVE.decode(name)
    except UnicodeDecodeError:
        root.status.set_msg('Failed! Charset %s' % name)
    
def charset(name):
    AreaVi.ACTIVE.charset = name
    root.status.set_msg('Charset %s set.' % name)

ENV['decode']  = decode
ENV['charset'] = charset




