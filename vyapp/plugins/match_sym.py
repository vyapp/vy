"""
Mode: 1
Event: <Key-P> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

 
Mode: 1
Event: <Key-O> 
Description: Place the cursor at the next occurrence of ( ) { } [ ] : .

"""

def install(area):
    area.install((1, '<Key-P>', lambda event: event.widget.go_next_sym()),
                 (1, '<Key-O>', lambda event: event.widget.go_prev_sym()))


