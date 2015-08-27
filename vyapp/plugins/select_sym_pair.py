"""

Mode: 1
Event: <Key-slash> 
Description: Select text between pairs of ( ) [] {} when the cursor
is placed over one of these characters.

"""


def install(area):
    area.install(('NORMAL', '<Key-slash>', lambda event: event.widget.select_case_pair(('(', ')'))),
                 ('NORMAL', '<Key-slash>', lambda event: event.widget.select_case_pair(('[', ']'))),
                 ('NORMAL', '<Key-slash>', lambda event: event.widget.select_case_pair(('{', '}'))))


