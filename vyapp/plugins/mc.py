""""
Overview
========

Implement functionalities to manage files. It is a filemanager-like plugin.

Key-Commands
============

Mode: NORMAL
Event: <Key-J> 
Description: List files in the actual AreaVi instance that has focus.

Mode: NORMAL
Event: <Key-L> 
Description: If the path under the cursor is a path for a folder then it
lists the folder files.

Mode: NORMAL
Event: <Key-K> 
Description: Add the path under the cursor to the clipboard for
removing, copying, moving.

Mode: NORMAL
Event: <Key-H> 
Description: List files in the parent folder of the path under
the cursor.

Mode: NORMAL
Event: <Key-R> 
Description: Delete all files whose paths are in the clipboard.

Mode: NORMAL
Event: <Key-E> 
Description: Rename the file/folder whose path is under the cursor.

Mode: NORMAL
Event: <Key-Y> 
Description: Copy all the clipboard files/folders recursively
to the destin which is the path under the cursor.

Mode: NORMAL
Event: <Key-T> 
Description: Move all the clipboard files/folders to the
path under the cursor.

Mode: NORMAL
Event: <Key-G> 
Description: List the paths in the clipboard.

Mode: NORMAL
Event: <Control-g> 
Description: Clear the clipboard.

"""

from subprocess import check_output, call, Popen
from os.path import expanduser, dirname, join
from vyapp.app import root
from vyapp.ask import Ask

class Mc(object):
    TAGCONF = {'(MC-DIRECTORY)': {'foreground': 'red'},
    '(MC-FILE)': {'foreground': 'blue'}}

    clipboard = []

    def __init__(self, area):
        self.area = area
        self.ph   = expanduser('~')

        area.install('mc', ('NORMAL', '<Key-H>', lambda e: self.up()),
        ('NORMAL', '<Key-L>', lambda e: self.down()),
        ('NORMAL', '<Key-Y>', lambda e: self.cp()),
        ('NORMAL', '<Key-T>', lambda e: self.mv()),
        ('NORMAL', '<Key-R>', lambda e: self.rm()),
        ('NORMAL', '<Key-K>', lambda e: self.select()),
        ('NORMAL', '<Control-g>', lambda e: self.clear_clipboard()),
        ('NORMAL', '<Key-G>', lambda e: self.list_clipboard()),
        ('NORMAL', '<Key-I>', lambda e: self.load()),
        ('NORMAL', '<Key-U>', lambda e: self.open()),
        ('NORMAL', '<Key-F>', lambda e: self.info()),
        ('NORMAL', '<Key-E>', lambda e: self.rename()),

        ('NORMAL', '<Key-J>', lambda e:self.ls()))

        area.tags_config(self.TAGCONF)

    def list_clipboard(self):
        self.area.delete('1.0', 'end')
        self.area.insert('1.0', 'Files in the clipboard!\n\n')
        self.area.insert('end', '\n'.join(Mc.clipboard))

    def clear_clipboard(self):
        del Mc.clipboard[:]
        root.status.set_msg('Cleared mc clipboard!')

    def select(self):
        filename = self.area.get_line()
        Mc.clipboard.append('"%s"' % filename)
        root.status.set_msg('Appended %s!' % filename)

    def down(self):
        self.ph = self.area.get_line()
        self.ls()

    def up(self):
        self.ph = dirname(self.ph)
        self.ls()

    def info(self):
        filename = self.area.get_line()

        data = check_output('stat "%s"' % filename, shell=1)
        self.area.delete('1.0', 'end')
        self.area.append(data, '(MC-FILE)')

    def ls(self):
        self.area.delete('1.0', 'end')

        data = check_output('find "%s" -maxdepth 1 -type d' % 
        self.ph, shell=1)
        self.area.append(data, '(MC-DIRECTORY)')

        data = check_output('find "%s" -maxdepth 1 -type f' % 
        self.ph, shell=1)
        self.area.append(data, '(MC-FILE)')

    def cp(self):
        destin = self.area.get_line()
        code = call('cp -R %s "%s"' % (' '.join(Mc.clipboard), 
        destin), shell=1)

        root.status.set_msg('Files copied!')
        del Mc.clipboard[:]
        self.ls()

    def mv(self):
        destin = self.area.get_line()
        code = call('mv %s "%s"' % (' '.join(Mc.clipboard), 
        destin), shell=1)

        root.status.set_msg('Files moved!')
        del Mc.clipboard[:]
        self.ls()

    def rename(self):
        path     = self.area.get_line()
        ask      = Ask()
        filename = ask.data.encode('utf-8')
        destin   = join(dirname(path), filename)
        code     = call('mv "%s" %s' % (path, 
        destin), shell=1)

        root.status.set_msg('File renamed!')
        self.ls()

    def rm(self):
        code = call('rm -fr %s' % ' '.join(Mc.clipboard), shell=1)
        del Mc.clipboard[:]
        root.status.set_msg('Deleted files!')
        self.ls()

    def load(self):
        filename = self.area.get_line()
        root.note.load([[filename]])

    def open(self):
        filename = self.area.get_line()
        # No need for "" because it is passing the entire filename
        # as parameter.
        Popen(['xdg-open', '%s'  % filename])

install = Mc




