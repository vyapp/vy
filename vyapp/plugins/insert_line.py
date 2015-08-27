"""
Mode: 1
Event: <Key-m> 
Description: Insert a line down then goes insertion mode.


Mode: 1
Event: <Key-n> 
Description: Insert a line up then goes insertion mode.


"""


def install(area):
    area.install(('NORMAL', '<Key-m>', lambda event: event.widget.insert_line_down()),
                 ('NORMAL', '<Key-n>', lambda event: event.widget.insert_line_up()))


