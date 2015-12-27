"""
"""

def beta(area):
    area.chmode('BETA')

def install(area):
    area.add_mode('BETA')
    area.install(('NORMAL', '<Key-4>', lambda event: beta(event.widget)))

