Guide
=====

1) Protype of functions that receives tag names and ranges mapping positions of the AreaVi instance.

def do_something_with_tag(self, name, index0, index1, index2, ...):

name corresponds to the tag name, index0, index1 ... to index's in the Text instance.

It is okay using names like ind0, ind1, ind2, ... indi, indj, pos0, pos1, ...
 inside functions to mean index's.

The name of the functions that are related with tags should follow tkinter style. It should
start with a 'tag'. Like in..

def tag_do_something(self, name, *args):


3) Some plugins may need to show information on the status bar, for such use set_status_msg.
It is needed to take care to not overwrite previous msgs from other plugins.

4) Some plugins that add a tag and such a tag should have a config like background and foreground
these settings should be received from the user like in.

# Plugin code.
def install(area, setup={'background':'yellow'}):
    pass

# Code in vyrc.
INSTALL = [[find, {'background': 'blue'}]]






