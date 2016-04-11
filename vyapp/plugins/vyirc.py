"""
Overview
========

It implements a neat IRC Client interface that permits connection with multiple networks. IRC networks turn into
tabs, IRC network channels turn into tabs as well.

Usage
=====

Vyirc implements the IrcMode class that has the following constructor definition.

    def __init__(self, addr, port, user, nick, irccmd, channels=[]):

In order to initiate an IRC connection one would execute something like below by pressing <Control-semicolon> in NORMAL mode.

    IrcMode(addr='irc.freenode.org', port=6667, user='vy vy vy :vyirc', nick='vyirc', 
             irccmd='PRIVMSG nickserv :identify nick_password', channels=['#vy'])

It is enough to stabilish a connection with the IRC server. 
After calling IrcMode constructor it will open a new tab tied to the IRC connection. The new tab
will be in IRC mode.

It is possible to send only raw IRC commands to the IRC network by pressing <Control-e> in IRC mode. Some users
have a registered nick, in order to identify to an user nick, type the command below after pressing <Control-e>.

    PRIVMSG nickserv :identify nick_password

Some IRC networks may vary the command format described above.

The command to join a channel is as usually implemented in other irc clients. It is as follow. It is used the
key-command <Control-e> in IRC mode.

    JOIN #channel

In order to leave a channel type the IRC command below.

    PART #channel

One can query an user by pressing <Control-c> then typing its nick. It will open an areavi instance
for private chatting with the user.

For creating shortcuts for IRC networks, just import IrcMode from vyrc file then define IRC network functions like below.

def irc_freenode(addr='irc.freenode.org', port=6667, user='vy vy vy :vyirc', nick='vyirc', 
             irccmd='PRIVMSG nickserv :identify nick_password', channels=['#vy']):
    IrcMode(addr, port, user, nick, irccmd, channels)

The irc_freenode function will be exposed in vyapp.plugins.ENV, so it is possible to call it from <Control-e> or
<Key-semicolon>

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
from vyapp.ask import Ask
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
        con = Spin()
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
        area.bind('<Destroy>', lambda event: send_cmd(con, 'QUIT :vyirc rules!'), add=True)

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
        area.insert('end','\n\n')
        area.mark_set('CHDATA', '1.0')
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
            area_user.insee('CHDATA', H1 % (nick, msg))

    def set_common_irc_commands(self, area, con):
        area.add_mode('IRC', opt=True)
        area.chmode('IRC')
        area.install(('GAMMA', '<Key-i>', lambda event: event.widget.chmode('IRC')),
                     ('IRC', '<Control-e>', lambda event: self.send_cmd(event.widget, con)),
                     ('IRC', '<Control-c>', lambda event: self.start_user_chat(event.widget, con)),
                     ('IRC', '<Control-q>', lambda event: self.complete_nick(event.widget)),
                     ('IRC', '<Control_R>', lambda event: self.reset(event.widget)),
                     ('IRC', '<Control_L>', lambda event: self.reset(event.widget)),
                     ('IRC', '<F1>', lambda event: event.widget.mark_set('CHDATA', 'insert')))

    def complete_nick(self, area):
        """
        """

        try:    
            self.seq.next()
        except StopIteration:
            pass

    def reset(self, area):
        self.seq = area.complete_word(area.master)

    def set_common_irc_handles(self, area, con):
        l1 = lambda con, chan: self.create_channel(area, con, chan)
        l2 = lambda con, prefix, servaddr: send_cmd(con, 'PONG :%s' % servaddr)
        l3 = lambda con, data: area.insee('end', '%s\n' % data)

        self.misc = Misc(con)
        xmap(con, '*JOIN', l1)
        xmap(con, 'PING', l2)
        xmap(con, Terminator.FOUND, l3)
        xmap(con, 'PMSG', self.deliver_user_msg)

    def set_common_chan_commands(self, area, con, chan):
        e1 = lambda event: self.send_msg(event.widget, chan, con)
        area.hook('IRC', '<Return>', e1)

    def set_common_chan_handles(self, area, con, chan):
        l1 = lambda con, nick, user, host, msg: area.insee('CHDATA', H1 % (nick, msg))
        l2 = lambda con, addr, nick, msg: area.insee('CHDATA', H2 % msg)

        l3 = lambda con, nick, user, host, msg: area.insee('CHDATA', H3 % (nick, chan, msg))

        l4 = lambda con, nick, user, host: area.insee('CHDATA', H4 % (nick, chan))
        l5 = lambda con, nicka, user, host, nickb: area.insee('CHDATA', H5 % (nicka, nickb))
        l6 = lambda con, prefix, nick, mode, peers: area.insee('CHDATA', H6 % peers)
        l7 = lambda con, *args: area.insee('CHDATA', H7)
        l8 = lambda con, nick, user, host, target, msg: area.insee('CHDATA', H8 % (nick, target, chan, msg))
        l9 = lambda con, nick, user, host, mode, target='': area.insee('CHDATA', H9 % (nick, chan, mode, target))


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

    def send_msg(self, area, chan, con):
        data = area.cmd_like()
        area.insee('CHDATA', H1 % (self.misc.nick, data))
        send_msg(con, chan, data.encode('utf-8'))
        return 'break'

    def on_connect_err(self, con, err):
        print 'not connected'





