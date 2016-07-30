"""

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi

ENV['cpsel']  = lambda sep='\n': AreaVi.ACTIVE.cpsel(sep)
ENV['ctsel']  = lambda sep='\n': AreaVi.ACTIVE.ctsel(sep)
ENV['chmode'] = lambda id: AreaVi.ACTIVE.chmode(id)

