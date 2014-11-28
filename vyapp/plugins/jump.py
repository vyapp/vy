"""

"""

def jump_next_mode(area):
    area.chmode(11)

def jump_back_mode(area):
    area.chmode(10)

def jump_next(area, char):
    index = area.search(char, 'insert', stopindex='end')
    if not index: return
    area.mark_set('insert', area.index('%s +1c' % index))
    area.see('insert')

def jump_back(area, char):
    index = area.search(char, 'insert', stopindex='1.0', backwards=True)
    if not index: return
    area.mark_set('insert', index)
    area.see('insert')

def install(area):
        area.add_mode(10)
        area.add_mode(11)

        INSTALL = [(1, '<Key-v>', lambda event: jump_next_mode(event.widget)), 
                   (1, '<Key-c>', lambda event: jump_back_mode(event.widget))]

            
        area.hook(10, '<Key>', lambda event: jump_back(event.widget, chr(event.keysym_num)))
        area.hook(11, '<Key>', lambda event: jump_next(event.widget, chr(event.keysym_num)))

        area.install(*INSTALL)










