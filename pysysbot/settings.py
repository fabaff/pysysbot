# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2013 Fabian Affolter <fabian@affolter-engineering.ch>
#
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

import os
import sys
import ConfigParser

def read_config(file, config_jabber={}):
    """
    Read the configuration data from user's home directory.
    Create an example file if it doesn't exist.
    
    Based on MythJabberbot (http://www.ian-barton.com/wiki/MythTV/MythJabberbot)
    """
    BOT_NAME = 'pysysbot'
    config_data = []
    CONFIG_FILE = os.path.expanduser("~") + '/.' + BOT_NAME
    if not(os.path.exists(CONFIG_FILE)):
        print '~/.' + BOT_NAME + ' does not exist.'
        configfile = open(CONFIG_FILE, "w")
        configparse = ConfigParser.ConfigParser()
        configparse.add_section(BOT_NAME)
        print 'Please enter your jabber username and your password.'
        username_in = raw_input('Username: ').strip()
        password_in = raw_input('Password: ').strip()
        if len(username_in) == 0 and len(password_in) == 0:
            configparse.set(BOT_NAME, 'username', 'NOT SET')
            configparse.set(BOT_NAME, 'password', 'NOT SET')
            print 'Please edit ~/.' + BOT_NAME + ' afterwards to match your'
            print 'settings if you do not have a jabber account at the moment.'
        else:
            configparse.set(BOT_NAME, 'username', username_in)
            configparse.set(BOT_NAME, 'password', password_in)
            print '~/.' + BOT_NAME + ' created.'
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
