from vyapp.app import root

def install(area):
    area.hook(-1, '<FocusIn>', lambda event: root.status.set_mode(area.id))
    area.hook(-1, '<<Chmode>>', lambda event: root.status.set_mode(area.id))


