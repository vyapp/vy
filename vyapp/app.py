"""
This module exposes the vyapp.app.root attribute that is a variable pointing
to the App class instance. The App class instance holds all vy editor's widgets.
"""

from .base import App, Debug
import argparse
import itertools
import sys

parser = argparse.ArgumentParser()

parser.add_argument('files', nargs='*', help='Files')

parser.add_argument(
'-t', '--tab', dest='scheme', action='append_const', const=None,
default=[], help='Instantiate a new tab. Ex: -t -p file0 file1')

parser.add_argument(
'-p', '--panel', action='append', dest='scheme', default=[], nargs='+', 
help='Open files in vertical/horizontal ways -p file0 file1 -p file2')

parser.add_argument('-v', '--verbose', action='store_true',
help='Show exceptions and messages.')

args = parser.parse_args()

lst = [list(g) for k, g in itertools.groupby(args.scheme, 
lambda x: not x) if not k]

# parser.add_option("-v", "--debug", action="store_true", 
# default=False, dest="debug")
# (opt, args) = parser.parse_args()

# It points to the root toplevel window of vy. 
# It is the one whose AreaVi instances
# are placed on. 
root = App()
lst  = lst + [[[ind]] for ind in args.files]

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
if not args.verbose: sys.stderr = Debug()





