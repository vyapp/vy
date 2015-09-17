from vyapp.call import Call
from vyapp.ask import Ask
from vyapp.tools import set_status_msg
import shlex

class Output(Call):
    TIMEOUT = 200
    def __init__(self, area, *args):
        Call.__init__(self, *args)
        self.area = area
        area.after(self.TIMEOUT, self.update)

    def update(self):
        Call.update(self)
        self.area.after(self.TIMEOUT, self.update)


    def handle_read(self, data):
        self.area.insert('end', data)
        self.area.mark_set('insert', 'end')
        self.area.see('end')

class Pool(object):
    def __init__(self):
        self.base = []

    def create(self, area, *args):
        call = Output(area, *args)
        self.base.append(call)
        return call

    def send(self, data):
        for ind in self.base:
            ind.send(data)

class Command(object):
    def __init__(self, area):
        area.install(('NORMAL', '<Control-F4>', lambda event: self.start_process(event.widget)),
                     ('NORMAL', '<F9>', lambda event: self.dump_line(event.widget)))


        self.pool = Pool()

    def start_process(self, area):
        args   = Ask(area)
        o_area = area.master.master.create()
        args   = shlex.split(args.data)
        call   = self.pool.create(o_area, *args)
        o_area.hook(-1, '<Destroy>', lambda event, call=call: call.die())
        area.hook(-1, '<Destroy>', lambda event, call=call: call.die())

    def dump_line(self, area):
        line = area.get('insert linestart', 'insert +1l linestart')
        self.pool.send(line)

install = Command


