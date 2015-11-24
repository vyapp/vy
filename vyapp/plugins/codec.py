"""

"""

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from vyapp.tools import set_status_msg

def decode(name):
    try:
        AreaVi.ACTIVE.decode(name)
    except UnicodeDecodeError:
        set_status_msg('Failed! Charset %s' % name)
    
def charset(name):
    AreaVi.ACTIVE.charset = name
    set_status_msg('Charset %s set.' % name)

ENV['decode']  = decode
ENV['charset'] = charset

