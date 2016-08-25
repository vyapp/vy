"""

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.plugins import autoload
from vyapp.app import root

def load(plugin, *args, **kwargs):
    autoload(plugin, *args, **kwargs)

    for ind in AreaVi.areavi_widgets(root):
        plugin.install(ind, *args, **kwargs)

    root.status.set_msg('Plugin loaded!')

ENV['load'] = load











