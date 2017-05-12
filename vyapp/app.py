"""
This module exposes the vyapp.app.root attribute that is a variable pointing
to the App class instance. The App class instance holds all vy editor's widgets.
"""

from base import App, Debug
import sys

if __name__ != '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-l", "--lst", dest="lst",
    help='''This option takes a string of the form:
    "[[['file0', 'file1']], [['file2', 'file3']], ...]"
    It displays files in different tabs and paned windows.''', 
    metavar="string", default=[])

    parser.add_option("-v", "--debug", action="store_true", 
    default=False, dest="debug")
    (opt, args) = parser.parse_args()

    # It points to the root toplevel window of vy. 
    # It is the one whose AreaVi instances
    # are placed on. 
    root = App()
    lst  = eval(str(opt.lst))
    lst  = lst + map(lambda ind: [[ind]], args)
    
    # It has to be called from here.
    # otherwise the plugins will not
    # be able to import vyapp.app.root
    # variable.
    root.create_vyrc()

    if not lst: root.note.create('none')
    else: root.note.load(*lst)

    # It first waits vyrc file to be loaded in order to set sys.stderr.
    # Otherwise errors when loading the vyrc file will be missed as well as when
    # attempting to load a non existing file.
    if not opt.debug: sys.stderr = Debug()



