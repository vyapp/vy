from subprocess import check_output
from os.path import expanduser, dirname, join
from vyapp.app import root

class Mc(object):
    clipboard = []

    def __init__(self, area):
        self.area = area
        self.ph   = expanduser('~')

        area.install(('NORMAL', '<Key-H>', lambda e: self.up()),
        ('NORMAL', '<Key-L>', lambda e: self.down()),
        ('NORMAL', '<Key-Y>', self.cp),
        ('NORMAL', '<Key-R>', self.cut),
        ('NORMAL', '<Key-T>', self.paste),
        ('NORMAL', '<Key-G>', self.open),
        ('NORMAL', '<Key-J>', lambda e:self.ls()))

    def down(self):
        self.ph = self.area.get_seq()
        self.ls()

    def up(self):
        self.ph = dirname(self.ph)
        print 'fuck', self.ph
        self.ls()

    def ls(self):
        ph = join(self.ph, '*')
        data = check_output('ls -d -1 %s' % ph, shell=1)
        self.area.delete('1.0', 'end')
        self.area.insert('1.0', data)

    def cp(self, event):
        pass

    def cut(self, event):
        pass

    def rm(self, event):
        pass

    def paste(self, event):
        pass

    def open(self, event):
        root.note.load([[self.area.get_seq()]])

install = Mc


