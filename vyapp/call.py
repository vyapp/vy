from subprocess import Popen, PIPE, STDOUT
from threading import Thread
from Queue import Queue, Empty
from os import environ, setsid, killpg

TIMEOUT = 200
    
class Call(Thread):
    def __init__(self, *args):
        Thread.__init__(self)
        self.child = Popen(args, shell=0, stdout=PIPE, stdin=PIPE,  
                                            stderr=STDOUT,  env=environ)
        self.queue = Queue()
        self.start()
        self.stop = False
        self.base = []

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
                self.dispatch(data)
                
    def add_handle(self, handle):
        self.base.append(handle)

    def dispatch(self, data):
        for ind in self.base:
            ind(data)

    def die(self):
        self.stop = True
        self.child.kill()

def run_reactor(widget, reactor, timeout=200):
    def loop():
        widget.after(timeout, loop)               
        reactor.update()    
    widget.after(timeout, loop)               



