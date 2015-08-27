"""

Mode: 1
Event: <Key-j> 
Description: Move the cursor one line down.


Mode: 1
Event: <Key-k> 
Description: Move the cursor one line up.


Mode: 1
Event: <Key-h> 
Description: Move the cursor one character left.


Mode: 1
Event: <Key-l> 
Description: Move the cursor one character right.


"""


def install(area):
    area.install(('NORMAL', '<Key-j>', lambda event: event.widget.down()),
                 ('NORMAL', '<Key-k>', lambda event: event.widget.up()),
                 ('NORMAL', '<Key-h>', lambda event: event.widget.left()),
                 ('NORMAL', '<Key-l>', lambda event: event.widget.right()))


