"""

Mode: 1
Event: <Key-comma> 
Description: Do undo.


Mode: 1
Event: <Key-period> 
Description: Do redo.


"""


def install(area):
    area.install(('NORMAL', '<Key-comma>', lambda event: event.widget.do_undo()),
                 ('NORMAL', '<Key-period>', lambda event: event.widget.do_redo()))


