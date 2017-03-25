from vyapp.tools import get_area_tab_index
from vyapp.app import root
from os.path import basename

def install(area):
    area.install('io-status', (-1, '<Escape>', lambda event: root.status.set_msg('')),
           (-1, '<<SaveData>>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<<LoadData>>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<<ClearData>>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<FocusIn>', lambda event: root.title('Vy %s' % event.widget.filename)),
           (-1, '<<SaveData>>', lambda event: root.note.tab(get_area_tab_index(event.widget), text=basename(event.widget.filename))),
           (-1, '<<LoadData>>', lambda event: root.note.tab(get_area_tab_index(event.widget), text=basename(event.widget.filename))),
           (-1, '<<ClearData>>', lambda event: root.note.tab(get_area_tab_index(event.widget), text=basename(event.widget.filename))),
           (-1, '<FocusIn>', lambda event: root.note.tab(root.note.select(), text=basename(event.widget.filename))))






