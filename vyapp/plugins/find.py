"""
Overview
========

This module implements functionalities to find/replace patterns of text in 
an AreaVi instance that has focus.

Key-Commands
============

Namespace: find

Mode: NORMAL
Event: <Alt-slash>
Description: Set a search pattern.

Mode: Get
Event: <Alt-q>
Description: Set a replacement pattern.

Mode: Get
Event: <Alt-o>
Description: Pick the previous pattern from the cursor position.

Mode: Get
Event: <Alt-comma>
Description: Replace all occurrences.

Mode: Get
Event: <Alt-p>
Description: Pick the next pattern from the cursor position.

Mode: Get
Event: <Alt-period>
Description: Replace the next matched pattern for the previously 
set replacement.

Mode: Get
Event: <Alt-n>
Description: Highligh all matched patterns inside a selected 
region of text.

Mode: Get
Event: <Alt-semicolon>
Description: Replace all matched patterns inside a selected region 
of text for the previously set replacement.
"""

from vyapp.ask import Get
from vyapp.stderr import printd
from vyapp.app import root

class Find:
    confs = {
        'background':'green', 'foreground':'white'
    }

    opts  = {'nolinestop': False, 'regexp': False,
    'nocase': True, 'exact': False,'elide': False}

    data  = ''
    regex = ''

    def __init__(self, area):
        self.area  = area
        area.tag_config('(CATCHED)', self.confs)

        area.install('find', ('NORMAL', 
        '<Alt-slash>', lambda event: self.start()))

    @classmethod
    def c_appearance(cls, **confs):
        """
        Used to set matched region properties. These properties
        can be background, foreground etc. 

        Check Tkinter Text widget documentation on tags for more info.
        """

        cls.confs.update(confs)
        printd('Find - Setting confs = ', cls.confs)

    def start(self):
        get = Get(events={
        '<Alt-q>': self.set_data,
        '<Alt-o>': self.up, '<Escape>': self.cancel, 
        '<Alt-p>': self.down, '<Return>': self.cancel,
        '<Alt-n>':  self.pick_selmatches,
        '<Alt-period>': self.sub_xcursor,
        '<Alt-semicolon>': self.sub_xselection, 
        '<Alt-comma>': self.replace_all_matches, 
        '<Control-n>': self.toggle_nocase_option,
        '<Control-x>': self.toggle_regexp_option,

        '<Control-e>': self.toggle_exact_option,
        '<Control-i>': self.toggle_elide_option,
        '<Control-l>': self.toggle_nolinestop_option},
        default_data=Find.regex)

    def toggle_nocase_option(self, wid):
        self.opts['nocase'] = False if self.opts['nocase'] else True
        root.status.set_msg('nocase=%s' % self.opts['nocase'])

    def toggle_regexp_option(self, wid):
        self.opts['regexp'] = False if self.opts['regexp'] else True
        root.status.set_msg('regexp=%s' % self.opts['regexp'])

    def toggle_exact_option(self, wid):
        self.opts['exact'] = False if self.opts['exact'] else True
        root.status.set_msg('exact=%s' % self.opts['exact'])

    def toggle_elide_option(self, wid):
        self.opts['elide'] = False if self.opts['elide'] else True
        root.status.set_msg('elide=%s' % self.opts['elide'])

    def toggle_nolinestop_option(self, wid):
        self.opts['nolinestop'] = False if self.opts['nolinestop'] else True
        root.status.set_msg('nolinestop=%s' % self.opts['nolinestop'])

    def set_data(self, wid):
        Find.data = wid.get()
        wid.delete(0, 'end')
        root.status.set_msg('Set replacement: %s' % Find.data)

    def cancel(self, wid):
        Find.regex = wid.get()
        self.area.tag_remove('(CATCHED)', '1.0', 'end')
        return True

    def up(self, wid):
        regex = wid.get()
        index = self.area.ipick('(CATCHED)', regex, index='insert', 
        stopindex='1.0', backwards=True, **self.opts)

    def down(self, wid):
        regex = wid.get()
        index = self.area.ipick('(CATCHED)', regex, 
        index='insert', stopindex='end', **self.opts)

    def pick_selmatches(self, wid):
        """
        Highligh matched patterns inside selected text.
        """

        regex   = wid.get()
        matches = self.area.tag_xmatch('sel', regex, **self.opts)
        for _, index0, index1 in matches:
            self.area.tag_add('(CATCHED)', index0, index1)

        count = len(self.area.tag_ranges('(CATCHED)'))
        root.status.set_msg('Found: %s' % count)

    def sub_xcursor(self, wid):
        """
        Replace matched text data under the cursor.
        """

        regex = wid.get()
        # As there is just one range for catched due to ipick
        # mapping just one per call.
        index = self.area.tag_nextrange('(CATCHED)', '1.0')
        self.area.replace(regex, Find.data, index[0], **self.opts)

    def sub_xselection(self, wid):
        """
        Replace matched text for data inside selected regions.
        """
        regex = wid.get()
        count = self.area.tag_xsub('sel', regex, Find.data, **self.opts)
        root.status.set_msg('Replaced matches: %s' % count)

    def replace_all_matches(self, wid):
        """
        Replace all matches along the whole text for data.
        """
        regex = wid.get()
        count = self.area.replace_all(regex, 
            Find.data, '1.0', 'end', **self.opts)
        root.status.set_msg('Replaced matches: %s' % count)

install = Find




