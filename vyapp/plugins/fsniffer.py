"""
Overview
========

Quickly open files in vy by using locate command.

Key-Commands
============

Namespace: fsniffer

Mode: Global
Event: <Alt-minus>
Description: Locate a file and open it in the current AreaVi instance.

Mode: Global
Event: <Alt-equal>
Description: Locate a file and open it in another tab.

"""

from vyapp.ask import Get
from vyapp.app import root
from vyapp.regutils import build_regex
from subprocess import check_output, CalledProcessError


class FSniffer(object):
    def __init__(self, area):

        self.area = area
        self.path = ''
        area.install('fsniffer', (-1, '<Alt-minus>', lambda event: 
        Get(events={'<<Idle>>' : self.find, '<<Data>>': self.update_process,
        '<Return>': self.view_on_current, '<Escape>': lambda wid: True})),
        (-1, '<Alt-equal>', lambda event: 
        Get(events={'<<Idle>>' : self.find, '<<Data>>': self.update_process,
        '<Return>': self.view_on_new_tab, '<Escape>': lambda wid: True})))

    def run_cmd(self, data):
        path = check_output(['locate', '--limit', '1', 
        '--regexp', build_regex(data, '.*')], encoding='utf8')
        path = path.strip('\n').rstrip('\n')
        return path

    def find(self, wid):
        try:
            self.path = self.run_cmd(wid.get())
        except CalledProcessError:
            root.status.set_msg('No match found.')
        else:
            root.status.set_msg(
            'Matched: %s' % self.path)

    def view_on_current(self, wid):
        if not self.path: return
        self.area.load_data(self.path)
        return True

    def view_on_new_tab(self, wid):
        if not self.path: return
        # The NoteVi.load method should be rethought.
        # When it throws an exception it opens a blank tab.
        root.note.load([[self.path]])
        return True

    def update_process(self, wid):
        self.path = ''
        root.status.set_msg('Locating...')

install = FSniffer


