from vyapp.ask import *
from re import escape

class QuickSearch(object):
    def __init__(self, area):
        """

        """
        area.add_mode('QUICK_SEARCH')
        area.install(('QUICK_SEARCH', '<Key>', lambda event: self.add_data(event.widget, event.keysym_num)),
                        ('NORMAL', '<Key-backslash>', lambda event: event.widget.chmode('QUICK_SEARCH')),
                        ('QUICK_SEARCH', '<Escape>', lambda event: self.clear_data(event.widget)),
                        ('QUICK_SEARCH', '<BackSpace>', lambda event: self.del_data(event.widget)),
                        ('QUICK_SEARCH', '<Tab>', lambda event: self.go_down(event.widget)),
                        ('QUICK_SEARCH', '<Control-Tab>', lambda event: self.go_up(event.widget)),
                        ('QUICK_SEARCH', '<Key-space>', lambda event: self.data.append('.+?')))


        self.data = []

    def clear_data(self, area):
        area.tag_remove('sel', '1.0', 'end')
        del self.data[:]

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
        area.pick_next_down('sel', ''.join(self.data), '1.0', 'end')
        
    def del_data(self, area):
        """

        """

        try:
            self.data.pop()
        except IndexError:
            return
    
        area.tag_remove('sel', '1.0', 'end')
        area.pick_next_down('sel', ''.join(self.data), '1.0', 'end')

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























