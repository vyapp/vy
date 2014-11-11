"""

"""

from vyapp.tools.misc import echo, get_all_areavi_instances
from vyapp.app import ENV
from vyapp.areavi import AreaVi
from vyapp.plugins import autoload

def count_all_words():
    area = AreaVi.ACTIVE

    data = area.get('1.0', 'end')
    echo('Count of words:%s' % data.count(' '))

def load(plugin, *args, **kwargs):
    autoload(plugin, *args, **kwargs)

    for ind in get_all_areavi_instances():
        plugin.install(ind, *args, **kwargs)


ENV['cw'] = count_all_words
ENV['ss'] = lambda filename: AreaVi.ACTIVE.save_data_as(filename)
ENV['lo'] = lambda filename: AreaVi.ACTIVE.load_data(filename)
ENV['get'] = lambda *args: AreaVi.ACTIVE.get(*args)
ENV['find'] = lambda *args, **kwargs: AreaVi.ACTIVE.tag_add_found('sel', AreaVi.ACTIVE.find(*args, **kwargs))
ENV['sub'] = lambda *args, **kwargs: AreaVi.ACTIVE.replace_all(*args, **kwargs)
ENV['load'] = load


