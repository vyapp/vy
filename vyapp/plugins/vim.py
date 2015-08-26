"""

Mode: 1
Event: <Key-d> 
Description: Delete selection of text.


Mode: 1
Event: <Key-x> 
Description: Delete a line where the cursor is on.


Mode: 1
Event: <Key-z> 
Description: Delete a char from the cursor position.


Mode: 1
Event: <Key-y> 
Description: Copy selection to the clipboard.


Mode: 1
Event: <Key-u> 
Description: Cut selection then add to the clipboard.


Mode: 1
Event: <Key-t> 
Description: Paste text from the clipboard in the cursor position.


Mode: 1
Event: <Key-r> 
Description: Paste text from the clipboard one line down.


Mode: 1
Event: <Key-e> 
Description: Paste text from the clipboard one line up.

Mode: 1
Event: <Control-Y> 
Description: Add selection to the clipboard with a separator \n.


Mode: 1
Event: <Control-U> 
Description: Cut selection and add to the clipboard with a separator \n.




"""
from vyapp.app import root

def install(area):
    area.install((1, '<Key-d>', lambda event: event.widget.clsel()),
                 (1, '<Key-x>', lambda event: event.widget.cllin()),
                 (1, '<Key-z>', lambda event: event.widget.clchar()),
                 (1, '<Key-y>', lambda event: event.widget.cpsel()),
                 (1, '<Key-u>', lambda event: event.widget.ctsel()),
                 (1, '<Key-t>', lambda event: event.widget.ptsel()),
                 (1, '<Key-r>', lambda event: event.widget.ptsel_after()),
                 (1, '<Key-e>', lambda event: event.widget.ptsel_before()),
                 (1, '<Control-Y>', lambda event: event.widget.cpblock()),
                 (1, '<Control-U>', lambda event: event.widget.ctblock()))
        







