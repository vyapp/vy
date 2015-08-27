"""
Mode: 1
Event: <Key-o> 
Description: Place the cursor at the beginning of the line.


Mode: 1
Event: <Key-p> 
Description: Place the cursor at the end of the line.
"""

def install(area):
    area.install(('NORMAL', '<Key-o>', lambda event: event.widget.go_line_start()),
                 ('NORMAL', '<Key-p>', lambda event: event.widget.go_line_end()))


