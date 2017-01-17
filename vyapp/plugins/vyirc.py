"""
Overview
========

It implements a neat IRC Client interface that permits connection with multiple networks. IRC networks turn into
tabs, IRC network channels turn into tabs as well.

Key-Commands
============

Mode: GAMMA
Event: <Key-i>
Description: Get in IRC mode, only possible for areavi instances that are tied to IRC connecitons.

Mode: IRC
Event: <Control-e>
Description: Used to send raw IRC commands to the IRC network.

Mode: IRC
Event: <Control-c>
Description: Used to open a private chat channel with an user.

Mode: IRC
Event: <F1>
Description: Used to pick up a different position in the AreaVi instance where to drop
the text coming from the irc network.

Commands
========

Command: IrcMode(self, addr, port, user, nick, irccmd, channels=[])
Description: Initiate a new IRC connection.
addr     = The IRC network address.
port     = The IRC network port.
user     = The user parameters like 'vy vy vy :vy'
irccmd   = A sequence of IRC commands to be executed on motd.
           It is used to identify nick.
channels = A list of channels to join in.

"""

from untwisted.plugins.irc import Irc, Misc, send_cmd, send_msg
from untwisted.network import Spin, xmap, spawn, zmap, once
from untwisted.iostd import Client, Stdin, Stdout, CONNECT, CONNECT_ERR, LOAD, CLOSE, lose
from untwisted.splits import Terminator
from vyapp.exe import exec_quiet
from vyapp.plugins import ENV
from vyapp.ask import Ask, Get
from vyapp.app import root
from vyapp.areavi import AreaVi

H1 = '<%s> %s\n' 
H2 = 'Topic :%s\n' 
H3 = '>>> %s has left %s :%s<<<\n' 
H4 = '>>> %s has joined %s <<<\n' 
H5 = '>>> %s is now known as %s <<<\n'
H6 = 'Peers:%s\n'
H7 = '>>> Connection is down ! <<<\n'
H8 = '>>> %s has kicked %s from %s (%s) <<<\n'
H9 = '>>> %s sets mode %s %s on %s <<<\n'
H10 = '>>> Connection is down ! <<<\n'

