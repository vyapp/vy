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
H11 = '>>> %s [%s@%s] has quit :%s <<<\n' 

class ChannelController(object):
    """
    Controls channel events and installs basic commands.
    """
    def __init__(self, irc, area, chan):
        self.irc   = irc
        self.area  = area
        self.chan  = chan
        self.peers = set()

        events = (('PRIVMSG->%s' % chan , self.e_privmsg), 
        ('332->%s' % chan, self.e_332), 
        ('PART->%s' % chan, self.e_part), 
        ('JOIN->%s' % chan, self.e_join), 
        ('*NICK', self.e_nick),
        ('QUIT', self.e_quit),
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
    
        # Hook to send msgs.
        area.hook('IRC', '<Key-i>', lambda event: Get(
        events={'<Escape>': lambda wid: True, 
        '<Return>': lambda wid: 
        self.irc.drop_msg(area, wid, chan)}))

        # It unbinds the above callback.
        # In case the part command as sent by text
        # by the user. After part it should destroy the
        # area.
        once(irc.con, '*PART->%s' % chan, lambda con, *args: 
        area.unbind('<Destroy>'))

    def e_privmsg(self, con, nick, user, host, msg):
        self.area.append(H1 % (nick, msg))
        self.area.tag_add('(VYIRC-PRIVMSG)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_join(self, con, nick, user, host):
        self.peers.add(nick.lower())
        self.area.append(H4 % (nick, self.chan))
        self.area.tag_add('(VYIRC-JOIN)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_mode(self, con, nick, user, host, mode, target=''):
        self.area.append(H9 % (nick, self.chan, mode, target))
        self.area.tag_add('(VYIRC-MODE)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_part(self, con, nick, user, host, msg):
        self.peers.remove(nick.lower())
        self.area.append(H3 % (nick, self.chan, msg))
        self.area.tag_add('(VYIRC-PART)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_kick(self, con, nick, user, host, target, msg):
        self.area.append(H8 % (nick, target, self.chan, msg))
        self.area.tag_add('(VYIRC-KICK)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_nick(self, con, nicka, user, host, nickb):
        self.area.append(H5 % (nicka, nickb))

    def e_close(self, con, *args):
        self.area.append(H7)
        self.area.tag_add('(VYIRC-CLOSE)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_332(self, con, addr, nick, msg):
        self.area.append(H2 % msg)
        self.area.tag_add('(VYIRC-332)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_353(self, con, prefix, nick, mode, peers):
        self.peers.update(peers.lower().split(' '))
        self.area.append(H6 % peers)
        self.area.tag_add('(VYIRC-353)', 
        'insert -1l linestart', 'insert -1l lineend')

    def e_quit(self, con, nick, user, host, msg=''):
        if not nick.lower() in self.peers: return
        self.area.append(H11 % (nick, user, host, msg))
        self.area.tag_add('(VYIRC-QUIT)', 
        'insert -1l linestart', 'insert -1l lineend')

class IrcMode(object):
    """
    Controls basic irc events and installs basic commands.
    """

    COLOR_SCHEME = {
    '(VYIRC-PRIVMSG)': {'foreground': '#688B96'},
    '(VYIRC-JOIN)': {'foreground': '#F06EF0'},
    '(VYIRC-PART)': {'foreground': '#F0BDAD'},
    '(VYIRC-QUIT)': {'foreground': '#4EDB1F'},
    '(VYIRC-NICK)': {'foreground': '#E9F0AD'},
    '(VYIRC-KICK)': {'foreground': '#FC8D9A'},
    '(VYIRC-353)': {'foreground': '#BF9163'},
    '(VYIRC-332)': {'foreground': '#81BFFC'},
    '(VYIRC-CLOSE)': {'foreground': '#A7F2E9'}}
    
    def __init__(self, addr, port, user, nick, irccmd, channels=[]):
        con      = Spin()
        self.con = con
        con.connect_ex((addr, int(port)))
        Client(con)

        xmap(con, CONNECT, self.on_connect)
        xmap(con, CONNECT_ERR, self.e_connect_err)
        self.misc     = None
        self.addr     = addr
        self.port     = port
        self.user     = user
        self.nick     = nick
        self.irccmd   = irccmd
        self.channels = channels

    def send_cmd(self, event):
        """
        Used to drop irc commands.
        """

        ask = Ask()
        send_cmd(self.con, ask.data)

    def on_connect(self, con):
        area = self.create_area(self.addr)
        area.bind('<Destroy>', lambda event: 
        send_cmd(con, 'QUIT :vy rules!'), add=True)

        Stdin(con)
        Stdout(con)
        Terminator(con)
        Irc(con)
        self.misc = Misc(con)

        xmap(con, CLOSE, lambda con, err: lose(con))
        xmap(con, '*JOIN', self.create_channel)
        xmap(con, Terminator.FOUND, 
        lambda con, data: area.append('%s\n' % data))

        xmap(con, 'PMSG', self.e_pmsg)
        xmap(con, '376', lambda con, *args: 
        send_cmd(con, self.irccmd))

        xmap(con, '376', self.auto_join)

        xmap(con, 'PING', lambda con, prefix, servaddr: 
        send_cmd(con, 'PONG :%s' % servaddr))

        send_cmd(con, 'NICK %s' % self.nick)
        send_cmd(con, 'USER %s' % self.user) 

    def create_channel(self, con, chan):
        area = self.create_area(chan)
        ChannelController(self, area, chan)

    def create_area(self, name):
        """
        Create areavi instance for a target and installs 
        basic irc commands.
        """

        area = root.note.create(name)
        area.add_mode('IRC')
        area.chmode('IRC')
        area.install(('GAMMA', '<Key-i>', lambda event: area.chmode('IRC')),
        (-1, '<<Chmode-IRC>>', lambda event: area.mark_set('insert', 'end')),
        ('IRC', '<Control-e>', self.send_cmd),
        ('IRC', '<Control-c>',  self.open_private_channel))

        for indi, indj in self.COLOR_SCHEME.iteritems():
            area.tag_config(indi, **indj)
        return area

    def open_private_channel(self, event):
        data = Ask().data
        if data: self.create_private_channel(data)

    def create_private_channel(self, nick):
        """
        Create private messages channels.
        """

        # In case there is no areavi for the user then creates
        # a private channel.
        area = self.create_area(nick)
        area.hook('IRC', '<Key-i>', lambda event: Get(
        events={'<Escape>': lambda wid: True, 
        '<Return>': lambda wid: 
        self.drop_msg(area, wid, nick)}))
        return area

    def e_pmsg(self, con, nick, user, host, target, msg):
        """
        Private messages sent to the user are handled here.
        """
        # Attempt to retrieve the areavi which corresponds
        # to the target/user.
        base    = lambda (key, value): (key.lower(), value)
        files   = AreaVi.get_opened_files(root).iteritems()
        targets = dict(map(base, files))

        try:
            area = targets[nick.lower()]
        except KeyError:
            area = self.create_private_channel(nick)
        else:
            area.append(H1 % (nick, msg))

    def auto_join(self, con, *args):
        for ind in self.channels:
            send_cmd(con, 'JOIN %s' % ind)

    def e_connect_err(self, con, err):
        print 'not connected'

    def drop_msg(self, area, wid, target):
        """
        Drop msgs and update the areavi.
        """

        data = wid.get()
        area.append(H1 % (self.misc.nick, data))
        send_msg(self.con, target, data.encode('utf-8'))
        area.tag_add('(VYIRC-PRIVMSG)', 
        'insert -1l linestart', 'insert -1l lineend')
        wid.delete(0, 'end')





