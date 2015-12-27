"""
"""

def gamma(area):
    area.chmode('GAMMA')

def install(area):
    area.add_mode('GAMMA')
    area.install(('NORMAL', '<Key-5>', lambda event: gamma(event.widget)))

