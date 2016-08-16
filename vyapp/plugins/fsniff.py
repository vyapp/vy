from vyapp.ask import Get
from vyapp.app import root
from re import escape, split
from vyapp.tools import set_status_msg
from subprocess import check_output

class Fsniff(object):
    def __init__(self, area):
        self.area = area
        area.install((-1, '<Alt-equal>', lambda event: 
        Get(area, events={'<Return>' : self.echo, 
        '<Alt-comma>': self.view_on_new_tab, 
        '<Control-d>': self.view_on_current, '<Escape>': lambda wid: True})))

    def make_pattern(self, data):
        """

        """

        data    = split(' +', data)
        pattern = ''
        for ind in xrange(0, len(data)-1):
            pattern = pattern + escape(data[ind]) + '.*'
        pattern = pattern + escape(data[-1])
        return pattern

    def find(self, data):
        data = check_output(['locate', '--regexp', self.make_pattern(data)])
        data = data.split('\n', 2)
        return data[0]

    def view_on_current(self, wid):
        path = self.find(wid.get())
        self.area.load_data(path)
        return True

    def view_on_new_tab(self, wid):
        path = self.find(wid.get())
        root.note.load([[path]])
        return True

    def echo(self, wid):
        path = self.find(wid.get())
        set_status_msg('Matched: %s' % path)

install = Fsniff
