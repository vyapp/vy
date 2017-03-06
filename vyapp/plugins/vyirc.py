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

class ChannelController(object):
    """
    """
    def __init__(self, irc, area, chan):
        self.irc   = irc
        self.area  = area
        self.chan  = chan
        self.peers = []

        events = (('PRIVMSG->%s' % chan , self.e_privmsg), 
        ('332->%s' % chan, self.e_332), 
        ('PART->%s' % chan, self.e_part), 
        ('JOIN->%s' % chan, self.e_join), 
        ('*NICK', self.e_nick),
        ('353->%s' % chan, self.e_353), 
        ('KICK->%s' % chan, self.e_kick), 
        ('MODE->%s' % chan, self.e_mode),
        (CLOSE, self.e_close))

        def unset(con, *args):
            for key, value in events:
                zmap(irc.con, key, value)

        for key, value in events:
            xmap(irc.con, key, value)

        once(irc.con, '*PART->%s' % chan, unset)
        xmap(irc.con, '*KICK->%s' % chan, unset)

        area.bind('<Destroy>', lambda event: 
        unset(irc.con), add=True)

        # When area is destroyed, it sends a PART.
        area.bind('<Destroy>', lambda event: 
        send_cmd(irc.con, 'PART %s' % chan), add=True)

        area.hook('IRC', '<Key-i>', lambda event: Get(
        events={'<Escape>': lambda wid: True, 
        '<Return>': self.msg_channel}))

        # It unbinds the above callback.
        # In case the part command as sent by text
        # by the user. After part it should destroy the
        # area.
        once(irc.con, '*PART->%s' % chan, lambda con, *args: 
        area.unbind('<Destroy>'))

    def e_privmsg(self, con, nick, user, host, msg):
        self.area.append(H1 % (nick, msg))

    def e_join(self, con, nick, user, host):
        self.area.append(H4 % (nick, self.chan))

    def e_mode(self, con, nick, user, host, mode, target=''):
        self.area.append(H9 % (nick, self.chan, mode, target))

    def e_part(self, con, nick, user, host, msg):
        self.area.append(H3 % (nick, self.chan, msg))

    def e_kick(self, con, nick, user, host, target, msg):
        self.area.append(H8 % (nick, target, self.chan, msg))

    def e_nick(self, con, nicka, user, host, nickb):
        self.area.append(H5 % (nicka, nickb))

    def e_close(self, con, *args):
        self.area.append(H7)

    def e_332(self, con, addr, nick, msg):
        self.area.append(H2 % msg)

    def e_353(self, con, prefix, nick, mode, peers):
        self.area.append(H6 % peers)

    def msg_channel(self, wid):
        data = wid.get()
        self.area.append(H1 % (self.irc.misc.nick, data))
        send_msg(self.con, self.chan, data.encode('utf-8'))
        wid.delete(0, 'end')

class UserController(object):
    """
    """
    def __init__(self, irc, area):
        self.irc = irc
        area.hook('IRC', '<Key-i>', lambda event: Get(
        events={'<Escape>': lambda wid: True, 
        '<Return>': self.msg_user}))

    def msg_user(self, wid):
        data = wid.get()
        self.area.append(H1 % (self.irc.misc.nick, data))
        send_msg(self.con, self.chan, data.encode('utf-8'))
        wid.delete(0, 'end')

class IrcMode(object):
    """
    """

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
        ask = Ask()
        send_cmd(con, ask.data)

    def on_connect(self, con):
        area = root.note.create(self.addr)    

        area.bind('<Destroy>', lambda event: 
        send_cmd(con, 'QUIT :vy rules!'), add=True)

        Stdin(con)
        Stdout(con)
        Terminator(con)
        Irc(con)

        xmap(con, CLOSE, lambda con, err: lose(con))
        self.set_common_irc_handles(area, con)
        self.set_common_irc_commands(area, con)

        xmap(con, '376', lambda con, *args: 
        send_cmd(con, self.irccmd))

        xmap(con, '376', self.auto_join)

        send_cmd(con, 'NICK %s' % self.nick)
        send_cmd(con, 'USER %s' % self.user) 

    def create_channel(self, area, con, chan):
        area_chan = self.create_area(chan)
        self.set_common_irc_commands(area_chan, con)
        ChannelController(con, area_chan, chan)

    def create_area(self, name):
        area = root.note.create(name)
        area.add_mode('IRC')
        area.chmode('IRC')
        area.install(('GAMMA', '<Key-i>', lambda event: area.chmode('IRC')),
        (-1, '<<Chmode-IRC>>', lambda event: area..mark_set('insert', 'end')),
        ('IRC', '<Control-e>', lambda event: self.send_cmd(area, con)),
        ('IRC', '<Control-c>', lambda event: self.start_user_chat(area, con)))

        return area

    def start_user_chat(self, area, con):
        ask = Ask()
        self.create_user_chat(con, ask.data)

    def create_user_chat(self, con, nick):
        area_user = self.create_area(nick)
        return area_user

    def deliver_user_msg(self, con, nick, user, host, target, msg):
        try:
            area_user = dict(map(lambda (key, value): (key.lower(), value), 
                                 AreaVi.get_opened_files(root).iteritems()))[nick.lower()]
        except KeyError:
            area_user = self.create_user_chat(con, nick)
        finally:
            area_user.append(H1 % (nick, msg))

    def set_common_irc_handles(self, area, con):
        l1 = lambda con, chan: self.create_channel(area, con, chan)
        l2 = lambda con, prefix, servaddr: send_cmd(con, 'PONG :%s' % servaddr)
        l3 = lambda con, data: area.append('%s\n' % data)

        self.misc = Misc(con)
        xmap(con, '*JOIN', l1)
        xmap(con, 'PING', l2)
        xmap(con, Terminator.FOUND, l3)
        xmap(con, 'PMSG', self.deliver_user_msg)

    def auto_join(self, con, *args):
        for ind in self.channels:
            send_cmd(con, 'JOIN %s' % ind)

    def on_connect_err(self, con, err):
        print 'not connected'




