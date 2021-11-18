"""
Overview
========

A wrapper around silver search.

Key-Commands
============

Namespace: sniper

Mode: NORMAL
Event: <Key-B>
Description: Get a text pattern and perform a search.

Mode: NORMAL
Event: <Key-b>
Description: Open the previous found occurrences of the pattern.

Mode: INPUT
Event: <Control-i>
Description: Set a file pattern for silver search to ignore.

Mode: INPUT
Event: <Control-x>
Description: Set lax pattern search.

Mode: INPUT
Event: <Control-r>
Description: Set regex search for patterns.

Mode: INPUT
Event: <Control-l>
Description: Set literal search for patterns.

Mode: INPUT
Event: <Control-w>
Description: Set wide search, in wide search mode sniper
will be searching in the directories that were set
in Sniper.dirs. In non wide search sniper will search
in your current file project and in your AreaVi.HOME.

Mode: INPUT
Event: <Control-m>
Description: Set multiline search.

"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.regutils import build_regex
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.tools import error
from vyapp.stderr import printd
from vyapp.app import root
from vyapp.ask import Get
from re import findall

class Sniper:
    options = LinePicker()
    # Path to ag program.
    path = 'ag'

    # Dirs where ag will search when in 
    # wide mode.
    dirs = ()

    # Sniper search options.
    file_regex = ''
    ignore     = ''
    multiline  = True

    # Either lax(1), literal(0), regex(2).
    type   = 1
    nocase = False
    wide   = True

    def  __init__(self, area):
        self.area = area

        area.install('sniper', 
        (-1, '<Alt-s>', self.display_matches),
        (-1, '<Alt-r>', self.find_matches))

        if not self.dirs:
            printd('Sniper - Sniper.dirs is not set.')

    def display_matches(self, event):
        self.options.display()
        return 'break'

    def find_matches(self, event):
        wid = Get(events = {
        '<Return>':self.find, 
        '<Control-i>':self.set_ignore_regex, 
        '<Control-x>':self.set_type_lax, 
        '<Control-r>':self.set_type_regex, 
        '<Control-l>':self.set_type_literal, 
        '<Control-g>':self.set_file_regex, 
        '<Control-s>':self.set_nocase, 
        '<Control-w>':self.set_wide, 
        '<Control-m>':self.set_multiline, 
        '<Escape>':  lambda wid: True})
        return 'break'
        
    @classmethod
    def c_path(cls, path='ag'):
        """
        Set the ag path. If ag is known to your environment then
        there is no need to set it.
        """
        pass
        cls.path = path
        printd('Sniper - Setting ag path = ', path)

    @classmethod
    def c_dirs(cls, *dirs):
        """
        Folders where ag will be searching for data.
        """
        cls.dirs = dirs
        printd('Sniper - Setting dirs =', *dirs)

    def set_wide(self, wid):
        Sniper.wide = False if Sniper.wide else True
        root.status.set_msg('Set wide search: %s' % Sniper.wide)

    def set_multiline(self, wid):
        Sniper.multiline = False if Sniper.multiline else True
        root.status.set_msg('Set multiline search: %s' % Sniper.multiline)

    def set_nocase(self, wid):
        Sniper.nocase = False if Sniper.nocase else True
        root.status.set_msg('Set nocase search: %s' % Sniper.nocase)

    def set_ignore_regex(self, wid):
        Sniper.ignore = wid.get()
        root.status.set_msg('Set ignore file regex:%s' % Sniper.ignore)
        wid.delete(0, 'end')

    def set_type_literal(self, wid):
        root.status.set_msg('Set search type: LITERAL')
        Sniper.type = 0

    def set_type_lax(self, wid):
        root.status.set_msg('Set search type: LAX')
        Sniper.type = 1

    def set_type_regex(self, wid):
        root.status.set_msg('Set search type: REGEX')
        Sniper.type = 2

    def set_file_regex(self, wid):
        self.file_regex = wid.get()
        root.status.set_msg('Set file regex:%s' % self.file_regex)
        wid.delete(0, 'end')

    def make_cmd(self, pattern):
        cmd = [self.path, '--nocolor', '--nogroup',
        '--vimgrep', '--noheading']

        if self.ignore:
            cmd.extend(['--ignore', self.ignore])
        if self.file_regex:
            cmd.extend(['-G', self.file_regex])
        if self.nocase:
            cmd.append('-s')
        if not self.multiline:
            cmd.append('--nomultiline')
        else:
            cmd.append('--multiline')

        if self.type == 1:
            cmd.append(build_regex(pattern))
        elif self.type == 2:
            cmd.append(pattern)
        else:
            cmd.extend(['-Q', pattern])

        if not Sniper.wide:
            cmd.extend([self.area.project, AreaVi.HOME])
        else:
            cmd.extend(Sniper.dirs)
        return cmd

    def run_cmd(self, pattern):
        cmd = self.make_cmd(pattern)
        child = Popen(cmd, stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset)
        return child.communicate()[0]

    @error
    def find(self, wid):
        """
        """

        pattern = wid.get()
        root.status.set_msg('Set pattern:%s!' % pattern)

        output = self.run_cmd(pattern)
        regex  = '(.+):([0-9]+):[0-9]+:(.+)' 
        ranges = findall(regex, output)

        if ranges:
            self.options(ranges)
        else:
            root.status.set_msg('No results:%s!' % pattern)
        return True

install = Sniper

