class Tab(object):
    def __init__(self, area, tab_size, char=' '):
        self.TAB_SIZE = tab_size
        self.CHAR     = char
        area.hook(0, '<Tab>', lambda event: self.insert_tab(event.widget))
    
    def insert_tab(self, area):
        area.edit_separator()
        area.insert('insert', self.CHAR * self.TAB_SIZE)
    
        return 'break'
    

install = Tab
