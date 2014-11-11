
class Rcp(object):
    """
    Record cursor position.
    """
    def __init__(self, area):
        START        = (1,0)
        self.area    = area
        self.record  = [START] * 3
        self.index   = 0
        self.count   = 0

        self.INSTALL = [(1, '<apostrophe>', lambda event: self.go()), 
                        (1, '<quotedbl>', lambda event: self.save())]

        area.install(*self.INSTALL)

    def save(self):
        # The actual index is the last mark created position.
        self.record[self.count] = self.area.indcur()
        self.index              = self.count
        self.count              = (self.count + 1) % len(self.record)

    def go(self):
        # It makes the index periodic. 

        try: 
            coord = self.record[self.index]
        except: pass
        else: self.area.setcur(*coord)

        try:
            self.index = (self.index + 1) % len(self.record)
        except ZeroDivisionError: pass


install = Rcp






