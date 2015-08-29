"""

"""

from vyapp.tools import exc, set_status_msg
from vyapp.ask import Ask
from vyapp.plugins import ENV

import sys

def exec_cmd(area, env):
    ask    = Ask(area)
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

install = lambda area: area.install(('NORMAL', '<Key-semicolon>', lambda event: exec_cmd(event.widget, ENV)), 
           ('NORMAL', '<Control-e>', lambda event: exec_region(event.widget, ENV)),
           ('NORMAL', '<Control-E>', lambda event: set_target(event.widget)))


















