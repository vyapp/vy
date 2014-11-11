from vyapp.ask import *

class Find(object):
    def __init__(self, area, setup={'background':'blue', 'foreground':'yellow'}):
        self.area         = area
        self.regex        = ''
        self.data         = ''
        self.TAG_FOUND    = '__found__'

        area.tag_config(self.TAG_FOUND, **setup)


        self.INSTALL = [(1, '<Control-q>'    , lambda event: self.set_regex()),
                        (1, '<Control-Q>'    , lambda event: self.set_data()),
                        (1, '<Key-Q>'        , lambda event: self.area.tag_remove(self.TAG_FOUND, '1.0', 'end')),
                        (1, '<Control-Left>' , lambda event: self.area.tag_add_found(self.TAG_FOUND, self.area.tag_find_ranges('sel', self.regex))),
                        (1, '<Shift-Left>' , lambda event: self.area.tag_replace_ranges('sel', self.regex, self.data)),

                        (1, '<Control-Right>', lambda event: self.area.replace(self.regex, self.data, 'insert')),

                        (1, '<Shift-Up>'     , lambda event: self.area.replace_all(self.regex, self.data, '1.0', 'insert')),
                        (1, '<Shift-Right>'  , lambda event: self.area.replace_all(self.regex, self.data)),
                        (1, '<Shift-Down>'   , lambda event: self.area.replace_all(self.regex, self.data, 'insert', 'end')),

                        (1, '<Control-Up>'   , lambda event: self.area.pick_next_up(self.TAG_FOUND, self.regex)),
                        (1, '<Control-Down>' , lambda event: self.area.pick_next_down(self.TAG_FOUND, self.regex))]

        area.install(*self.INSTALL)


    def set_regex(self):
        ask = Ask(self.area, 'Regex', self.regex)
        self.regex = ask.data

        # self.regex = self.area.get_ranges('sel')

    def set_data(self):
        ask = Ask(self.area, 'Replace', self.data)
        self.data = ask.data

        # self.data = self.area.get_ranges('sel')


install = Find



















