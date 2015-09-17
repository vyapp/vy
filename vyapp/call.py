from subprocess import Popen, PIPE, STDOUT
from threading import Thread
from Queue import Queue, Empty
from os import environ, setsid, killpg

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
