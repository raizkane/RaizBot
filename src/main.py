#!/usr/bin/env python

'''
		Copyright (C) 2015 Raiz Kane <raiz@airmail.cc>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

# Importing necessary libraries/modules

import socket

# Functions must be defined here for later execution

server = "irc.oftc.net"
channel = "#botcontrol"
botnick = "RaizBot"

def ping(): 
	ircsock.send("PONG :pingis\n")  

def sendmsg(chan, msg):
	ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan):
	ircsock.send("JOIN "+ chan +"\n")

# The whole code goes here

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n")
ircsock.send("NICK "+ botnick +"\n")

joinchan(channel)
joinchan("#oftc-hacker")
joinchan("#nottor")


while 1:
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)

	if ircmsg.find(":#nottor, contact") != -1:
		sendmsg("#nottor", "[0x2C1A25C7] Raiz Kane <raiz@airmail.cc>")
		sendmsg("#nottor", "		E9B9 460F 0389 F4AC 713C")
		sendmsg("#nottor", "		EEDA 13D1 E8BF 2C1A 25C7")

	if ircmsg.find(":#oftc-hacker, contact") != -1:
		sendmsg("#oftc-hacker", "[0x2C1A25C7] Raiz Kane <raiz@airmail.cc>")
		sendmsg("#oftc-hacker", "		E9B9 460F 0389 F4AC 713C")
		sendmsg("#oftc-hacker", "		EEDA 13D1 E8BF 2C1A 25C7")
		
	if ircmsg.find(":#nottor, map") != -1:
		sendmsg("#nottor", "OFTC channels map <https://github.com/raizkane/OFTC-channels-map> for more info visit #map.")

	if ircmsg.find(":#oftc-hacker, map") != -1:
		sendmsg("#oftc-hacker", "OFTC channels map <https://github.com/raizkane/OFTC-channels-map> for more info visit #map.")

	if ircmsg.find(":#nottor, awesomepentest") != -1:
		sendmsg("#nottor", "https://github.com/enaqx/awesome-pentest")
		
	if ircmsg.find(":#oftc-hacker, awesomepentest") != -1:
		sendmsg("#oftc-hacker", "https://github.com/enaqx/awesome-pentest")
		
	if ircmsg.find(":#nottor, who") != -1:
		sendmsg("#nottor", "Hey, I'm RaizBot, Raiz made me to make his life easier")

	if ircmsg.find(":#oftc-hacker, who") != -1:
		sendmsg("#oftc-hacker", "Hey, I'm RaizBot, Raiz made me to make his life easier")

	if ircmsg.find("PING :") != -1: 
		ping()

