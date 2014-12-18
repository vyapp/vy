from vyapp.ask import *
from re import escape

class QuickSearch(object):
    def __init__(self, area):
        """

        """
        area.add_mode('Quick Search')

        self.INSTALL = [('Quick Search', '<Key>'          , lambda event: self.add_data(event.widget, event.keysym_num)),
                        (1, '<Key-backslash>'    , lambda event: self.start_search(event.widget)),
                        ('Quick Search', '<BackSpace>'    , lambda event: self.del_data(event.widget)),
                        ('Quick Search', '<Tab>'    , lambda event: self.go_down(event.widget)),
                        ('Quick Search', '<Control-Tab>'    , lambda event: self.go_up(event.widget)),
                        ('Quick Search', '<Key-space>'   , lambda event: self.data.append('.+?'))]

        area.install(*self.INSTALL)

    def start_search(self, area):
        """

        """

        self.data = []
        area.chmode('Quick Search')

    def add_data(self, area, char):
        """

        """

        try:
            char = chr(char)
        except ValueError:
            return
        else:
            char = escape(char)
            self.data.append(char)
    
        area.tag_remove('sel', '1.0', 'end')
        area.mark_set('insert', '1.0')
        area.pick_next_down('sel', ''.join(self.data))
        
    def del_data(self, area):
        """

        """

        try:
            self.data.pop()
        except IndexError:
            return
    
        area.tag_remove('sel', '1.0', 'end')
        area.mark_set('insert', '1.0')
        area.pick_next_down('sel', ''.join(self.data))

    def go_up(self, area):
        """

        """

        area.tag_remove('sel', '1.0', 'end')
        area.pick_next_up('sel', ''.join(self.data))
        
        
    def go_down(self, area):
        """

        """

        area.tag_remove('sel', '1.0', 'end')
        area.pick_next_down('sel', ''.join(self.data))



install = QuickSearch




















