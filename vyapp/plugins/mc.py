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
Event: <Key-I>
Description: Dump the contents of a file whose path is under the cursor line.

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

Mode: NORMAL
Event: <Control-E> 
Description: Create a dir over the cursor path.

"""

from subprocess import check_output, check_call
from os.path import expanduser, dirname, join
from vyapp.stderr import printd
from vyapp.tools import error
from vyapp.app import root
from vyapp.ask import Ask

# Wrapper around these functions to get the
# error shown on the statusbar.
check_output = error(check_output)
check_call  = error(check_call)

class Mc:
    confs = {'(MC-DIRECTORY)': {'foreground': 'red'},
    '(MC-FILE)': {'foreground': 'yellow'}}

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
        ('NORMAL', '<Key-F>', lambda e: self.info()),
        ('NORMAL', '<Key-E>', lambda e: self.rename()),
        ('NORMAL', '<Control-E>', lambda e: self.create_dir()),
        ('NORMAL', '<Key-I>', self.load_path),
        ('NORMAL', '<Key-J>', lambda e:self.ls(self.ph)))

        for indi, indj in self.confs.items():
            self.area.tag_config(indi, **indj)

    @classmethod
    def c_appearance(cls, dir, file):
        """
        Used to configure foreground/background for directory entries.

        Check Tkinter Text widget tags for more info.
        """

        cls.confs['(MC-DIRECTORY)'] = dir
        cls.confs['(MC-FILE)']      = file

        printd('(Mc) Setting dir/file appearance confs = ', cls.confs)

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
        ph = self.area.get_line()
        self.ls(ph)

    def up(self):
        ph = dirname(self.ph)
        self.ls(ph)

    def info(self):
        filename = self.area.get_line()

        data = check_output('stat "%s"' % filename, shell=1, encoding='utf8')
        self.area.delete('1.0', 'end')
        self.area.append(data, '(MC-FILE)')

    def ls(self, ph):
        """
        """

        self.area.delete('1.0', 'end')

        data = check_output('find "%s" -maxdepth 1 -type d' % 
        ph, shell=1, encoding='utf8')
        self.area.append(data, '(MC-DIRECTORY)')

        data = check_output('find "%s" -maxdepth 1 -type f' % 
        ph, shell=1, encoding='utf8')
        self.area.append(data, '(MC-FILE)')

        # If the previous commands ran succesfully
        # then set the path.
        self.ph = ph

    def cp(self):
        destin = self.area.get_line()
        code   = check_call('cp -R %s "%s"' % (
            ' '.join(Mc.clipboard), destin), shell=1)

        root.status.set_msg('Files copied!')
        del Mc.clipboard[:]
        self.ls(self.ph)

    def mv(self):
        destin = self.area.get_line()
        code   = check_call('mv %s "%s"' % (
            ' '.join(Mc.clipboard), destin), shell=1)

        root.status.set_msg('Files moved!')
        del Mc.clipboard[:]
        self.ls(self.ph)

    def rename(self):
        path = self.area.get_line()

        root.status.set_msg('(Mc) Rename file:')
        ask    = Ask()
        destin = join(dirname(path), ask.data)
        code   = check_call('mv "%s" %s' % (path, 
        destin), shell=1)

        root.status.set_msg('File renamed!')
        self.ls(self.ph)

    def rm(self):
        code = check_call('rm -fr %s' % ' '.join(Mc.clipboard), shell=1)
        del Mc.clipboard[:]
        root.status.set_msg('Deleted files!')
        self.ls(self.ph)

    def create_dir(self):
        path = self.area.get_line()

        root.status.set_msg('Type dir name:')
        ask  = Ask()
        path = join(path, ask.data)
        code = check_call('mkdir "%s"' % path, shell=1)

        root.status.set_msg('Folder created!')
        self.ls(self.ph)

    def load_path(self, event):
        """
        Dump the contents of the file whose path is under the cursor.
        """
    
        filename = self.area.get_line()
        root.note.load([[filename]])
    

install = Mc


