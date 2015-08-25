"""
Mode: 1
Event: <Key-w> 
Description: Scroll one line up.


Mode: 1
Event: <Key-s> 
Description: Scroll one line down.
"""

def install(area):
    area.install((1, '<Key-w>', lambda event: event.widget.scroll_line_up()),
                 (1, '<Key-s>', lambda event: event.widget.scroll_line_down()))

