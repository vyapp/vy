from traceback import print_exc as debug
from vyapp.app import root
from vyapp.areavi import AreaVi
import sys


def execute(handle, *args, **kwargs):
    """

    """
    try:
        val = handle(*args, **kwargs)
    except Exception:
        debug()
    else:
        return val

def burn(chain, event, opt = None):
    """

    """

    for ind in chain:
        val = execute(ind, event)

        if val == True:    opt = True
        elif val == False: opt = False

    return opt

def exec_quiet(handle, *args, **kwargs):
    try:
        val = handle(*args, **kwargs)
    except Exception:
        pass
    else:
        return val

def exc(data, env):
    """

    """
    import sys
    # It has to be set before because
    # if some data code catches an exception
    # then prints use print_exc it will go to
    # sys.__stderr__.

    tmp        = sys.stderr
    sys.stderr = sys.stdout

    try:
    
        exec(data, env)
    except Exception:
        debug()
    finally:
        sys.stderr = tmp


def get_all_areavi_instances(wid=root):
    for ind in wid.winfo_children():
        if isinstance(ind, AreaVi):
            yield ind
        else:
            for ind in get_all_areavi_instances(ind):
                yield ind

def get_opened_files():
    map = dict()
    for ind in get_all_areavi_instances():
        map[ind.filename] = ind
    return map

def get_area_tab_index(area):
    return area.master.master.master

def set_line(area, line):
    from vyapp.app import root
    import sys
    sys.stderr.write(area.filename + '\n')
    root.note.select(get_area_tab_index(area))
    area.focus()
    area.inset('%s.0' % int(line))
    area.seecur()


def find_on_all(chunk):
    for indi in get_all_areavi_instances():
        it = indi.find(chunk, '1.0', 'end')

        for indj in it:
            yield indj[0]

def set_status_msg(msg):
    from vyapp.app import root
    root.status.set_msg(msg)

def set_status_line(line):
    from vyapp.app import root
    root.status.set_line(line)

def set_status_col(col):
    from vyapp.app import root
    root.status.set_column(col)

def set_status_mode(mode):
    from vyapp.app import root
    root.status.set_mode(mode)


def consume_iter(iterator, time=1):
    def cave():
        from vyapp.app import root
        try:
            iterator.next()
        except Exception:
            pass
        else:    
            root.after(time, cave)

    cave()









