from subprocess import Popen, PIPE, STDOUT
from threading import Thread
from Queue import Queue, Empty
from os import environ, setsid, killpg

class Call(Thread):
    def __init__(self, *args):
        """
        """

        self.child = Popen(args, shell=0, stdout=PIPE, stdin=PIPE,  
                                            stderr=STDOUT,  env=environ)
        self.args  = args
        self.queue = Queue()
        self.stop  = False
        self.base  = []
        Thread.__init__(self)
        self.start()

    def send(self, data):
        """
        """

        data = data.encode('utf-8')
        self.child.stdin.write(data)

    def run(self):
        """
        """

        while not self.stop:
            self.queue.put_nowait(self.child.stdout.readline())
        self.child.wait()

    def update(self):
        """
        """

        while not self.queue.empty():
            self.dispatch(self.queue.get_nowait())
            
    def add_handle(self, handle):
        """
        """

        self.base.append(handle)

    def dispatch(self, data):
        """
        """

        for ind in self.base:
            ind(data)

    def die(self):
        """
        """
        self.stop = True
        self.child.kill()

def run_reactor(widget, reactor, timeout=200):
    def loop():
        widget.after(timeout, loop)               
        reactor.update()    
    widget.after(timeout, loop)               





