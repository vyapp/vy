
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
    area.install(*INSTALL) 



