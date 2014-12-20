from traceback import format_exc as debug
from vyapp.tools.misc import Stdout, exec_quiet
from vyapp.ask import *
import sys

def redirect_stdout(area):
    try:
        sys.stdout.remove(area)
    except ValueError:
        pass
    sys.stdout.append(Stdout(area))

def install(area):
    area.install((1, '<Control-W>', lambda event: event.widget.tag_delete_ranges(Stdout.TAG_CODE)),
           (1, '<Control-Tab>', lambda event: sys.stdout.restore()),
           (1, '<Key-W>', lambda event: event.widget.tag_delete(Stdout.TAG_CODE)),
           (1, '<Control-w>', lambda event: exec_quiet(sys.stdout.remove, event.widget)),
           (1, '<Tab>', lambda event: redirect_stdout(event.widget)))

   

















