from untwisted.event import LOAD, CLOSE
from vyapp.app import root

import signal

class BaseSpawn(object):
    def __init__(self, cmd, input, output):
        self.cmd    = cmd
        self.input  = input
        self.output = output
        self.install_events()

    def install_events(self):
        """

        """
        self.input.hook('spawn', 'NORMAL', '<Control-c>', 
        lambda event: self.dump_signal(signal.SIGINT), add=False)

        self.input.hook('spawn', 'NORMAL', '<Control-backslash>', 
        lambda event: self.dump_signal(signal.SIGQUIT), add=False)

        # When one of the AreaVi instances are destroyed then
        # the process is killed.

        self.output.hook('spawn', -1, '<Destroy>', 
        lambda event: self.terminate_process())

        self.input.hook('spawn', -1, '<Destroy>', 
        lambda event: self.terminate_process())

        self.input.hook('spawn', 'NORMAL', '<F1>', 
        lambda event: self.dump_line(), add=False)

        self.input.hook('spawn', 'INSERT', '<F1>', 
        lambda event: self.dump_line(), add=False)

        root.status.set_msg('%s -> %s' % (self.input.filename, 
        self.output.filename))

    def dump_signal(self, num):
        pass

    def terminate_process(self):
        pass

    def dump_line(self):
        pass

    def handle_close(self, expect):
        pass







