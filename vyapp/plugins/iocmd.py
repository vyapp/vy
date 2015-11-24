"""

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

ENV['ss'] = lambda filename: AreaVi.ACTIVE.save_data_as(filename)
ENV['lo'] = lambda filename: AreaVi.ACTIVE.load_data(filename)

