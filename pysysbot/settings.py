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
#
import os
import sys
import ConfigParser

def read_config(file, config_jabber={}):
    """Read the configuration data."""
    config_data = []
    if not(os.path.exists(file)):
        print 'pysysbot configuration file does not exist.'
        sys.exit(0)
    else:
        configparse = ConfigParser.ConfigParser()
        configparse.read(file)
        config_jabber['username'] = configparse.get('pysysbot', 'username')
        if config_jabber['username'] == 'NOT_SET':
            print 'Please edit your configuration file (%s) and set your JID' \
                % (file)
            sys.exit(0)
        config_jabber['password'] = configparse.get('pysysbot', 'password')
        if config_jabber['password'] == 'NOT_SET':
            print 'Please edit your configuration file (%s) and set your Jabber password' \
                % (file)
            sys.exit(0)
        config_data.append(config_jabber)
    return config_data
