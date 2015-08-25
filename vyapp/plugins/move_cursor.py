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
    area.install((1, '<Key-j>', lambda event: event.widget.down()),
                 (1, '<Key-k>', lambda event: event.widget.up()),
                 (1, '<Key-h>', lambda event: event.widget.left()),
                 (1, '<Key-l>', lambda event: event.widget.right()))

