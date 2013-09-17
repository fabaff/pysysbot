# This file is part of pysysbot.
#
# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2013 Fabian Affolter <fabian at affolter-engineering.ch>
#
# Released under the BSD license. See COPYING file for details.
#
try:
    import datetime
    import os
    import sys
    import socket
    import ConfigParser
    import urllib2
    import psutil
    from jabberbot import JabberBot, botcmd
    import settings
except ImportError:
	print """Cannot find all required libraries please install them and try again."""
	raise SystemExit

__version__ = '0.1.2'
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
            'pysysbot is licensed under BSD'
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
        """Shows the count of processes of the system."""
        processes = psutil.get_pid_list()
        return 'Running processes: %i' % (len(processes))

    @botcmd
    def disk(self, mess, args):
        # Credits: https://code.google.com/p/psutil/source/browse/examples/disk_usage.py
        """Details about the disk usage."""
        templ = "%-35s %8s %8s %8s %5s%% %9s  %s\n"
        disks = templ % ("Device", "Total", "Used", "Free", "Use ", "Type", "Mount")
        for part in psutil.disk_partitions(all=False):
            usage = psutil.disk_usage(part.mountpoint)
            disks = disks + templ % (part.device,
                            bytes2human(usage.total),
                            bytes2human(usage.used),
                            bytes2human(usage.free),
                            int(usage.percent),
                            part.fstype,
                            part.mountpoint)
        return disks

    @botcmd
    def mem(self, mess, args):
        """Memory status of the system."""
        vmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        mem = "\nMemory status" + \
                "\n" + " Mem total  : \t" + bytes2human(vmem[0]) + \
                "\t Swap total : \t" + bytes2human(swap[0]) + \
                "\n" + " Mem used   : \t" + bytes2human((vmem[0] - vmem[1])) + \
                "\t Swap used  : \t" + bytes2human(swap[1]) + \
                "\n" + " Mem avail. : \t" + bytes2human(vmem[1]) + \
                "\t Swap free  : \t" + bytes2human(swap[2]) + \
                "\n" + " Mem used   : \t" + str(vmem[2]) + " %" + \
                " \t Swap used  : \t" + str(swap[3]) + " %"
        return mem

    @botcmd
    def who(self, mess, args):
        """Information about users who are currently logged in."""
        users = psutil.get_users()
        who = '\n'
        for user in users:
            who = who + '%-10s %-10s %s  (%s)\n' % \
                    (user.name,
                    user.terminal or '-',
                    datetime.datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M"),
                    user.host)
        return who

def bytes2human(n):
    # Credits: http://code.activestate.com/recipes/578019
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def main():
    config = settings.read_config('/etc/pysysbot/pysysbot.conf')
    bot = pySysBot(config[0]['username'], config[0]['password'], debug=False)
    bot.serve_forever()

if __name__ == '__main__':
    main()