class IrcMode(object):
    def __init__(self, addr, port, user, nick, irccmd, channels=[]):
        con      = Spin()
        self.con = con
        con.connect_ex((addr, int(port)))
        Client(con)

        xmap(con, CONNECT, self.on_connect)
        xmap(con, CONNECT_ERR, self.on_connect_err)
        self.misc      = None
        self.addr      = addr
        self.port      = port
        self.user      = user
        self.nick      = nick
        self.irccmd    = irccmd
        self.channels  = channels

    def send_cmd(self, area, con):
        ask = Ask(area)
        send_cmd(con, ask.data)

    def on_connect(self, con):
        area = root.note.create(self.addr)    
        area.bind('<Destroy>', lambda event: send_cmd(con, 'QUIT :vy rules!'), add=True)

        Stdin(con)
        Stdout(con)
        Terminator(con)
        Irc(con)

        xmap(con, CLOSE, lambda con, err: lose(con))
        self.set_common_irc_handles(area, con)
        self.set_common_irc_commands(area, con)
        xmap(con, '376', lambda con, *args: send_cmd(con, self.irccmd))
        xmap(con, '376', self.auto_join)

        send_cmd(con, 'NICK %s' % self.nick)
        send_cmd(con, 'USER %s' % self.user) 

    def create_channel(self, area, con, chan):
        area_chan = self.create_area(chan)
        self.set_common_irc_commands(area_chan, con)
        self.set_common_chan_commands(area_chan, con, chan)
        self.set_common_chan_handles(area_chan, con, chan)

        # area_chan.bind('<Destroy>', lambda event: send_cmd(con, 'PART %s' % chan), add=True)
        # on_close = lambda con, err: area_chan.unbind('<Destroy>')
        # xmap(con, CLOSE, on_close)
        # area_chan.bind('<Destroy>', lambda event: zmap(con, CLOSE, on_close), add=True)
        # xmap(con, '*PART->%s' % chan, lambda con, *args: exec_quiet(area_chan.unbind, '<Destroy>'))
        # xmap(con, '*PART->%s' % chan, lambda con, *args: zmap(con, CLOSE, on_close))

        area_chan.bind('<Destroy>', lambda event: send_cmd(con, 'PART %s' % chan), add=True)
        once(con, '*PART->%s' % chan, lambda con, *args: area_chan.unbind('<Destroy>'))

    def create_area(self, name):
        area = root.note.create(name)
        return area

    def start_user_chat(self, area, con):
        ask = Ask(area)
        self.create_user_chat(con, ask.data)

    def create_user_chat(self, con, nick):
        area_user = self.create_area(nick)
        self.set_common_irc_commands(area_user, con)
        self.set_common_chan_commands(area_user, con, nick)
        return area_user

    def deliver_user_msg(self, con, nick, user, host, target, msg):
        try:
            area_user = dict(map(lambda (key, value): (key.lower(), value), 
                                 AreaVi.get_opened_files(root).iteritems()))[nick.lower()]
        except KeyError:
            area_user = self.create_user_chat(con, nick)
        finally:
            area_user.append(H1 % (nick, msg))

    def set_common_irc_commands(self, area, con):
        area.add_mode('IRC')
        area.chmode('IRC')
        area.install(('GAMMA', '<Key-i>', lambda event: event.widget.chmode('IRC')),
                     (-1, '<<Chmode-IRC>>', lambda event: event.widget.mark_set('insert', 'end')),
                     ('IRC', '<Control-e>', lambda event: self.send_cmd(event.widget, con)),
                     ('IRC', '<Control-c>', lambda event: self.start_user_chat(event.widget, con)))

    def set_common_irc_handles(self, area, con):
        l1 = lambda con, chan: self.create_channel(area, con, chan)
        l2 = lambda con, prefix, servaddr: send_cmd(con, 'PONG :%s' % servaddr)
        l3 = lambda con, data: area.append('%s\n' % data)

        self.misc = Misc(con)
        xmap(con, '*JOIN', l1)
        xmap(con, 'PING', l2)
        xmap(con, Terminator.FOUND, l3)
        xmap(con, 'PMSG', self.deliver_user_msg)

    def set_common_chan_commands(self, area, con, chan):
        e1 = lambda event: self.send_msg(event.widget, chan, con)

        area.hook('IRC', '<Key-i>', lambda event: Get(area, 
        events={'<Escape>': lambda wid: True, 
                '<Return>': lambda wid: self.send_msg(area, wid, chan, con)}))

    def set_common_chan_handles(self, area, con, chan):
        l1 = lambda con, nick, user, host, msg: area.append(H1 % (nick, msg))
        l2 = lambda con, addr, nick, msg: area.append(H2 % msg)
        l3 = lambda con, nick, user, host, msg: area.append(H3 % (nick, chan, msg))

        l4 = lambda con, nick, user, host: area.append(H4 % (nick, chan))
        l5 = lambda con, nicka, user, host, nickb: area.append(H5 % (nicka, nickb))
        l6 = lambda con, prefix, nick, mode, peers: area.append(H6 % peers)
        l7 = lambda con, *args: area.append(H7)
        l8 = lambda con, nick, user, host, target, msg: area.append(H8 % (nick, target, chan, msg))
        l9 = lambda con, nick, user, host, mode, target='': area.append(H9 % (nick, chan, mode, target))

        events = (('PRIVMSG->%s' % chan , l1), ('332->%s' % chan, l2),
                  ('PART->%s' % chan, l3), ('JOIN->%s' % chan, l4), 
                  ('*NICK', l5), ('353->%s' % chan, l6), (CLOSE, l7), 
                  ('KICK->%s' % chan, l8), ('MODE->%s' % chan, l9))

        for key, value in events:
            xmap(con, key, value)

        def unset(con, *args):
            for key, value in events:
                zmap(con, key, value)

        once(con, '*PART->%s' % chan, unset)
        xmap(con, '*KICK->%s' % chan, unset)
        area.bind('<Destroy>', lambda event: unset(con), add=True)

    def auto_join(self, con, *args):
        for ind in self.channels:
            send_cmd(con, 'JOIN %s' % ind)

    def send_msg(self, area, wid, chan, con):
        data = wid.get()
        area.append(H1 % (self.misc.nick, data))
        send_msg(con, chan, data.encode('utf-8'))
        wid.delete(0, 'end')

    def on_connect_err(self, con, err):
        print 'not connected'











