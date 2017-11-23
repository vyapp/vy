##############################################################################
tee >(stdbuf -o 0 python -i)

##############################################################################
# pychecker.

from re import findall
regex = '(.+?):([0-9]+):?([0-9]*):(.+)'
findall(regex, 'file1.py:4:6: invalid syntax')
findall(regex, "file0.py:1: 'file1' imported but unused")

findall('(a+)(b+)', 'aabbb\naaaabbb')

from re import findall
regex = '(.+?):([0-9]+):?[0-9]*:(.+)'
findall(regex, 'file1.py:4:6: invalid syntax')
findall(regex, "file0.py:1: 'file1' imported but unused")

findall('(a+)(b+)', 'aabbb\naaaabbb')

##############################################################################
import re
REGSTR = '\(Pdb\) Deleted breakpoint (?P<index>[0-9]+)(?P<foo>a)'
regex = re.search(REGSTR, '(Pdb) Deleted breakpoint 11a')
groups = ('index', )
regex.group(*groups)
regex.groups('index')
##############################################################################
import re
REGSTR = '\> (.+)\(([0-9]+)\)(.+)'
regex = re.search(REGSTR, 
'(Pdb) > /home/tau/tests/pyflakes/file0.py(2)<module>()')

regex.groups()
regex.group(0)
##############################################################################
def func(a, b):
    print(a, b)

s = '12'
func(*s)
##############################################################################

def get_sentinel_file(path, filename):
    """
    """

    tmp = path
    while True:
        tmp = dirname(tmp)
        if exists(join(tmp, filename)):
            return tmp
        elif tmp == dirname(tmp):
            return path
        path = tmp

##############################################################################

from pygments.token import Comment, Token, Keyword, String
Comment.split()
Comment
Comment is Token.Comment

x = {
        Comment:1
    }

x[Token.Comment]
Keyword.Declaration.split()

from pygments.styles import get_style_by_name
from pygments.style import Style
Style.styles
x=get_style_by_name('colorful')

x.styles
dir(x)
dir(x)

arr = [1, 2, 3]
reversed(arr)
Style.background_color
Style.default_style
dir(Style)
String.split()
x = {Token.Literal.String.Single:2}
x[String.Single]
String.Single.split()
x = getattr(Style, 'default_style', {})
x
##############################################################################
#parse #pygment #style #token #value
from re import search
reg = search('bg\:(?P<bg>.+) ?', 'nobold bg:#434')

reg.group('fee')
dir(reg)
reg.groupdict()
from pygments.lexers import *
from pygments.lexers import get_lexer_for_filename 

help(search)
##############################################################################
from re import *
H3 = '>>> %s has left %s :%s <<<\n' 
reg3 = '(\>\>\>) (.+) (has left) (.+) :(.+) (<<<)'

e = match(reg3, H3)
e.group(1)
e.group(2)
e.group(3)
e.group(4)
e.group(5)
e.group(6)

tagnize(reg3, H3 % fields)

def tagnize(regex, data):
    pass

def test():
    print 'foo'

x= {1:'a'}
dir(x)
help(x.setdefault)
x.setdefault(1, test())
##############################################################################
# irc, pygments, lexer, irssi.

from pygments.lexers.textfmts import IrcLogsLexer

dir(IrcLogsLexer)
IrcLogsLexer.aliases
##############################################################################

from Tkinter import *
root = Tk()

def a(e):
    print 'A'

def b(e):
    print 'B'


# just handle a gets called, not sure why
# when it should get a and b called.
root.event_add('<<A>>', '<Key-u>')
root.event_add('<<B>>', '<Key-u>')

root.bind('<<A>>', a)
root.bind('<<B>>', b)

##############################################################################
import mimetypes
mimetypes.add_type('application/x-golang', '.go')
mimetypes.add_type('application/x-golang', '.goo')

mimetypes.guess_extension('application/x-golang')
mimetypes.guess_all_extensions('application/x-golang')
mimetypes.guess_type('f.go')
mimetypes.add_type('application/x-golang', '.c')
mimetypes.guess_type('f.c')

