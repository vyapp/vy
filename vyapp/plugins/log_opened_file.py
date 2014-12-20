""" This file implements a plugin that logs all opened files and saved
files into a filename specified."""



import os
    
def log(area, logfile):
    with open(logfile, 'a+') as fd:
        fd.write('%s\n' % os.path.abspath(area.filename))


def install(area, logfile):
    area.install((-1, '<<SaveData>>', lambda event: log(event.widget, logfile)),
                 (-1, '<<LoadData>>', lambda event: log(event.widget, logfile)))



