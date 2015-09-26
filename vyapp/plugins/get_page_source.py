import sys
import urllib2

def install(area):
    def get_url_clipboard_source():
        opener            = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        req               = opener.open(area.clipboard_get()) 
        sys.stdout.write(req.read())

    area.hook('BETA', '<Key-m>', lambda event: get_url_clipboard_source())



