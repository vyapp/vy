from vyapp.app import root

def update(area):
    """
    It is used to update the mode status bar 
    """
    area.hook(-1, '<FocusIn>', lambda event: root.status.set_mode(area.id))
    area.hook(-1, '<<Chmode>>', lambda event: root.status.set_mode(area.id))

def install(area):
    area.install((-1, '<FocusIn>', lambda event: update(event.widget)))

