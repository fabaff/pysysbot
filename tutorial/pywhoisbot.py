#!/usr/bin/python
#
# Copyright (c) 2009  Fabian Affolter, Swissjabber. 
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Fabian Affolter <fabian at bernewireless.net>
#
# Requires: python-jabberbot
# 
from jabberbot import JabberBot, botcmd
import os

class pyWhoisBot(JabberBot):
    """
    This is a simple Jabber bot that shows you the details about
    a specific URL or an IP address.
    
    Contact: You <you at some-domain.tld>
    """
    @botcmd
    def whois( self, mess, args):
        """Displays details about a domain name or an IP address"""
        whois = os.popen('/usr/bin/whois ' + args).read().strip()
        nslook = os.popen('/usr/bin/nslookup ' + args).read().strip()
        return 'Whois\n--------\n%s\n\nNslookup\n--------------\n%s' % ( whois, nslook, )

username = 'jabber username'
password = 'jabber account password'
bot = pyWhoisBot(username,password)
bot.serve_forever()