mimetypes.guess_type('fee.rb')
mimetypes.guess_type('f.py')
mimetypes.guess_type('f.c')
mimetypes.guess_type('f.cpp')
mimetypes.guess_type('fe.go')
mimetypes.guess_type('fee.js')
mimetypes.guess_type('fee.html')
mimetypes.guess_type('f.oeirueoriu')
mimetypes.guess_extension('application/x-ruby')
mimetypes.guess_extension('application/x-python')
mimetypes.types_map
mimetypes.types
mimetypes.knownfiles
dir(mimetypes)
##############################################################################
# python-magic, guessing file type on content.
import magic

magic.from_file("/home/tau/projects/morphology-code/catch-offset", mime=True)
##############################################################################
# filemagic guessing file type on content.
import magic

with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
    m.id_filename("/home/tau/projects/morphology-code/catch-offset")
##############################################################################
from os.path import splitext
splitext('foo.py')
splitext('foo')
##############################################################################
from Tkinter import *
root = Tk()
root.configure(background='black')

'.py'.strip('.')
from os.path import splitext
'ee.py'
##############################################################################
import sys

class MyStdin(object):
    def __init__(self):
        self.default = sys.stdin
        sys.stdin    = self
    def read(self, data):
        print 'Data', data
        self.default.read(data)        
    def write(self, data):
        print 'Data', data
        self.default.write(data)        
    def readline(self):
        data = self.default.readline()        
        print 'The data:', data
        return data
    def readlines(self):
        data = self.default.readlines()        
        print 'The data:', data
        return data

n = MyStdin()
print 'ee'
sys.stdin
dir(n.default)
s = raw_input()
dir(sys.stdin)
##############################################################################
from pygments.lexers import *
from pygments.lexers import get_lexer_for_filename 
lexer = get_lexer_for_filename('py.py')

data = '''
s=""" oo"""'''

for pos, token, value in lexer.get_tokens_unprocessed(data):
    print(pos, token, value)


' o'

String.Double is String.Doc
isinstance(String.Doc, (String.Double,))

from pygments.token import String
from pygments.styles.colorful import ColorfulStyle
from vyapp.plugins.syntax.styles.vy import VyStyle
s = ColorfulStyle()
ColorfulStyle.background_color
ColorfulStyle.style_for_token(String)
VyStyle.style_for_token(String.Doc)

s.style_for_token
ColorfulStyle.style_for_token(String.Doc)
ColorfulStyle.styles
quit()

def foo(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)


foo(2, 3, 3, c=2)
foo(2, 3, 3, b=2)

a = {'a': 1, 'b': 2}
b = {'a':1}

sa = set(a.items())
sb = set(b.items())
sa
sb
sb.issubset((('a', 1),))
sb.issubset({'a':1})
('a', 1) in a

m = memoryview((('a', 1), ('b', 2)))

sb
sa.issuperset(sb)
sb.issubset(set(())
su = set()
su.issubset(sb)

##############################################################################
# get, keysym_num, keycode, tkinter, event.

from tkinter import *
root = Tk()
frame = Frame(root)
text = Text(frame)
text.pack()
frame.pack()
text.insert('1.0', 'some text')
text.tag_add('test', '1.0', '1.4')
text.tag_names('1.3')
text.insert('2.0', 'some text')
text.tag_add('cool', '2.0', '2.4')
text.tag_names('2.3')

from os.path import exists, dirname, join

def get_sentinel_file(path, filename):
    tmp = path
    while True:
        tmp = dirname(tmp)
        if exists(join(tmp, filename)):
            return tmp
        elif tmp == dirname(tmp):
            return path
        path = tmp


def exp(a, b):
    prod = a
    for ind in range(0, b):
        prod = prod * prod
    return prod

exp(2, 2)
##############################################################################
from pygments.lexers import guess_lexer, guess_lexer_for_filename, get_lexer_for_filename
guess_lexer('#!/usr/bin/python\nprint "Hello World!"')
guess_lexer('print "Hello World!"')
guess_lexer_for_filename('test', '#!/usr/bin/python\nprint "Hello World!"')
get_lexer_for_filename('tt', '#!/usr/bin/python\nprint "Hello World!"')
help(guess_lexer_for_filename)
help(get_lexer_for_filename)
help(guess_lexer)
lexer = guess_lexer('#!/usr/bin/python\nprint "Hello World!"')
lexer.name
dir(lexer)
lexer.mimetypes
lexer = guess_lexer_for_filename('test.java', '')
lexer.name
##############################################################################
# os path.
import os.path
os.path.splitext('oo')

try:
    raise IndexError
except IndexError:
    raise KeyError
except KeyError:
    print('cool')




