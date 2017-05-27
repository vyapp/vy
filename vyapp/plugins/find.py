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
Event: <Alt-bracketright>
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
Event: <Alt-slash>
Description: Highligh all matched patterns inside a selected 
region of text.

Mode: Get
Event: <Alt-semicolon>
Description: Replace all matched patterns inside a selected region 
of text for the previously set replacement.
"""

from vyapp.ask import Get, Ask
from vyapp.app import root

class Find(object):
    TAGCONF = { '(CATCHED)': {
    'background':'green', 'foreground':'white'}}

    def __init__(self, area, nolinestop=False, 
        regexp=True, nocase=True, exact=False, elide=False):

        self.area  = area
        self.data  = ''
        self.index = None
        self.regex = ''

        area.tags_config(self.TAGCONF)

        area.install('find', ('NORMAL', '<Alt-slash>', lambda event: self.start()))
        self.opts = {'nolinestop': nolinestop, 'regexp': regexp,
        'nocase': nocase, 'exact': exact,'elide': elide}

    def start(self):
        self.index = ('insert', 'insert')
        root.status.set_msg('Set replacement: %s' % self.data)

        get = Get(events={
        '<Alt-bracketright>': self.set_data,
        '<Alt-o>': self.up, '<Escape>': self.cancel, 
        '<Alt-p>': self.down, '<Return>': self.cancel,
        '<Alt-slash>':  self.pick_selection_matches,
        '<Alt-period>': self.replace_on_cur,
        '<Alt-semicolon>': self.replace_on_selection, 
        '<Alt-comma>': self.replace_all_matches, 
        '<Control-n>': self.toggle_nocase_option,
        '<Control-e>': self.toggle_exact_option,
        '<Control-i>': self.toggle_elide_option,
        '<Control-l>': self.toggle_nolinestop_option},
        default_data=self.regex)

    def toggle_nocase_option(self, wid):
        self.opts['nocase'] = False if self.opts['nocase'] else True
        root.status.set_msg('nocase=%s' % self.opts['nocase'])

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
        self.data = wid.get().decode('string_escape')
        wid.delete(0, 'end')
        root.status.set_msg('Set replacement: %s' % self.data)

    def cancel(self, wid):
        self.regex = wid.get()
        self.area.tag_remove('(CATCHED)', '1.0', 'end')
        return True

    def up(self, wid):
        regex = wid.get()
        self.index = self.area.ipick('(CATCHED)', regex, index='insert', 
        stopindex='1.0', backwards=True, **self.opts)

    def down(self, wid):
        regex = wid.get()
        self.index = self.area.ipick('(CATCHED)', regex, index='insert', 
        stopindex='end', **self.opts)

    def pick_selection_matches(self, wid):
        regex = wid.get()
        self.area.map_matches('(CATCHED)', 
        self.area.collect('sel', regex, **self.opts))

    def replace_on_cur(self, wid):
        regex = wid.get()
        self.area.replace(regex, self.data, self.index[0], **self.opts)

    def replace_on_selection(self, wid):
        regex = wid.get()
        self.area.replace_ranges('sel', regex, self.data, **self.opts)

    def replace_all_matches(self, wid):
        regex = wid.get()
        self.area.replace_all(regex, self.data, '1.0', 'end', **self.opts)

install = Find










