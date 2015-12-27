"""
"""

def normal(area):
    area.chmode('NORMAL')
    area.clear_selection()

def install(area):
    area.add_mode('NORMAL')
    area.chmode('NORMAL')
    area.install((-1, '<Escape>', lambda event: normal(event.widget)))

