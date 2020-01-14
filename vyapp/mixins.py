class IdleEvent:
    def __init__(self, widget):
        self.widget.bind('<<Data>>', self.dispatch_idle, add=True)
        self.widget  = widget
        self.timeout = 400
        self.funcid  = ''

    def dispatch_idle(self, event):
        # Make sure self.funcid is initialized before calling after_cancel.
        # The idea here it is to have <<idle>> spawned once when the user
        # stopped typing.

        if self.funcid:
            self.widget.after_cancel(self.funcid)
        self.funcid = self.widget.after(self.timeout, 
        lambda: self.widget.event_generate('<<Idle>>'))

class Echo:
    """

    """

    def __init__(self, area):
        self.area = area
        self.bind('<BackSpace>', self.on_backspace)
        self.bind('<Key>', self.dispatch)

    def dispatch(self, event):
        if event.char:  
            self.on_char(event.char)

    def on_char(self, char):
        self.area.insert('insert', char)

    def on_backspace(self, event):
        self.area.delete('insert -1c', 'insert')
        self.on_delete(event)

    def on_delete(self, event):
        pass

class DataEvent:
    def __init__(self, widget):
        self.widget = widget
        self.widget.bind('<Key>', self.dispatch_data, add=True)

    def dispatch_data(self, event):
        if event.char:
            self.widget.event_generate('<<Data>>')

