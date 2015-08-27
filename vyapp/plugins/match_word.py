"""

Mode: 1
Event: <Key-bracketright> 
Description: Place the cursor at the beginning of the next word.


Mode: 1
Event: <Key-braceright> 
Description: Place the cursor at the beginning of the previous word.


Mode: 1
Event: <Key-bracketleft> 
Description: Add selection to a word where the cursor is placed on.

"""

def install(area):
    area.install(('NORMAL', '<Key-bracketright>', lambda event: event.widget.go_next_word()),
                 ('NORMAL', '<Key-braceright>', lambda event: event.widget.go_prev_word()),
                 ('NORMAL', '<Key-bracketleft>', lambda event: event.widget.select_word()))



