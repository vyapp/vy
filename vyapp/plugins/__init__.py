HANDLE  = []

# ENV is a dict holding plugins objects, like functions, classes etc.
# Plugins should install their handles in ENV.
ENV     = {}

def autoload(plugin, *args, **kwargs):
    HANDLE.append((plugin.install, args, kwargs))

def autocall(handle, *args, **kwargs):
    HANDLE.append((handle, args, kwargs))
            
def rmap(map):
    def shell(area):
        area.update_map(map)
    autocall(shell)



