"""
Overview
========

Used to find snippets accross folders.

Key-Commands
============


"""

from subprocess import Popen, STDOUT, PIPE
from vyapp.regutils import build_regex
from vyapp.widgets import LinePicker
from vyapp.areavi import AreaVi
from vyapp.app import root
from vyapp.ask import Get
from re import findall

class Fsnip:
    options = LinePicker()
    PATH    = 'ag'
    # Fsnip search options.
    file_regex = ''
    hidden     = False
    ignore     = ''
    multiline  = True
    # Either lax, literal, regex.
    type       = 'LAX'
    nocase     = False
    folder     = ''

    def  __init__(self, area):
        self.area = area
        area.install('fsnip', 
        ('NORMAL', '<Key-b>', lambda event: self.options.display()),
        ('NORMAL', '<Key-B>', lambda event: Get(events = {
        '<Return>':self.find, 
        '<Control-i>':self.set_ignore_regex, 
        '<Control-x>':self.set_type_lax, 
        '<Control-r>':self.set_type_regex, 
        '<Control-l>':self.set_type_literal, 
        '<Control-g>':self.set_file_regex, 
        '<Escape>':  lambda wid: True})))

    def set_ignore_regex(self, wid):
        Fsnip.ignore = build_regex(wid.get())
        root.status.set_msg('Set ignore file regex:%s' % Fsnip.ignore)
        wid.delete(0, 'end')

    def set_type_literal(self, wid):
        root.status.set_msg('Set search type: LITERAL')
        Fsnip.type = 'LITERAL'

    def set_type_lax(self, wid):
        root.status.set_msg('Set search type: LAX')
        Fsnip.type = 'LAX'

    def set_type_regex(self, wid):
        root.status.set_msg('Set search type: REGEX')
        Fsnip.type = 'REGEX'

    def set_file_regex(self, wid):
        self.file_regex = build_regex(wid.get())
        root.status.set_msg('Set file regex:%s' % self.file_regex)
        wid.delete(0, 'end')

    def make_cmd(self, pattern):
        cmd = [self.PATH, '--nocolor', '--nogroup',
        '--vimgrep', '--noheading']

        if self.hidden:
            cmd.append('--hidden')
        if self.ignore:
            cmd.extend(['--ignore', self.ignore])
        if self.file_regex:
            cmd.extend(['-G', self.file_regex])
        if self.nocase:
            cmd.append('-i')

        if self.type == 'LAX':
            cmd.append(build_regex(pattern))
        elif self.type == 'REGEX':
            cmd.append(pattern)
        else:
            cmd.extend(['-Q', pattern])
        cmd.append(self.area.project)

        print(cmd)
        return cmd

    def run_cmd(self, pattern):
        cmd = self.make_cmd(pattern)
        child = Popen(cmd, stdout=PIPE, stderr=STDOUT, 
        encoding=self.area.charset)
        return child.communicate()[0]

    def find(self, wid):
        """
        """

        root.status.set_msg('Set fsnip pattern!')
        output  = self.run_cmd(wid.get())
        regex   = '(.+):([0-9]+):[0-9]+:(.+)' 
        ranges  = findall(regex, output)

        if ranges:
            self.options(ranges)
        else:
            root.status.set_msg('No results:%s!' % pattern)
        return True

install = Fsnip

