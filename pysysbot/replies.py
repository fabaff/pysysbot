"""The available replies."""
import datetime
import os
import sys
import socket
import psutil

from .constants import VERSION as __version__, AUTHOR_EMAIL


def version():
    """Details about the bot."""
    version = 'pySysBot %s \n%s\n%s' % (
        __version__,
        'Author: {}'.format(AUTHOR_EMAIL),
        'pysysbot is licensed under BSD',
    )
    return version


def kernel():
    """Show which kernel is used."""
    kernel = os.uname()[2]
    return kernel


def time():
    """Show the current system time."""
    ctime = datetime.datetime.today().strftime('%A, %d. %B %Y %H:%M:%S')
    return ctime


def uptime():
    """Show the uptime of the system."""
    uptime = open('/proc/uptime').read().split()[0]
    # This is heavily based on the work of Hubert Chathi and his System bot.
    uptime = float(uptime)
    (uptime, secs) = (int(uptime / 60), uptime % 60)
    (uptime, mins) = divmod(uptime, 60)
    (days, hours) = divmod(uptime, 24)

    uptime = '%d day%s, %d hour%s %02d min%s' % (
        days,
        days != 1 and 's' or '',
        hours,
        hours != 1 and 's' or '',
        mins,
        mins != 1 and 's' or '',
    )
    return uptime


def system():
    """Display details about system."""
    system = os.uname()
    system_data = (
        "\nSystem information"
        + "\n"
        + " Type:     "
        + system[0]
        + "\n"
        + " FQDN:    "
        + system[1]
        + "\n"
        + " Kernel:   "
        + system[2]
        + "\n"
        + " Data:     "
        + system[3]
        + "\n"
        + " Arch:     "
        + system[4]
    )
    return system_data


def load():
    """Display the system load over the last 1, 5 and 15 minutes."""
    loaddata = []
    load = os.getloadavg()
    for i in load:
        loaddata.append(i)
    load_data = (
        "\nLoad average of the system"
        + "\n"
        + "  1 min: \t"
        + str(loaddata[0])
        + "\n"
        + "  5 min: \t"
        + str(loaddata[1])
        + "\n"
        + " 15 min: \t"
        + str(loaddata[2])
    )
    return load_data


def processes():
    """Show the count of processes of the system."""
    processes = psutil.get_pid_list()
    return "Running processes: {}".format(len(processes))


# Credits: https://code.google.com/p/psutil/source/browse/examples/disk_usage.py
def disk():
    """Show details about the disk usage."""
    templ = "%-35s %8s %8s %8s %5s%% %9s  %s\n"
    disks = templ % (
        "Device",
        "Total",
        "Used",
        "Free",
        "Use ",
        "Type",
        "Mount",
    )
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        disks = disks + templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint,
        )
    return disks


def mem():
    """Show memory status of the system."""
    vmem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    mem = (
        "\nMemory status"
        + "\n"
        + " Mem total  : \t"
        + bytes2human(vmem[0])
        + "\t Swap total : \t"
        + bytes2human(swap[0])
        + "\n"
        + " Mem used   : \t"
        + bytes2human((vmem[0] - vmem[1]))
        + "\t Swap used  : \t"
        + bytes2human(swap[1])
        + "\n"
        + " Mem avail. : \t"
        + bytes2human(vmem[1])
        + "\t Swap free  : \t"
        + bytes2human(swap[2])
        + "\n"
        + " Mem used   : \t"
        + str(vmem[2])
        + " %"
        + " \t Swap used  : \t"
        + str(swap[3])
        + " %"
    )
    return mem


def who():
    """Information about users who are currently logged in."""
    users = psutil.users()
    who = '\n'
    for user in users:
        who = who + '%-10s %-10s %s  (%s)\n' % (
            user.name,
            user.terminal or '-',
            datetime.datetime.fromtimestamp(user.started).strftime(
                "%Y-%m-%d %H:%M"
            ),
            user.host,
        )
    return who


# Credits: http://code.activestate.com/recipes/578019
def bytes2human(n):
    """Convert bytes to human readable format."""
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

