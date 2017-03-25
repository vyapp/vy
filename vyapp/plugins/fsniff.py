from vyapp.ask import Get
from vyapp.app import root
from vyapp.regutils import build_regex
from subprocess import check_output, CalledProcessError


class Fsniff(object):
    def __init__(self, area):

        self.area = area
        self.path = ''
        area.install('fsniff', (-1, '<Alt-minus>', lambda event: 
        Get(events={'<<Idle>>' : self.find, '<<Data>>': self.update_process,
        '<Return>': self.view_on_current, '<Escape>': lambda wid: True})),
        (-1, '<Alt-equal>', lambda event: 
        Get(events={'<<Idle>>' : self.find, '<<Data>>': self.update_process,
        '<Return>': self.view_on_new_tab, '<Escape>': lambda wid: True})))

    def run_cmd(self, data):
        path = check_output(['locate', '--limit', '1', 
        '--regexp', build_regex(data, '.*')])
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

install = Fsniff







