"""Handler for configuration settings."""
import os
import sys
import configparser


def read_config(file, config_jabber={}):
    """ Read the configuration data. """
    config_data = []
    if not (os.path.exists(file)):
        print('pysysbot configuration file does not exist.')
        sys.exit(0)
    else:
        configparse = configparser.ConfigParser()
        configparse.read(file)
        config_jabber['username'] = configparse.get('pysysbot', 'username')
        if config_jabber['username'] == 'NOT_SET':
            print(
                'Please edit your configuration file (%s) and set your JID',
                file,
            )
            sys.exit(0)
        config_jabber['password'] = configparse.get('pysysbot', 'password')
        if config_jabber['password'] == 'NOT_SET':
            print(
                'Please edit your configuration file (%s) and set your '
                'Jabber password', file,
            )
            sys.exit(0)
        config_data.append(config_jabber)
    return config_data
