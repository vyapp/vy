
"""

"""

def select(area):
    area.chmode(1)
    area.clear_selection()

def insert(area):
    area.chmode(0)
    area.clear_selection()

def sigma(area):
    area.chmode(2)

def beta(area):
    area.chmode(3)

def mi(area):
    area.chmode(4)

def xi(area):
    area.chmode(5)


INSTALL = [(1, '<Key-i>', lambda event: insert(event.widget)),
           (-1, '<Escape>', lambda event: select(event.widget)),
           (1, '<Key-3>', lambda event: sigma(event.widget)),
           (1, '<Key-4>', lambda event: beta(event.widget)),
           (1, '<Key-5>', lambda event: mi(event.widget)),
           (1, '<Key-6>', lambda event: xi(event.widget))]


def install(area):
    # The mode in which the AreaVi is in.
    # The 0 means the standard editing mode.

    # The two basic modes, insert and selection.
    area.add_mode(0, opt=True)
    area.add_mode(1)
    area.add_mode(2)
    area.add_mode(3)
    area.add_mode(4)
    area.add_mode(5)
    area.add_mode(6)
    area.add_mode(7)
    area.chmode(1)

    area.install(*INSTALL) 






