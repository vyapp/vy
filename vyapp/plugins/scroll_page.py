"""
Mode: 1
Event: <Key-q> 
Description: Scroll a page up.


Mode: 1
Event: <Key-a> 
Description: Scroll one page down.

"""


def install(area):
    area.install((1, '<Key-q>', lambda event: event.widget.scroll_page_up()),
                 (1, '<Key-a>', lambda event: event.widget.scroll_page_down()))

