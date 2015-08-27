TAG_SHADE = '_shade_'

def toggle_shade(area):
    map0 = area.tag_nextrange(TAG_SHADE, 'insert', 'insert lineend')
    map1 = area.tag_prevrange(TAG_SHADE, 'insert', 'insert linestart')

    if map0 or map1:
        area.tag_remove(TAG_SHADE, 'insert linestart', 
                        'insert lineend')
    else:
        area.tag_add(TAG_SHADE, 'insert linestart', 
                     'insert lineend')
        
def go_prev_shade(area):
    map = area.tag_prevrange(TAG_SHADE, 'insert linestart')
    if not map: return

    area.mark_set('insert', map[0])
    area.see('insert')

def go_next_shade(area):
    map = area.tag_nextrange(TAG_SHADE, 'insert lineend')
    if not map: return

    area.mark_set('insert', map[0])
    area.see('insert')


def install(area, setup={'background':'green', 'foreground':'black'}):
    area.tag_configure(TAG_SHADE, **setup)
    area.install(('ALPHA', '<Key-q>', lambda event: toggle_shade(event.widget)),
           ('ALPHA', '<Key-a>', lambda event: go_prev_shade(event.widget)),
           ('ALPHA', '<Key-s>', lambda event: go_next_shade(event.widget)))






