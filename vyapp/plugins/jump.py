"""

"""

def jump_next_mode(area):
    area.chmode(11)

def jump_back_mode(area):
    area.chmode(10)

def jump_next(area, char):
    index = area.search(char, 'insert', stopindex='end')
    if not index: return
    area.mark_set('insert', area.index('%s +1c' % index))
    area.see('insert')

def jump_back(area, char):
    index = area.search(char, 'insert', stopindex='1.0', backwards=True)
    if not index: return
    area.mark_set('insert', index)
    area.see('insert')

def install(area):
        area.add_mode(10)
        area.add_mode(11)

        INSTALL = [(1, '<Key-v>', lambda event: jump_next_mode(event.widget)), 
                   (1, '<Key-c>', lambda event: jump_back_mode(event.widget))]

        KEYS = {
                'apostrophe':"'", 
                '1':'1', 
                '2':'2', 
                '3':'3', 
                '4':'4',
                '5':'5',
                '6':'6',
                '7':'7',
                '8':'8',
                '9':'9',
                '0':'0',
                'minus':'-',
                'equal':'=',
                'q':'q',
                'w':'w',
                'e':'e',
                'r':'r',
                't':'t',
                'y':'y',
                'u':'u',
                'i':'i',
                'o':'o',
                'p':'p',
                'bracketleft':'[',
                'a':'a',
                's':'s',
                'd':'d',
                'f':'f',
                'g':'g',
                'h':'h',
                'j':'j',
                'k':'k',
                'l':'l',
                'asciitilde':'~',
                'bracketright':']',
                'z':'z',
                'x':'x',
                'c':'c',
                'v':'v',
                'b':'b',
                'n':'n',
                'm':'m',
                'comma':',',
                'period':'.',
                'semicolon':';',
                'slash':'/',
                'exclam':'!',
                'at':'@',
                'numbersign':'#',
                'dollar':'$',
                'percent':'%',
                'ampersand':'&',
                'asterisk':'*',
                'parenleft':'(',
                'parenright':')',
                'underscore':'_',
                'plus':'+',
                'Q':'Q',
                'W':'W',
                'E':'E',
                'R':'R',
                'T':'T',
                'Y':'Y',
                'U':'U',
                'I':'I',
                'O':'O',
                'P':'P',
                'grave':'`',
                'braceleft':'{',
                'A':'A',
                'S':'S',
                'D':'D',
                'F':'F',
                'G':'G',
                'H':'H',
                'J':'J',
                'K':'K',
                'L':'L',
                'Ccedilla':'Ç',
                'asciicircum':'^',
                'braceright':'}',
                'bar':'|',
                'Z':'Z',
                'X':'X',
                'C':'C',
                'V':'V',
                'B':'B',
                'N':'N',
                'M':'M',
                'less':'<',
                'greater':'>',
                'colon':':',
                'question':'?',
                'backslash':'\\'

                }
            
        for key, char in KEYS.iteritems():
            area.hook(10, '<Key-%s>' % key, lambda event, char=char: jump_back(event.widget, char))

        for key, char in KEYS.iteritems():
            area.hook(11, '<Key-%s>' % key, lambda event, char=char: jump_next(event.widget, char))

        area.install(*INSTALL)









