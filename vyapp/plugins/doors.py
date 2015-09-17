from subprocess import Popen, PIPE, STDOUT
from threading import Thread
from Queue import Queue, Empty
from vyapp.ask import Ask
from vyapp.tools import set_status_msg
from os import environ, setsid, killpg
import shlex

class Call(Thread):
    def __init__(self, *args):
        Thread.__init__(self)
        self.child = Popen(args, shell=0, stdout=PIPE, stdin=PIPE,  
                                            stderr=STDOUT,  env=environ)
        self.queue = Queue()
        self.start()
        self.stop = False

    def send(self, data):
        self.child.stdin.write(data.encode('utf-8'))

    def run(self):
        while not self.stop:
            data = self.child.stdout.readline()
            self.queue.put_nowait(data)
    
    def update(self):
        while True:
            try:
                data = self.queue.get_nowait()
            except Empty:
                break
            else:
                self.handle_read(data)
                
    def handle_read(self, data):
        pass

    def die(self):
        self.stop = True
        self.child.kill()

class  Output(Call):
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

class Command(object):
    def __init__(self, area):
        area.install(('NORMAL', '<Control-F4>', lambda event: self.create_horizontal_area(event.widget)),
                     ('NORMAL', '<F9>', lambda event: self.dump_line(event.widget)))

    def create_horizontal_area(self, area):
        args = Ask(area)
        h_area = area.master.master.create()
        h_area.hook(-1, '<Destroy>', lambda event: self.call.die())
        area.hook(-1, '<Destroy>', lambda event: self.call.die())
        self.call = Output(h_area, *shlex.split(args.data))

    def dump_line(self, area):
        line = area.get('insert linestart', 'insert +1l linestart')
        self.call.send(line)

install = Command

