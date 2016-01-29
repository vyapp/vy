"""
Overview
========

This module implements functions to adjust AreaVi widget encoding.

Usage
=====

The function below defines the encoding to save files:

    charset(name)

The function:

    decode(name)

is used to adjust the encoding of the AreaVi widget text.

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
from vyapp.tools import set_status_msg

def decode(name):
    try:
        AreaVi.ACTIVE.decode(name)
    except UnicodeDecodeError:
        set_status_msg('Failed! Charset %s' % name)
    
def charset(name):
    AreaVi.ACTIVE.charset = name
    set_status_msg('Charset %s set.' % name)

ENV['decode']  = decode
ENV['charset'] = charset


