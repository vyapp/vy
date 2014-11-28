class KeyEvent(object):    
    def __init__(self, area, target_mode=1, modes=[2, 3, 4, 5, 6, 7]):
        for ind in modes:
            area.hook(ind, '<KeyPress-apostrophe>', lambda event: self.switch_standard_mode(event.widget))
        area.hook(target_mode, '<KeyRelease-apostrophe>', lambda event: self.switch_previous_mode(event.widget))

        # It seems tkinter generates KeyRelease events together with KeyPress events.
        self.target_mode = target_mode

    def switch_standard_mode(self, area):
        self.id = area.id
        area.chmode(self.target_mode)

    def switch_previous_mode(self, area):
        area.chmode(self.id)

install = ToggleMode


