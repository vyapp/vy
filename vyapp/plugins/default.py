"""

"""



# It may be possible to delete the bindings that echo chars over the screen.
# So i dont need to emulate this event. I could keep 'Text' in the bindtags order.
INSTALL = [(-1, '<ButtonPress>', lambda event: event.widget.focus()),
           (-1, '<<LoadData>>', lambda event: event.widget.go_text_start())]

def install(area):
    area.install(*INSTALL)







