import urllib
import urllib2

def post(data, lang, opt=False):
    opener            = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    lang_map = {
                    'c':'C',
                    'cpp':'C++',
                    'd':'D',
                    'hs':'Haskell',
                    'lua':'Lua',
                    'ocaml':'OCaml',
                    'php':'PHP',
                    'pl':'Perl',
                    'py':'Python',
                    'rb':'Ruby',
                    'scm':'Scheme',
                    'tcl':'Tcl'
               }


    head    = {
                    'code':data,
                    'lang':lang_map.get(lang, 'Plain Text'),
                    'submit':'Submit'
              }

    url         = 'http://codepad.org'
    head['run'] = opt
    pointer     = opener.open(url, urllib.urlencode(head))
    #output     = pointer.re()
    new_url     = pointer.geturl()

    return pointer, new_url

def CPPaste():
    import webbrowser
    from vyapp.tools.misc import get_file_extension
    from vyapp.areavi import AreaVi
    area = AreaVi.ACTIVE
    # The areavi in which the execute cmd even was 
    # issued from.
    data             = area.get('1.0', 'end')
    data             = data.encode('utf-8')
    ext              = get_file_extension(area.filename)
    pointer, new_url = post(data, ext, True)
    webbrowser.open(new_url)

from vyapp.app import ENV
ENV['CPPaste'] = CPPaste








