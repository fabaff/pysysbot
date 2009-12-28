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

class pyFortuneBot(JabberBot):
    """
    This is a simple Jabber bot that shows you who is logged in.
    
    Contact: You <you at some-domain.tld>
    """
    @botcmd
    def who(self, mess, args):
    """Display who's currently logged in"""
        who = os.popen('/usr/bin/who').read().strip()
        return who
 
username = 'jabber username'
password = 'jabber account password'
bot = pyFortuneBot(username,password)
bot.serve_forever()
