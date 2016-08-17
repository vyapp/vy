from vyapp.ask import Get
from vyapp.app import root
from re import escape, split
from vyapp.tools import set_status_msg
from subprocess import check_output, CalledProcessError


class Fsniff(object):
    def __init__(self, area):

        self.area = area
        self.path = ''
        area.install((-1, '<Alt-minus>', lambda event: 
        Get(area, events={'<<Idle>>' : self.find, '<<Data>>': self.update_process,
        '<Return>': self.view_on_current, '<Escape>': lambda wid: True})),
        (-1, '<Alt-equal>', lambda event: 
        Get(area, events={'<<Idle>>' : self.find, '<<Data>>': self.update_process,
        '<Return>': self.view_on_new_tab, '<Escape>': lambda wid: True})))

    def make_pattern(self, data):
        """

        """

        data    = split(' +', data)
        pattern = ''
        for ind in xrange(0, len(data)-1):
            pattern = pattern + escape(data[ind]) + '.*'
        pattern = pattern + escape(data[-1])
        return pattern

    def run_cmd(self, data):
        path = check_output(['locate', '--limit', '1', 
        '--regexp', self.make_pattern(data)])
        path = path.strip('\n').rstrip('\n')
        return path

    def find(self, wid):
        try:
            self.path = self.run_cmd(wid.get())
        except CalledProcessError:
            set_status_msg('No match found.')
        else:
            set_status_msg(
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
        set_status_msg('Locating...')

install = Fsniff



