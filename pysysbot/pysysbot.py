# This file is part of pysysbot.
#
# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2013 Fabian Affolter <fabian at affolter-engineering.ch>
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
try:
    import datetime
    import os
    import sys
    import socket
    import ConfigParser
    import urllib2
    import statgrab
    from jabberbot import JabberBot, botcmd
    import settings
except ImportError:
	print """Cannot find all required libraries please install them and try again."""
	raise SystemExit

__version__ = '0.1.1'
__author__ = 'Fabian Affolter <fabian@affolter-engineering.ch>'

class pySysBot(JabberBot):
    """
    This is a simple Jabber bot that can show you some details and
    information of the machine it is running on.
    """
    def top_of_help_message(self):
        """Returns a string that forms the top of the help message."""
        return "pySysBot\n\n"

#Bot commands
    @botcmd
    def version(self, mess, args):
        """Details about the bot."""
        version = '\n%s %s with Python %s\n%s\n%s' % (self.__class__.__name__,
            __version__,
            '.'.join([str(v) for v in sys.version_info[:3]]),
            'Author: %s' % __author__,
            'pysysbot is licensed under GPLv3+'
            )
        return version

    @botcmd
    def kernel(self, mess, args):
        """Kernel which is used."""
        kernel = os.uname()[2]
        return kernel

    @botcmd
    def time(self, mess, args):
        """Current system time."""
        ctime = datetime.datetime.today().strftime('%A, %d. %B %Y %H:%M:%S')
        return ctime

    @botcmd
    def uptime(self, mess, args):
        """The uptime of the system."""
        uptime = open('/proc/uptime').read().split()[0]
        # This is heavily based on the work of Hubert Chathi and his System status bot.
        uptime = float(uptime)
        (uptime, secs) = (int(uptime / 60), uptime % 60)
        (uptime, mins) = divmod(uptime, 60)
        (days, hours) = divmod(uptime, 24)

        uptime = '%d day%s, %d hour%s %02d min%s' % (days, days != 1 
            and 's' or '', hours, hours != 1 and 's' or '', mins,
            mins != 1 and 's' or '')
        return uptime

    @botcmd
    def system(self, mess, args):
        """Displays details about system."""
        system = os.uname()
        system_data = "\nSystem information" + \
                "\n" + " Type:     " + system[0] + \
                "\n" + " FQDN:    " + system[1] + \
                "\n" + " Kernel:   " + system[2] + \
                "\n" + " Data:     " + system[3] + \
                "\n" + " Arch:     " + system[4]
        return system_data

    @botcmd
    def load(self, mess, args):
        """Displays the system load over the last 1, 5, and 15 minutes."""
        loaddata = []
        load = os.getloadavg()
        for i in load:
                loaddata.append(i)
        load_data = "\nLoad average of the system" + \
                "\n" +"  1 min: \t" + str(loaddata[0]) + \
                "\n" +"  5 min: \t" + str(loaddata[1]) + \
                "\n" +" 15 min: \t" + str(loaddata[2])
        return load_data

    @botcmd
    def processes(self, mess, args):
        """Shows the processes of the system."""
        process = statgrab.sg_get_process_count()
        load_process = "\nProcesses" + \
                "\n" + " Zombie: \t\t"  + str(process['zombie']) + \
                "\n" + " Running: \t"   + str(process['running']) + \
                "\n" + " Stopped: \t"   + str(process['stopped']) + \
                "\n" + " Sleeping: \t"  + str(process['sleeping']) + \
                "\n" + " Total: \t\t"   + str(process['total'])
        return load_process

    @botcmd
    def mem(self, mess, args):
        """Memory status of the system."""
        # Stolen from some 
        swapstat = statgrab.sg_get_swap_stats()
        memstat = statgrab.sg_get_mem_stats()
        # Some calculation to get the perc of the data
        memdiff = memstat['total'] - memstat['free']
        memfloat = float (memdiff) / float(memstat['total'])
        memperc = int(round (memfloat * 100))
        swapdiff = swapstat['total'] - swapstat['free']
        swapfloat = float (swapdiff) / float(swapstat['total'])
        swapperc = int(round (swapfloat * 100))
        mem_process = "\nMemory status" + \
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

#    @botcmd
#    def ip(self, mess, args):
#        """Displays the IP Addresses of the server."""
#        # Source: http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/
#        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        s.connect(('google.com', 0))
#        int_ipaddr = s.getsockname()[0]
#        ext_ipaddr = urllib2.urlopen("http://automation.whatismyip.com/n09230945.asp").read()
#        data_ipaddr = "\nInternal IP address: \t" + int_ipaddr + \
#               "\n" +"External IP address: \t" + ext_ipaddr
#        return data_ipaddr

def main():
    config = settings.read_config('/etc/pysysbot/pysysbot.conf')
    bot = pySysBot(config[0]['username'], config[0]['password'], debug=False)
    bot.serve_forever()

if __name__ == '__main__':
    main()
