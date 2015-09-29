"""

"""

from untwisted.plugins.irc import Irc, send_cmd
from untwisted.network import Spin, xmap, spawn
from untwisted.utils.stdio import Client, Stdin, Stdout, CONNECT, CONNECT_ERR, LOAD, CLOSE
from untwisted.utils.shrug import *
from vyapp.plugins import ENV
from vyapp.ask import Ask
from vyapp.app import root

def on_privmsg(con, nick, user, host, target, msg):
    spawn(con, 'PRIVMSG->%s' % target.lower(), nick, user, host, msg)
    spawn(con, 'PRIVMSG->%s' % nick.lower(), target, user, host, msg)

def on_join(con, nick, user, host, chan):
    if con.nick == nick: 
        spawn(con, 'MEJOIN', chan)
    else:
        spawn(con, 'JOIN->%s' % chan, nick, 
              user, host)

def on_353(con, prefix, nick, mode, chan, peers):
    peers = peers.split(' ')
    spawn(con, '353->%s' % chan, prefix, 
          nick, mode, peers)

def on_part(con, nick, user, host, chan):
    if con.nick == nick: 
        spawn(con, 'PART->%s->MEPART' % chan, chan)
    else:
        spawn(con, 'PART->%s' % chan, nick, 
              user, host)

def on_001(con, address, nick, *args):
    con.nick = nick
    print 'the nick is', nick

class IrcMode(object):
    def __init__(self, area):
        area.add_mode('IRC')

        area.install(('IRC', '<Control-s>', lambda event: self.connect_server(event.widget)))

    def connect_server(self, area):
        ask        = Ask(area)
        con        = Spin()
        addr, port = ask.data.split(':')
        port       = int(port)
        con.connect_ex((addr, port))
        Client(con)
        xmap(con, CONNECT, lambda con: self.set_up_con(con, area))
        xmap(con, CONNECT_ERR, self.on_connect_err)
        area.hook('IRC', '<Control-e>', lambda event: self.send_cmd(event.widget, con))
        area.mark_set('addr', '1.0')
        xmap(con, FOUND, lambda con, data: area.insert('addr', '%s\n' % data))

    def send_cmd(self, area, con):
        ask = Ask(area)
        send_cmd(con, ask.data)

    def set_up_con(self, con, area):
        Stdin(con)
        Stdout(con)
        Shrug(con)
        Irc(con)
        xmap(con, '001', on_001)
        xmap(con, 'PRIVMSG', on_privmsg)
        xmap(con, 'JOIN', on_join)
        xmap(con, 'PART', on_part)
        xmap(con, '353', on_353)
        xmap(con, 'MEJOIN', lambda con, chan: self.create_channel(area, con, chan))

    def create_channel(self, area, con, chan):
        area.mark_set(chan, 'end')
        area.insert('end', '#' * 30 + '\n')
        area.insert(chan, '>')
        xmap(con, 'PRIVMSG', lambda *args: self.feed(area, *args))

    def feed(self, area, con, nick, user, host, target, msg):
        area.insert(target, msg)

    def on_connect_err(self, con, err):
        print 'not connected'

def ircmode():
    from vyapp.areavi import AreaVi
    AreaVi.ACTIVE.chmode('IRC')
    

ENV['ircmode'] = ircmode
install        = IrcMode
