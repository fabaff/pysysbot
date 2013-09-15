#pysysbot: A simple python jabber bot for getting system information

This python jabber (XMPP) bot is based on the [jabberbot framework] 
(http://thpinfo.com/2007/python-jabberbot/). The bot is capable to
display details about the system it is running on. If you don't
want or can stay connected through SSH all the time this is an easy
way to get information about the remote system.

This bot contains a lot of parts used in a German tutorial about the the
jabberbot framework on http://www.swissjabber.org.
 
##Goals
 
- Show some information about the system
- No need for a permanent SSH connection to the remote system
- Can serve for many users
 
##Requirements
 
- python-jabberbot (http://thp.io/2007/python-jabberbot/)
- pystatgrab (http://www.i-scream.org/pystatgrab/)

All dependencies are available in the Fedora Package Collection.

```
sudo yum -y install python-jabberbot pystatgrab
```

##Installation

The packge will soon be available in the Fedora Package collection. Then

```
sudo yum -y install pysysbot
```

Till then, clone the git repository to use it.

```
git clone https://gitorious.org/pysysbot
```

##Usage

Create a configuration file: `/etc/pysysbot/pysysbot.conf` with the following
content or edit the file if you are running a release which is included in
your distribution:

```
[pysysbot]
username = Your JID
password = Your XMPP/Jabber password
```
You can run `pysysbot` from the command-line or as service with systemd.

```
sudo systemctl start pysysbot.service
```

##Resources

- [Website](http://affolter-engineering.ch/pysysbot/)
- [git repository](https://gitorious.org/pysysbot)
 
`pysysbot` is licensed under GPLv3+, for more details check COPYING. 
