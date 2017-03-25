from vyapp.app import root

def install(area):
    area.install('mode-status', (-1, '<FocusIn>', lambda event: root.status.set_mode(area.id)),
    (-1, '<<Chmode>>', lambda event: root.status.set_mode(area.id)))



