# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2013 Fabian Affolter <fabian@affolter-engineering.ch>
#
# Released under the BSD license. See COPYING file for details.
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
