INSTALL = []
HANDLE  = []

# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
ENV     = {}

def autoload(plugin, *args, **kwargs):
    INSTALL.append((plugin, args, kwargs))

def autocall(handle, *args, **kwargs):
    HANDLE.append((handle, args, kwargs))
            




