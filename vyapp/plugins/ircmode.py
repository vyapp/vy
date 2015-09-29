"""
Overview
========


Usage
=====

Key-Commands
============

"""

from untwisted.plugins.irc import Irc, send_cmd, send_msg
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

class IrcMode(object):
    def __init__(self, area):
        area.add_mode('IRC', opt=True)

        area.install(('IRC', '<Control-s>', lambda event: self.connect_server(event.widget)),
                     ('GAMMA', '<Key-i>', lambda event: event.widget.chmode('IRC')))

    def connect_server(self, area):
        ask        = Ask(area)
        con        = Spin()
        addr, port = ask.data.split(':')
        port       = int(port)
        con.connect_ex((addr, port))
        Client(con)

        xmap(con, CONNECT, lambda con: self.set_up_con(con, area))
        xmap(con, CONNECT_ERR, self.on_connect_err)


    def send_cmd(self, area, con):
        ask = Ask(area)
        send_cmd(con, ask.data)

    def set_up_con(self, con, area):
        Stdin(con)
        Stdout(con)
        Shrug(con)
        Irc(con)

        self.set_common_irc_handles(area, con)
        self.set_common_irc_commands(area, con)

    def create_channel(self, area, con, chan):
        area_chan = root.note.create(chan)
        area_chan.chmode('IRC')

        self.set_common_chan_commands(area_chan, con, chan)
        self.set_common_chan_handles(area_chan, con, chan)
    
    def set_common_irc_commands(self, area, con):
        area.hook('IRC', '<Control-e>', lambda event: self.send_cmd(event.widget, con))

    def set_common_irc_handles(self, area, con):
        l1 = lambda con, chan: self.create_channel(area, con, chan)
        l2 = lambda con, prefix, servaddr: send_cmd(con, 'PONG :%s' % servaddr)
        l3 = lambda con, data: area.insert('end', '%s\n' % data)

        xmap(con, '001', on_001)
        xmap(con, 'PRIVMSG', on_privmsg)
        xmap(con, 'JOIN', on_join)
        xmap(con, 'PART', on_part)
        xmap(con, '353', on_353)
        xmap(con, 'MEJOIN', l1)
        xmap(con, 'PING', l2)
        xmap(con, FOUND, l3)

    def set_common_chan_commands(self, area, con, chan):
        e1 = lambda event: self.send_chan_msg(event.widget, chan, con)
        e2 = lambda event: self.send_cmd(event.widget, con)

        area.hook('IRC', '<Return>', e1)
        area.hook('IRC', '<Control-e>', e2)

    def set_common_chan_handles(self, area, con, chan):
        l1 = lambda *args: self.on_privmsg(area, *args)
        l2 = lambda *args: self.on_332(area, *args)

        xmap(con, 'PRIVMSG->%s' % chan, l1)
        xmap(con, '332', l2)


    def on_part(self, area, *args):
        pass

    def send_chan_msg(self, area, chan, con):
        data = area.get('insert linestart', 'insert lineend')
        area.delete('insert linestart', 'insert lineend')
        area.insert('end', '<%s> %s' % (con.nick, data))
        send_msg(con, chan, str(data))

    def on_privmsg(self, area, con, nick, user, host, msg):
        area.insert('end', '<%s> %s\n' % (nick, msg))
        area.mark_set('insert', 'end')
        area.see('insert')

    def on_332(self, area, con, addr, nick, channel, msg):
        area.insert('end', 'Topic: %s\n' % msg)

    def on_connect_err(self, con, err):
        print 'not connected'

def ircmode():
    from vyapp.areavi import AreaVi
    AreaVi.ACTIVE.chmode('IRC')
    

ENV['ircmode'] = ircmode
install        = IrcMode


