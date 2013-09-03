#!/usr/bin/python
#
# Copyright (c) 2009-2013 Fabian Affolter <fabian at affolter-engineering.ch>
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
# Requires: python-jabberbot
# 
import os

from jabberbot import JabberBot, botcmd

class pyFortuneBot(JabberBot):
    """
    This is a simple Jabber bot that can tell you a fortune.
    
    Contact: You <you at some-domain.tld>
    """
    @botcmd
    def fortune( self, mess, args):
        """Get a random quote"""
        fortune = os.popen('/usr/bin/fortune').read()
        return fortune
 
username = 'jabber username'
password = 'jabber account password'
bot = pyFortuneBot(username,password)
bot.serve_forever()
