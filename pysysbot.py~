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
import datetime
import os

class pySysBot(JabberBot):
    """
    This is a simple Jabber bot that can show you some details and
    information of the machine it is running on and about yourself.
    
    Contact: Fabian Affolter <fabian at bernewireless.net>
    """
    @botcmd
    def echo( self, mess, args):
        """Returns passed arguments"""
        return args

    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        return str(datetime.datetime.now())


    @botcmd
    def welcome( self, mess, args):
        """Returns passed arguments"""
        return args

 
username = 'jabber username'
password = 'jabber account password'
bot = pySysBot(username,password)
bot.serve_forever()
