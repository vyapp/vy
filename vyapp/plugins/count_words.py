from vyapp.areavi import AreaVi
from vyapp.tools import set_status_msg
from vyapp.plugins import ENV
from re import findall

def cw():
    area = AreaVi.ACTIVE

    data = area.get('1.0', 'end')
    set_status_msg('Count of words:%s' % len(findall('\W+', data)))

ENV['cw'] = cw

