INSTALL = []
HANDLE  = []

def autoload(plugin, *args, **kwargs):
    INSTALL.append((plugin, args, kwargs))

def autocall(handle, *args, **kwargs):
    HANDLE.append((handle, args, kwargs))
            



