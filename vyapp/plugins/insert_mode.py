"""
"""

def insert(area):
    area.chmode('INSERT')
    area.clear_selection()

def install(area):
    # The two basic modes, insert and selection.
    area.add_mode('INSERT', opt=True)
    area.install(('NORMAL', '<Key-i>', lambda event: insert(event.widget)))

