HANDLE  = []

# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
ENV     = {}

def autoload(plugin, *args, **kwargs):
    HANDLE.append((plugin.install, args, kwargs))

def autocall(handle, *args, **kwargs):
    HANDLE.append((handle, args, kwargs))
            
def mapset(namespace, map):
    HANDLE.append((lambda area: 
    area.update_map(namespace, map), (), {}))





