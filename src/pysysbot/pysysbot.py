#!/usr/bin/python
#
# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2010 Fabian Affolter <fabian@affolter-engineering.ch>
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
# Requires: python-jabberbot
#
try:
    import datetime
    import os
    import sys
    import socket
    import ConfigParser
    import urllib2
    from jabberbot import JabberBot, botcmd
    import statgrab
except ImportError:
	print """Cannot find all required libraries please install them and try again."""
	raise SystemExit

__version__ = '0.2'


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
        return "Python %s / %s %s / %s %s" % \
            ('.'.join([str(v) for v in sys.version_info[:3]]),
             BOT_NAME,
             __version__,
             os.uname()[0],
             os.uname()[2])

#Bot commands
    @botcmd
    def time( self, mess, args):
        """Displays current server time."""
        return datetime.datetime.today().strftime('%A, %d. %B %Y %H:%M:%S')

    @botcmd
    def uptime(self, mess, args):
        """Displays the server uptime."""
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
        """Displays details about server."""
        server = os.uname()
        server_data = "System information" + \
                "\n" + " System: \t" + server[0] + \
                "\n" + " FQDN: \t"   + server[1] + \
                "\n" + " Kernel: \t" + server[2] + \
                "\n" + " Data: \t"   + server[3] + \
                "\n" + " Arch: \t"   + server[4]
        return server_data

    @botcmd
    def load(self, mess, args):
        """Displays the server load over the last 1, 5, and 15 minutes."""
        loaddata = []
        load = os.getloadavg()
        for i in load:
                loaddata.append(i)
        load_data = "Load average of the system" + \
                "\n" +"  1 min: \t" + str(loaddata[0]) + \
                "\n" +"  5 min: \t" + str(loaddata[1]) + \
                "\n" +" 15 min: \t" + str(loaddata[2])
        return load_data

    @botcmd
    def processes(self, mess, args):
        """Displays the processes of the server."""
        process = statgrab.sg_get_process_count()
        load_process = "Processes" + \
                "\n" + " Zombie: \t"    + str(process['zombie'])  + \
                "\n" + " Running: \t"   + str(process['running'])  + \
                "\n" + " Stopped: \t"   + str(process['stopped'])  + \
                "\n" + " Sleeping: \t"  + str(process['sleeping']) + \
                "\n" + " Total: \t\t"   + str(process['total'])
        return load_process

    @botcmd
    def mem(self, mess, args):
        """Displays the memory status of the server."""
        swapstat = statgrab.sg_get_swap_stats()
        memstat = statgrab.sg_get_mem_stats()
        #Some calculation to get the perc of the data
        memdiff = memstat['total'] - memstat['free']
        memfloat = float (memdiff) / float(memstat['total'])
        memperc = int(round (memfloat * 100))
        swapdiff = swapstat['total'] - swapstat['free']
        swapfloat = float (swapdiff) / float(swapstat['total'])
        swapperc = int(round (swapfloat * 100))
        mem_process = "Memory status" + \
                "\n" + " Mem Total : \t" + str(memstat['total']/1048576) + \
                " MB \t \t Swap Total : \t" + str(swapstat['total']/1048576) + \
                " MB" + \
                "\n" + " Mem Used : \t" + str(memstat['used']/1048576) + \
                " MB \t \t Swap Used : \t" + str(swapstat['used']/1048576) + \
                " MB" + \
                "\n" + " Mem Free : \t" + str(memstat['free']/1048576)  + \
                " MB \t \t \t Swap Free : \t" + str(swapstat['free']/1048576) + \
                " MB" + "\n" + " Mem Used : \t" + str(memperc) + " %" + \
                " \t \t \t Swap Used : \t" + str(swapperc) + " %" 
        return mem_process

    @botcmd
    def ip(self, mess, args):
        """Displays the IP Addresses of the server."""
        #Source: http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        int_ipaddr = s.getsockname()[0]
        ext_ipaddr = urllib2.urlopen("http://whatismyip.com/automation/n09230945.asp").read()
        data_ipaddr = "Internal IP address: \t" + int_ipaddr + \
               "\n" +"External IP address: \t" + ext_ipaddr
        return data_ipaddr

 
def read_config(file, config_jabber={}):
    """
    Read the configuration data from user's home directory.
    Create an example file if it doesn't exist.
    
    Based on MythJabberbot (http://www.ian-barton.com/wiki/MythTV/MythJabberbot)
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
