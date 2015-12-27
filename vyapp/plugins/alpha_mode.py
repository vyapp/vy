def alpha(area):
    area.chmode('ALPHA')

def install(area):
    area.add_mode('ALPHA')
    area.install(('NORMAL', '<Key-3>', lambda event: alpha(event.widget)))

