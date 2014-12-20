"""

"""
from vyapp.ask import *

def go_to_pos(area):
    ask = Ask(area, 'Line.Col', '')

    if not ask.data: return

    try:
        line, col = ask.data.split('.')
    except ValueError:
        area.setcurl(ask.data)
    else:
        area.setcur(line, col)    

install = lambda area: area.install((1, '<F3>', lambda event: go_to_pos(event.widget)))

