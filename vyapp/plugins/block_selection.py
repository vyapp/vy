""" Block selection. """

def install(area):
    area.install((1, '<Control-K>', lambda event: event.widget.block_up()),
                 (1, '<Control-J>', lambda event: event.widget.block_down()),
                 (1, '<Control-H>', lambda event: event.widget.block_left()),
                 (1, '<Control-L>', lambda event: event.widget.block_right()),
                 (1, '<Control-V>', lambda event: event.widget.start_block_selection()))


