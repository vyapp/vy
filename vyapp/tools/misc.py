from traceback import print_exc as debug
import sys

class Stdout(object):    
    TAG_CODE = 'code'
    def __init__(self, area):
        # I am selecting from the beginning to the start of a line
        # below to the insert cursor so i add a line
        # to the end of the line below to the cursor then
        # the code_mark will be after the sel mark.
        # this was a pain in the ass to notice.
        self.area = area
        self.area.mark_set('code_mark', 'insert')

    def write(self, data):
        index0 = self.area.index('code_mark')
        self.area.insert('code_mark', data)
        self.area.tag_add(self.TAG_CODE, index0, 'code_mark')
 
        self.area.see('insert')

    def __eq__(self, other):
        return self.area == other

class Transmitter(object):
    def __init__(self, default):
        self.base    = [default]
        self.default = default

    def restore(self):
        del self.base[:]
        self.base.append(self.default)

    def append(self, fd):
        self.base.append(fd)

    def remove(self, fd):
        self.base.remove(fd)

    def write(self, data):
        for ind in self.base: 
            ind.write(data)
            
def echo(data): 
    """

    """

    sys.stdout.write(data)    

def get_file_extension(filename):
    """

    """

    try:
        ext = filename.rsplit('.')[1]
    except IndexError:
        pass
    else:
        return ext

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


def get_all_areavi_instances():
    from vyapp.app import root
    from vyapp.areavi import AreaVi

    lst = []
    for indi in root.note.winfo_children():
        for indj in indi.winfo_children():
            for indz in indj.winfo_children():
                for indn in indz.winfo_children():
                    if isinstance(indn, AreaVi):
                       lst.append(indn)
    return lst

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


def run_vyrc(area):
    from os.path import expanduser, join
    ENV = dict()
    dir = expanduser('~')
    dir = join(dir, '.vy')
    rc  = join(dir, 'vyrc')

    execfile(rc, ENV)

    for ind in ENV['INSTALL']:
        ind[0].install(area, *ind[1:])

    for ind in ENV['HANDLE']:
        ind(area)

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




