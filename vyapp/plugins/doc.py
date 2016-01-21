"""
"""
from os.path import dirname, join

def load_book(area):
    dir = dirname(dirname(__file__))
    ph  = join(dir, 'data', 'BOOK.md')
    area.load_data(ph)

def install(area):
    area.install(('BETA', '<Key-h>', lambda event: load_book(event.widget)))



