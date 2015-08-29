"""


"""

from traceback import format_exc as debug
from vyapp.stdout import Stdout
from vyapp.tools import exec_quiet, set_status_msg
from vyapp.ask import *
import sys

def redirect_stdout(area):
    try:
        sys.stdout.remove(area)
    except ValueError:
        pass
    sys.stdout.append(Stdout(area))
    set_status_msg('Output redirected to %s' % area.index('insert'))

def install(area):
    area.install(('NORMAL', '<Control-W>', lambda event: event.widget.tag_delete_ranges(Stdout.TAG_CODE)),
           ('NORMAL', '<Control-Tab>', lambda event: sys.stdout.restore()),
           ('NORMAL', '<Key-W>', lambda event: event.widget.tag_delete(Stdout.TAG_CODE)),
           ('NORMAL', '<Control-w>', lambda event: exec_quiet(sys.stdout.remove, event.widget)),
           ('NORMAL', '<Tab>', lambda event: redirect_stdout(event.widget)))

   






















