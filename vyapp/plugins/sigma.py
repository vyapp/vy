def clip_ph(area):
    """ Sends filename path to clipboard. """
    area.clipboard_clear()
    area.clipboard_append(area.filename)


def install(area):
    area.install(('ALPHA', '<Key-u>', lambda event: clip_ph(event.widget)))









