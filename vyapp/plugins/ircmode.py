"""
Overview
========


Usage
=====

Key-Commands
============

"""

from untwisted.plugins.irc import Irc, Misc, send_cmd, send_msg
from untwisted.network import Spin, xmap, spawn, zmap
from untwisted.utils.stdio import Client, Stdin, Stdout, CONNECT, CONNECT_ERR, LOAD, CLOSE, lose
from untwisted.utils.shrug import Shrug, FOUND
from vyapp.plugins import ENV
from vyapp.ask import Ask
from vyapp.app import root
from vyapp.areavi import AreaVi

H1 = '<%s> %s\n' 
H2 = 'Topic :%s\n' 
H3 = '>>>%s has left %s.<<<\n' 
H4 = '>>>%s has joined %s.<<<\n' 
H5 = '>>>%s is now known as %s<<<\n'
H6 = 'Peers:%s\n'
# H7 = '>>>%s has quit (%s)<<<\n'

class IrcMode(object):
    def __init__(self, area, addr, port):
        con = Spin()
        con.connect_ex((addr, int(port)))
        Client(con)

        xmap(con, CONNECT, lambda con: self.set_up_con(con, area))
        xmap(con, CONNECT_ERR, self.on_connect_err)
        self.misc = None

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
        area_chan = self.create_area(chan)
        self.set_common_irc_commands(area_chan, con)
        self.set_common_chan_commands(area_chan, con, chan)
        self.set_common_chan_handles(area_chan, con, chan)


    def create_area(self, name):
        area = root.note.create(name)
        area.insert('end','\n\n')
        area.mark_set('CHDATA', '1.0')
        return area

    def deliver_user_msg(self, con, nick, user, host, target, msg):
        try:
            area_user = AreaVi.get_opened_files(root)[nick]
        except KeyError:
            area_user = self.create_area(nick)
            self.set_common_irc_commands(area_user, con)
            self.set_common_chan_commands(area_user, con, nick)
        finally:
            area_user.insee('CHDATA', H1 % (nick, msg))

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

        self.misc = Misc(con)
        xmap(con, 'MEJOIN', l1)
        xmap(con, 'PING', l2)
        xmap(con, FOUND, l3)
        xmap(con, 'PMSG', self.deliver_user_msg)

    def set_common_chan_commands(self, area, con, chan):
        e1 = lambda event: self.send_msg(event.widget, chan, con)
        area.hook('IRC', '<Return>', e1)

    def set_common_chan_handles(self, area, con, chan):
        l1 = lambda con, nick, user, host, msg: area.insee('CHDATA', H1 % (nick, msg))
        l2 = lambda con, addr, nick, msg: area.insee('CHDATA', H2 % msg)
        # it may be missing a msg='' parameter.
        l3 = lambda con, nick, user, host: area.insee('CHDATA', H3 % (nick, chan))
        l4 = lambda con, nick, user, host: area.insee('CHDATA', H4 % (nick, chan))
        l5 = lambda con, nicka, user, host, nickb: area.insee('CHDATA', H5 % (nicka, nickb))
        l6 = lambda con, prefix, nick, mode, peers: area.insee('CHDATA', H6 % peers)
        # l7 = lambda con, nick, user, host, msg: area.insee('CHDATA', H7 % (nick, msg))

        events = (('PRIVMSG->%s' % chan , l1), ('332->%s' % chan, l2),
            ('PART->%s' % chan, l3), ('JOIN->%s' % chan, l4), ('MENICK', l5), ('353->%s' % chan, l6))

        for key, value in events:
            xmap(con, key, value)

        def unset(con, *args):
            for key, value in events:
                zmap(con, key, value)
            zmap(con, 'PART->%s->MEPART' % chan, unset)

        xmap(con, 'PART->%s->MEPART' % chan, unset)

    def send_msg(self, area, chan, con):
        data = area.cmd_like()
        area.insee('CHDATA', H1 % (self.misc.nick, data))
        send_msg(con, chan, data.encode('utf-8'))
        return 'break'

    def on_connect_err(self, con, err):
        print 'not connected'

def ircmode(addr='irc.freenode.org', port=6667):
    area = root.note.create(addr)    
    IrcMode(area, addr, port)

ENV['ircmode'] = ircmode














