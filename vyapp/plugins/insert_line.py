"""
Mode: 1
Event: <Key-m> 
Description: Insert a line down then goes insertion mode.


Mode: 1
Event: <Key-n> 
Description: Insert a line up then goes insertion mode.


"""

def insert_down(area):
        area.insert_line_down()
        area.chmode('INSERT')

def insert_up(area):
        area.insert_line_up()
        area.chmode('INSERT')

def install(area):
    area.install(('NORMAL', '<Key-m>', lambda event: insert_down(event.widget)),
                 ('NORMAL', '<Key-n>', lambda event: insert_up(event.widget)))



