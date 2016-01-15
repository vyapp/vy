"""
Overview
========

It implements a neat IRC Client interface that permits connection with multiple networks. IRC networks turn into
tabs, IRC network channels turn into tabs as well.

Usage
=====

Vyirc implements the ircmode function that has the following definition.

    ircmode(irc_server, irc_port)

In order to initiate an IRC connection one would execute something like below by pressing <Control-semicolon> in NORMAL mode.

    ircmode('irc.freenode.org', 6667)

It would start an IRC connection on a new tab. After initializing the socket connection one would send the user host to
the irc server by pressing <Control-e> in IRC mode then typing

    USER user user user :real name

again <Control-e> then

    NICK user_nick

It is enough to stabilish a connection with the IRC server. After executing the function ircmode
the new tab will be in IRC mode. In order to make the areavi instance go back to NORMAL mode it is enough to press
<Escape>. It is possible to get back in IRC mode by pressing <Key-i> in GAMMA mode. However, only areavi instances that are
tied to IRC connections can be in IRC mode.

It is possible to send only raw IRC commands to the IRC network by pressing <Control-e> in IRC mode. Some users
have a registered nick, in order to identify to an user nick, type the command below after pressing <Control-e>.

    PRIVMSG nickserv :identify nick_password

Some IRC networks may vary the command format described above.

The command to join channel is as usually implemented in other irc clients. It is as follow. It is used the
key-command <Control-e> in IRC mode.

    JOIN #channel

In order to leave a channel type the IRC command below.

    PART #channel

One can query an user by pressing <Control-c> then typing its nick. It will open an areavi instance
for private chatting with the user.

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

Commands
========

ircmode(irc_server, irc_port)
    irc_server: The IRC network address.

    irc_port: The port to connect to. It is normally 6667

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
H7 = '>>>%s has quit (%s)<<<\n'

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
        area_chan.bind('<Destroy>', lambda event: send_cmd(con, 'PART %s' % chan))

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
        area.hook('GAMMA', '<Key-i>', 
                lambda event: event.widget.chmode('IRC'))
        area.hook('IRC', '<Control-e>', lambda event: self.send_cmd(event.widget, con))
        area.hook('IRC', '<Control-c>', lambda event: self.start_user_chat(event.widget, con))
        area.install(('IRC', '<Control-q>', lambda event: self.complete_nick(event.widget)))
        area.install(('IRC', '<Control_R>', lambda event: self.reset(event.widget)))
        area.install(('IRC', '<Control_L>', lambda event: self.reset(event.widget)))

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

        def l7(con, nick, user, host, msg):
            pass

        events = (('PRIVMSG->%s' % chan , l1), ('332->%s' % chan, l2),
            ('PART->%s' % chan, l3), ('JOIN->%s' % chan, l4), ('MENICK', l5), ('353->%s' % chan, l6), ('QUIT', l7))

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








