"""
Mode: 1
Event: <Key-C> 
Description: Add selection to a character whose cursor is on.


Mode: 1
Event: <Key-V> 
Description: Remove selection from a character whose cursor is on.
"""

def install(area):
    area.install((1, '<Key-C>', lambda event: event.widget.select_char()),
                 (1, '<Key-V>', lambda event: event.widget.unselect_char()))


