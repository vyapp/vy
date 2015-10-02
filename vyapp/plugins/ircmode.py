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
from untwisted.utils.stdio import Client, Stdin, Stdout, CONNECT, CONNECT_ERR, LOAD, CLOSE, lose
from untwisted.utils.shrug import *
from vyapp.plugins import ENV
from vyapp.ask import Ask
from vyapp.app import root

H1 = '<%s> %s\n' 
H2 = 'Topic :%s\n' 
H3 = '>>>%s has left %s.<<<\n' 
H4 = '>>>%s has joined %s.<<<\n' 
H5 = '>>>%s is now known as %s<<<\n'
H6 = 'Peers:%s\n'

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
    spawn(con, '353->%s' % chan, prefix, 
          nick, mode, peers)

def on_332(con, addr, nick, channel, msg):
    spawn(con, '332->%s' % channel, addr, nick, msg)

def on_part(con, nick, user, host, chan):
    spawn(con, 'PART->%s' % chan, nick, 
          user, host)

    if con.nick == nick: 
        spawn(con, 'PART->%s->MEPART' % chan, chan)

def on_001(con, address, nick, *args):
    con.nick = nick

def on_nick(con, nicka, user, host, nickb):
    if not con.nick == nicka: 
        return

    con.nick = nickb;
    spawn(con, 'MENICK', nicka, user, host, nickb)


class IrcMode(object):
    def __init__(self, area, addr, port):
        con = Spin()
        con.connect_ex((addr, int(port)))
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

        xmap(con, CLOSE, lambda con, err: lose(con))
        self.set_common_irc_handles(area, con)
        self.set_common_irc_commands(area, con)

    def create_channel(self, area, con, chan):
        area_chan = root.note.create(chan)

        self.set_common_irc_commands(area_chan, con)
        self.set_common_chan_commands(area_chan, con, chan)
        self.set_common_chan_handles(area_chan, con, chan)

        area_chan.insert('end','\n\n')
        area_chan.mark_set('CHDATA', '1.0')

    def set_common_irc_commands(self, area, con):
        area.add_mode('IRC', opt=True)
        area.chmode('IRC')
        area.hook('GAMMA', '<Key-i>', 
                lambda event: event.widget.chmode('IRC'))
        area.hook('IRC', '<Control-e>', lambda event: self.send_cmd(event.widget, con))

    def set_common_irc_handles(self, area, con):
        l1 = lambda con, chan: self.create_channel(area, con, chan)
        l2 = lambda con, prefix, servaddr: send_cmd(con, 'PONG :%s' % servaddr)
        l3 = lambda con, data: area.insee('end', '%s\n' % data)

        xmap(con, '001', on_001)
        xmap(con, 'PRIVMSG', on_privmsg)
        xmap(con, 'JOIN', on_join)
        xmap(con, 'PART', on_part)
        xmap(con, '353', on_353)
        xmap(con, '332', on_332)
        xmap(con, 'NICK', on_nick)

        xmap(con, 'MEJOIN', l1)
        xmap(con, 'PING', l2)
        xmap(con, FOUND, l3)

    def set_common_chan_commands(self, area, con, chan):
        e1 = lambda event: self.send_msg(event.widget, chan, con)
        area.hook('IRC', '<Return>', e1)

    def set_common_chan_handles(self, area, con, chan):
        l1 = lambda con, nick, user, host, msg: area.insee('CHDATA', H1 % (nick, msg))
        l2 = lambda con, addr, nick, msg: area.insee('CHDATA', H2 % msg)
        l3 = lambda con, nick, user, host: area.insee('CHDATA', H3 % (nick, chan))
        l4 = lambda con, nick, user, host: area.insee('CHDATA', H4 % (nick, chan))
        l5 = lambda con, nicka, user, host, nickb: area.insee('CHDATA', H5 % (nicka, nickb))
        l6 = lambda con, prefix, nick, mode, peers: area.insee('CHDATA', H6 % peers)

        events = (('PRIVMSG->%s' % chan , l1), ('332->%s' % chan, l2),
            ('PART->%s' % chan, l3), ('JOIN->%s' % chan, l4), ('MENICK', l5), ('353->%s' % chan, l6))

        for key, value in events:
            xmap(con, key, value)

        def unset(con, *args):
            for key, value in events:
                zmap(con, key, value)

        xmap(con, 'PART->%s->MEPART' % chan, unset)

    def send_msg(self, area, chan, con):
        data = area.cmd_like()
        area.insee('CHDATA', H1 % (con.nick, data))
        send_msg(con, chan, data.encode('utf-8'))
        return 'break'

    def on_connect_err(self, con, err):
        print 'not connected'

def ircmode(addr='irc.freenode.org', port=6667):
    area = root.note.create(addr)    
    IrcMode(area, addr, port)

ENV['ircmode'] = ircmode








