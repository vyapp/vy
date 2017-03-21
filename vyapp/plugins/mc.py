from subprocess import check_output, call, Popen
from os.path import expanduser, dirname, join
from vyapp.app import root

class Mc(object):
    clipboard = []

    def __init__(self, area):
        self.area = area
        self.ph   = expanduser('~')

        area.install(('NORMAL', '<Key-H>', lambda e: self.up()),
        ('NORMAL', '<Key-L>', lambda e: self.down()),
        ('NORMAL', '<Key-Y>', lambda e: self.cp()),
        ('NORMAL', '<Key-T>', lambda e: self.mv()),
        ('NORMAL', '<Key-R>', lambda e: self.rm()),
        ('NORMAL', '<Key-K>', lambda e: self.select()),
        ('NORMAL', '<Control-g>', lambda e: self.clear_clipboard()),
        ('NORMAL', '<Key-G>', lambda e: self.list_clipboard()),
        ('NORMAL', '<Key-I>', lambda e: self.load()),
        ('NORMAL', '<Key-U>', lambda e: self.open()),

        ('NORMAL', '<Key-J>', lambda e:self.ls()))

    def list_clipboard(self):
        self.area.delete('1.0', 'end')
        self.area.insert('1.0', 'Files in the clipboard!\n\n')
        self.area.insert('end', '\n'.join(Mc.clipboard))

    def clear_clipboard(self):
        del Mc.clipboard[:]
        root.status.set_msg('Cleared mc clipboard!')

    def select(self):
        filename = self.area.get_seq()
        Mc.clipboard.append(filename)
        root.status.set_msg('Appended %s!' % filename)

    def down(self):
        self.ph = self.area.get_seq()
        self.ls()

    def up(self):
        self.ph = dirname(self.ph)
        self.ls()

    def ls(self):
        data = check_output('find %s -maxdepth 1' % self.ph, shell=1)
        self.area.delete('1.0', 'end')
        self.area.insert('1.0', data)

    def cp(self):
        destin = self.area.get_seq()
        code = call('cp %s %s' % (' '.join(Mc.clipboard), destin), shell=1)
        root.status.set_msg('Files copied!')
        del Mc.clipboard[:]
        self.ls()

    def mv(self):
        destin = self.area.get_seq()
        code = call('mv %s %s' % (' '.join(Mc.clipboard), destin), shell=1)
        root.status.set_msg('Files moved!')
        del Mc.clipboard[:]
        self.ls()

    def rm(self):
        code = call('rm %s' % ' '.join(Mc.clipboard), shell=1)
        del Mc.clipboard[:]
        root.status.set_msg('Deleted files!')
        self.ls()

    def load(self):
        filename = self.area.get_seq()
        root.note.load([[filename]])

    def open(self):
        filename = self.area.get_seq()
        Popen(['xdg-open', filename])

install = Mc




