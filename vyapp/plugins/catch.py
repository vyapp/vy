"""
"""

from vyapp.ask import Get, Ask

class Catch(object):
    def __init__(self, area, setup={'background':'green', 'foreground':'white'}):
        self.area  = area
        self.data  = ''
        self.index = None
        self.regex = ''

        area.tag_config('(CATCHED)', **setup)

        area.install(('NORMAL', '<Alt-slash>'    , lambda event: self.start()), 
                     ('NORMAL', '<Alt-bracketright>'    , lambda event: self.set_data()))


    def start(self):
        self.index = ('insert', 'insert')
        get = Get(self.area, events={'<Alt-o>': self.up, '<Escape>': self.stop, 
                                     '<Alt-p>': self.down, '<Return>': self.stop,
                                     '<Alt-b>': lambda regex: self.area.map_matches('(CATCHED)', self.area.collect('sel', regex)),
                                     '<Alt-period>': lambda regex: self.area.replace(regex, self.data, self.index[0]),
                                     '<Alt-semicolon>': lambda regex: self.area.replace_ranges('sel', regex, self.data), 
                                     '<Alt-comma>': lambda regex: self.area.replace_all(regex, self.data, '1.0', 'end')}, default_data=self.regex)
    def set_data(self):
        ask = Ask(self.area, default_data = self.data)
        self.data = ask.data

    def stop(self, regex):
        self.area.tag_remove('(CATCHED)', '1.0', 'end')
        self.regex = regex
        return True

    def up(self, regex):
        self.area.tag_remove('(CATCHED)', '1.0', 'end')
        index = self.area.pick_next_up('(CATCHED)', regex, self.index[0])
        self.index = ('insert', 'insert') if not index else index

    def down(self, regex):
        self.area.tag_remove('(CATCHED)', '1.0', 'end')
        index = self.area.pick_next_down('(CATCHED)', regex, self.index[1])
        self.index = ('insert', 'insert') if not index else index


install = Catch







