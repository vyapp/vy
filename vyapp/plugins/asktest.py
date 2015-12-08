from vyapp.ask import *

def show(event):
    print 'Pressed key'

def test(area):
    ask = Ask(area)
    ask.entry.bind('<Key>', show)

def install(area):
    area.install(('NORMAL', '<Key-equal>', lambda event: test(event.widget)))

