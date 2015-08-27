""" Block selection. """

def install(area):
    area.install(('NORMAL', '<Control-K>', lambda event: event.widget.block_up()),
                 ('NORMAL', '<Control-J>', lambda event: event.widget.block_down()),
                 ('NORMAL', '<Control-H>', lambda event: event.widget.block_left()),
                 ('NORMAL', '<Control-L>', lambda event: event.widget.block_right()),
                 ('NORMAL', '<Control-V>', lambda event: event.widget.start_block_selection()))



