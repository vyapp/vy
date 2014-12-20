"""

"""

from vyapp.tools.misc import exc, set_status_msg
from vyapp.ask import Ask
from vyapp.app import ENV, DEV

import sys

def exec_cmd(area, env):
    ask    = Ask(area, 'Cmd')
    area.active()
    exc(ask.data, env)

def exec_region(area, env):
    data = area.tag_get_ranges('sel')
    data = data.encode('utf-8')
    exc(data, env)
    area.clear_selection()

def set_target(area):
    area.active()
    set_status_msg('Target set !')

install = lambda area: area.install((1, '<Key-semicolon>', lambda event: exec_cmd(event.widget, ENV)), 
           (1, '<Control-e>', lambda event: exec_region(event.widget, DEV)),
           (1, '<Control-E>', lambda event: set_target(event.widget)),
           (1, '<Key-E>', lambda event: exec_region(event.widget, ENV)))














