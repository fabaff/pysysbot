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
import os, sys
import ConfigParser

class pySysBot(JabberBot):
    """
    This is a simple Jabber bot that can show you some details and
    information of the machine it is running on.
    
    Contact: You <you at some-domain.tld>
    """
    def top_of_help_message(self):
        """Returns a string that forms the top of the help message"""
        return "pySysBot"

    def bottom_of_help_message(self):
        """Returns a string that forms the bottom of the help message"""
        return 'Version: 0.1'

#Bot commands
    @botcmd
    def time( self, mess, args):
        """Displays current server time"""
        return str(datetime.datetime.now())

    @botcmd
    def uptime(self, mess, args):
        """Displays the server uptime"""
        uptime = open('/proc/uptime').read().split()[0]
        # This is heavily based on the work of Hubert Chathi and his System status bot.
        uptime = float(uptime)
        (uptime,secs) = (int(uptime / 60), uptime % 60)
        (uptime,mins) = divmod(uptime,60)
        (days,hours) = divmod(uptime,24)

        uptime = 'Uptime: %d day%s, %d hour%s %02d min%s' % (days, days != 1 
            and 's' or '', hours, hours != 1 and 's' or '', mins,
            mins != 1 and 's' or '')
        return uptime

    @botcmd
    def server(self, mess, args):
        """Displays server information"""
        server = os.uname()
        data = "System: \t" + server[0] + \
            "\n" +"FQDN: \t" + server[1] + \
            "\n" +"Kernel: \t" + server[2] + \
            "\n" +"Data: \t" + server[3] + \
            "\n" +"Arch: \t" + server[4]
        return data
 
def read_config(file, config_jabber={}):
    """
    Read the configuration data from user's home directory.
    Create an example file if it doesn't exist.
    """

    if not(os.path.exists(CONFIG_FILE)):
        print '~/.my' + BOT_NAME + ' does not exist.'
        configfile = open(CONFIG_FILE, "w")
        configparse = ConfigParser.ConfigParser()
        configparse.add_section(BOT_NAME)
        print 'Please enter your jabber username and your password.'
        username_in = raw_input('Username: ').strip()
        password_in = raw_input('Password: ').strip()
        if len(username_in) == 0 and len(password_in) == 0:
            configparse.set(BOT_NAME, 'username', 'CHANGE_ME')
            configparse.set(BOT_NAME, 'password', 'NOT_SET')
            print 'Please edit ~/.my' + BOT_NAME + ' afterwards to match your'
            print 'settings if you do not have a jabber account at the moment.'
        else:
            configparse.set(BOT_NAME, 'username', username_in)
            configparse.set(BOT_NAME, 'password', password_in)
            print '~/.my' + BOT_NAME + ' created.'
        configparse.write(configfile)
        configfile.close()
        sys.exit()

    else:
        configparse = ConfigParser.ConfigParser()
        configparse.read(file)
        config_jabber['username'] = configparse.get(BOT_NAME, 'username')
        config_jabber['password'] = configparse.get(BOT_NAME, 'password')
        config_data.append(config_jabber)

    return config_data

def main():
    config = read_config(CONFIG_FILE)
    bot = pySysBot(config[0]['username'], config[0]['password'])
    bot.serve_forever()

if __name__ == '__main__':
    BOT_NAME = 'pysysbot'
    CONFIG_FILE = os.path.expanduser("~") + '/.my' + BOT_NAME
    config_data = []
    main()
