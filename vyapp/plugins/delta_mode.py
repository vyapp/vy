"""
"""

def delta(area):
    area.chmode('DELTA')

def install(area):
    area.add_mode('DELTA')
    area.install(('NORMAL', '<Key-6>', lambda event: delta(event.widget)))











