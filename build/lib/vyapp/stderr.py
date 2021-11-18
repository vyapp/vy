from traceback import format_exc
import logging
import sys

QUIET  = 100
logger = logging.getLogger()

def xhook(exctype, value, tb):
    logger.exception('', exc_info=(exctype, value, tb))

def printd(*args):
    logger.debug(' '.join(map(str, args)))

sys.excepthook = xhook
c_handler      = logging.StreamHandler()
logger.setLevel(logging.DEBUG)
logger.addHandler(c_handler)
