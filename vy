#! /usr/bin/env python
from optparse import OptionParser

if __name__ == '__main__':
    from vyapp.app import App


    parser   = OptionParser()
    parser.add_option("-l", "--lst", dest="lst",
                      help='''./vy -l "[[['vy', 'setup.py']], [['./vyapp/plugins/ibash.py', './vyapp/plugins/cmd.py']]]"''', 
                      metavar="string", default=[])
                  
    parser.add_option("-n", "--max-tabs", dest="max_tabs",
                      metavar="string", default='10')

    (opt, args) = parser.parse_args()

    root = App(int(opt.max_tabs))
    lst  = eval(str(opt.lst))
    lst  = lst + map(lambda ind: [[ind]], args)

    if not lst: root.note.create('None')
    else: root.note.load(*lst)
    root.mainloop()














