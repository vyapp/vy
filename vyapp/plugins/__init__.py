from functools import wraps

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
    area = None
    def __init__(self, name=None):
        self.name = name

    def __call__(self, handle):
        name = self.name if self.name else handle.__name__
        @wraps(handle)
        def wrapper(*args, **kwargs):
            return handle(Command.area, *args, **kwargs)
        ENV[name] = wrapper
        return wrapper

    @classmethod
    def set_target(cls, area):
        cls.area = area

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