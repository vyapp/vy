from subprocess import Popen, STDOUT, PIPE, CalledProcessError
from vyapp.app import root
from re import findall

class HtmlChecker(object):
    def  __init__(self, area, path='tidy', 
        setup={'foreground': '#D6917A'}):

        # The path that tidy stays, in some
        # systems it may not be available in the
        # PATH variable.
        area.tag_config('(HTML_CHECKER_ERRORS)', **setup)
        area.tag_config('(HTML_CHECKER_COMMENT)', background='blue')

        self.area = area
        self.path = path
        area.install((-1, '<<LoadData>>', self.check),
        (-1, '<<SaveData>>', self.check))

    def check(self, event):
        self.area.delete_ranges('(HTML_CHECKER_COMMENT)')
        cmd  = [self.path, '-e', 
        '-quiet', self.area.filename]

        child = Popen(cmd, stdout=PIPE, stderr=STDOUT)
        output, error = child.communicate()
        
        regex = 'line ([0-9]+) column ([0-9]+) - (.+)'
        ranges = findall(regex, output)
        print ranges

        for line, col, error in ranges:
            self.area.tag_add('(HTML_CHECKER_ERRORS)', 
             '%s.0' % line, '%s.0 lineend' % line)
        
        if child.returncode:
            root.status.set_msg('Errors were found!')
        else:
            root.status.set_msg('Errors were found!')

install = HtmlChecker

