"""
Overview
========

This module implements a scheme to spare some keystrokes when switching between modes that
are implemented in other modes like switching from PDB mode to NORMAL mode. The PDB mode is
implemented in BETA mode.

Usage
=====

The NORMAL mode is the mode in which most editing keycommands are implemented, there will
occur situations that some keycommands that are implemented in other modes will be used more often.

Suppose one is debugging a python application in PDB mode, it will be needed to switch to NORMAL mode
to do some editing, testing etc. The most obvious way to do that is switching to NORMAL mode by pressing 
<Escape> then doing the editing then switching back to PDB mode by switching to BETA mode then pressing 
<Key-p>. But it may be a bit awkward, a good way to avoid having to switch to BETA mode is using
the scheme that is implemented in this plugin.

Suppose a given AreaVi instance is in PDB mode then if the keycommand <Alt-Escape> is issued then
when that AreaVi instance is in NORMAL mode and the keycommand <Escape> is issued then
it will put the AreaVi instance in PDB mode again. The same behavior is expected with other modes as well.

When the secondary mode is not going to be used very often anymore then it is possible to get back the
standard behavior that is when pressing <Escape> in NORMAL mode it remains in NORMAL mode. For such
just switch to NORMAL mode then press <Alt-Escape>.

Key-Commands
============

Mode: -1
Event: <Alt-Escape>
Description: Set keycommand <Escape> in NORMAL mode to be used as a keycommand to switch between
NORMAL mode and the current AreaVi instance mode.

Mode: NORMAL
Event: <Escape>
Description: Switch from NORMAL mode to the target mode that was set by pressing <Alt-Escape>.
"""

from vyapp.tools import set_status_msg
from vyapp.exe import exec_quiet

class Switch(object):
    target_id  = 'NORMAL'
    default_id = 'NORMAL'
    def __init__(self, area):
        area.install(('-1', '<Alt-Escape>',  lambda event: self.set_target_id(event.widget)),
                     (Switch.default_id, '<Escape>', lambda event: exec_quiet(event.widget.chmode, Switch.target_id)))

    def set_target_id(self, area):
        """
        """

        Switch.target_id = area.id
        set_status_msg('%s mode pinned!' % area.id)

install = Switch


