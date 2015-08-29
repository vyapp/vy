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


