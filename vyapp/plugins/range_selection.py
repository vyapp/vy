""" 
Range selection 

Mode: 1
Event: <Control-k> 
Description: Add/remove selection one line up from the initial selection mark.
The initial selection mark is placed with Event: <Control-v>.


Mode: 1
Event: <Control-j> 
Description: Add/remove selection one line down from the initial selection mark.
The initial selection mark is placed with Event: <Control-v>.


Mode: 1
Event: <Control-l> 
Description: Add/remove selection one character right from the initial selection mark.
The initial selection mark is placed with Event: <Control-v>.


Mode: 1
Event: <Control-h> 
Description: Add/remove selection one character left from the initial selection mark.
The initial selection mark is placed with Event: <Control-v>.


Mode: 1
Event: <Control-v> 
Description: Drop a mark selection to be a reference for Event: <Control-k> Event: <Control-j> 

"""

def install(area):
    area.install(('NORMAL', '<Control-k>', lambda event: event.widget.sel_up()),
                 ('NORMAL', '<Control-j>', lambda event: event.widget.sel_down()),
                 ('NORMAL', '<Control-h>', lambda event: event.widget.sel_left()),
                 ('NORMAL', '<Control-l>', lambda event: event.widget.sel_right()),
                 ('NORMAL', '<Control-v>', lambda event: event.widget.start_selection()))



