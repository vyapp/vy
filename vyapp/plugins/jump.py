"""

"""

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
        area.add_mode('JUMP_BACK')
        area.add_mode('JUMP_NEXT')

        area.install(('NORMAL', '<Key-v>', lambda event: event.widget.chmode('JUMP_NEXT')), 
                     ('NORMAL', '<Key-c>', lambda event: event.widget.chmode('JUMP_BACK')),
                     ('JUMP_BACK', '<Key>', lambda event: jump_back(event.widget, chr(event.keysym_num))),
                     ('JUMP_NEXT', '<Key>', lambda event: jump_next(event.widget, chr(event.keysym_num))))













