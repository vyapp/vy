"""

Overview
========


Key-Commands
============

Namespace: assoc

Mode: 
Event: 
Description: 

"""

from vyapp.app import root

def install(area):
    area.install('assoc', ('NORMAL', '<Key-question>', 
    lambda event: root.status.set_msg('\n'.join(
    event.widget.get_assoc_data()))))










