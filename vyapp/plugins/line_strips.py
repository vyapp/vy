from re import sub

from vyapp.plugins import ENV
from vyapp.areavi import AreaVi
from re import escape

def strip(chars=' '):
    """
    Strip chars off the beginning of all selected lines.
    if chars is not given it removes spaces.
    """

    AreaVi.ACTIVE.replace_ranges('sel', 
    '^[%s]+' % escape(chars), '')

def rstrip(chars=' '):
    """
    Strip chars off the beginning of all selected lines.
    if chars is not given it removes spaces.
    """

    AreaVi.ACTIVE.replace_ranges('sel', 
    '[%s]+$' % escape(chars), '')

ENV['strip']  = strip
ENV['rstrip'] = rstrip


