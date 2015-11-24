"""

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

ENV['find'] = lambda *args, **kwargs: AreaVi.ACTIVE.tag_add_found('sel', AreaVi.ACTIVE.find(*args, **kwargs))
ENV['sub'] = lambda *args, **kwargs: AreaVi.ACTIVE.replace_all(*args, **kwargs)
ENV['get'] = lambda *args: AreaVi.ACTIVE.get(*args)


