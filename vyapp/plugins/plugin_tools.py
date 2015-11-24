"""

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.plugins import autoload
from vyapp.tools import set_status_msg

def load(plugin, *args, **kwargs):
    from vyapp.app import root
    autoload(plugin, *args, **kwargs)

    for ind in AreaVi.get_all_areavi_instances(root):
        plugin.install(ind, *args, **kwargs)

    set_status_msg('Plugin loaded!')

ENV['load'] = load








