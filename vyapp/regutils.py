from re import split, escape

def build_regex(data, delim='.+'):
    """

    """

    data    = split(' +', data)
    pattern = ''
    for ind in xrange(0, len(data)-1):
        pattern = pattern + escape(data[ind]) + delim
    pattern = pattern + escape(data[-1])
    return pattern





