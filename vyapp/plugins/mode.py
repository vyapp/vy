"""
This module implements basic modes that are used by built-in plugins.

"""

def normal(area):
    area.chmode('NORMAL')
    area.clear_selection()

def insert(area):
    area.chmode('INSERT')
    area.clear_selection()

def alpha(area):
    area.chmode('ALPHA')

def beta(area):
    area.chmode('BETA')

def gamma(area):
    area.chmode('GAMMA')

def delta(area):
    area.chmode('DELTA')


def install(area):
    # The mode in which the AreaVi is in.
    # The 0 means the standard editing mode.

    # The two basic modes, insert and selection.
    area.add_mode('INSERT', opt=True)
    area.add_mode('NORMAL')
    area.add_mode('ALPHA')
    area.add_mode('BETA')
    area.add_mode('GAMMA')
    area.add_mode('DELTA')

    area.chmode('NORMAL')

    area.install(('NORMAL', '<Key-i>', lambda event: insert(event.widget)),
           (-1, '<Escape>', lambda event: normal(event.widget)),
           ('NORMAL', '<Key-3>', lambda event: alpha(event.widget)),
           ('NORMAL', '<Key-4>', lambda event: beta(event.widget)),
           ('NORMAL', '<Key-5>', lambda event: gamma(event.widget)),
           ('NORMAL', '<Key-6>', lambda event: delta(event.widget)))









