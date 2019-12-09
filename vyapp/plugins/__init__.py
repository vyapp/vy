from functools import wraps, update_wrapper
from vyapp.areavi import AreaVi

# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
HANDLE  = []
ENV     = {}

def autoload(plugin, *args, **kwargs):
    HANDLE.append((plugin.install, args, kwargs))

def autocall(handle, *args, **kwargs):
    HANDLE.append((handle, args, kwargs))
            
def mapset(namespace, map):
    HANDLE.append((lambda area: 
    area.update_map(namespace, map), (), {}))

class Command:
    def __init__(self, name=None):
        self.name = name

    def __call__(self, handle):
        name = self.name if self.name else handle.__name__
        @wraps(handle)
        def wrapper(*args, **kwargs):
            return handle(AreaVi.ACTIVE, *args, **kwargs)
        ENV[name] = wrapper
        return wrapper

# def command(name):
    # def wrapper0(handle):
        # nonlocal name
        # name = name if name else handle.__name__
        # @wraps(handle)
        # def wrapper1(*args, **kwargs):
            # handle(AreaVi.ACTIVE, *args, **kwargs)
        # ENV[name] = wrapper1
        # return wrapper1
    # return wrapper0