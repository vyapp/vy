#! /usr/bin/env python
import sys
import time
import os

def stop():
    sys.stdout.flush()    
    sys.stdin.readline()

def head(frame, event, arg):
    # If the file isn't to be traced ...
    if not frame.f_code.co_filename in sys.argv:
        return

    stop()
    
    if event == 'call':
        print 'CALL %s %s %s %s' % (frame.f_code.co_name,
                                 frame.f_lineno,
                                 frame.f_code.co_filename, frame.f_locals)
        return head
    elif event == 'exception':
        print 'EXCEPTION %s %s %s %s' % (frame.f_code.co_name,
                                         frame.f_lineno,
                                         frame.f_code.co_filename, arg)
    elif event == 'return':
        print 'RETURN %s %s %s %s' % (frame.f_code.co_name,
                                      frame.f_lineno,
                                      frame.f_code.co_filename, arg)
    elif event == 'line':
        print 'LINE %s %s %s %s' % (frame.f_code.co_name,
                                    frame.f_lineno, 
                                    frame.f_code.co_filename, frame.f_locals)
    

# We need to add the target files to the path. Otherwise
# if it imports some file in its folder we get an exception.
# Because it can't find in the path for where to import the module.

folders = set()
for ind in sys.argv:
    folders.add(os.path.dirname(ind))
sys.path.extend(folders)
# It has to be set after setting the path. Otherwise we get a bug.


sys.settrace(head)
execfile(sys.argv[1], {})
quit()
















