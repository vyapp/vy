"""
Mode: Specified modes(See plugin installation).
Event: <KeyPress-apostrophe>
Description: Switch to one of the modes specified in modes.

Mode: Specified in target_mode(See plugin installation)
Event: <KeyRelease-apostrophe>
Description: Goes back to the previous mode.
"""

class ToggleMode(object):    
    def __init__(self, area, target_mode=1, modes=[2, 3, 4, 5, 6, 7]):
        for ind in modes:
            area.hook(ind, '<KeyPress-apostrophe>', lambda event: self.switch_standard_mode(event.widget))
        area.hook(target_mode, '<KeyRelease-apostrophe>', lambda event: self.switch_previous_mode(event.widget))

        # It seems tkinter generates KeyRelease events together with KeyPress events.
        self.id = 1
        self.target_mode = target_mode

    def switch_standard_mode(self, area):
        self.id = area.id
        area.chmode(self.target_mode)

    def switch_previous_mode(self, area):
        area.chmode(self.id)

install = ToggleMode



