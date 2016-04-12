#! /usr/bin/env python
from optparse import OptionParser
import sys

class Debug(object):
    def write(self, *args):
        pass

if __name__ == '__main__':
    from vyapp.app import App


    parser   = OptionParser()
    parser.add_option("-l", "--lst", dest="lst",
                      help='''This option takes a string of the form:
                      "[[['file0', 'file1']], [['file2', 'file3']], ...]"
                      It displays files in different tabs and paned windows.''', 
                      metavar="string", default=[])

    parser.add_option("-v", "--debug", action="store_true", default=False, dest="debug")

    (opt, args) = parser.parse_args()


    root = App()
    lst  = eval(str(opt.lst))
    lst  = lst + map(lambda ind: [[ind]], args)

    if not lst: root.note.create('None')
    else: root.note.load(*lst)
    
    # It first waits vyrc file to be loaded in order to set sys.stderr.
    # Otherwise errors when loading the vyrc file will be missed as well as when
    # attempting to load a non existing file.
    if not opt.debug: sys.stderr = Debug()
    root.mainloop()




