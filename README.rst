pysysbot 
========
A simple python jabber bot for getting system information.

This Python jabber (XMPP) bot is based on the `slimxmpp framework`_. The bot
is capable to display details about the system it is running on. If you don't
want or can stay connected through SSH all the time this is an easy way to get
information about the remote system.

This bot contains a lot of parts used in a German tutorial about the the
jabberbot framework on `Swissjabber`_.
 
.. _slimxmpp framework: https://slixmpp.readthedocs.io
.. _Swissjabber: http://www.swissjabber.org

Goals
----- 
- Show some information about the system
- No need for a permanent SSH connection to the remote system
- Can serve for many users
 
Requirements
------------
 
- `slimxmpp`_
- `psutil`_

All dependencies are available in the Fedora Package Collection.::

    sudo dnf -y install python3-slimxmpp python3-psutil

.. _slimxmpp: https://slixmpp.readthedocs.io
.. _psutil: https://psutil.readthedocs.io

Installation
------------

The package is available in the Fedora Package collection. Then::

    sudo dnf -y install pysysbot

Till then, clone the git repository to use it.::

    git clone https://github.com/fabaff/pysysbot

Usage
-----

Create a configuration file: ``/etc/pysysbot/pysysbot.conf`` with the following
content or edit the file if you are running a release which is included in
your distribution::

    [pysysbot]
    username = Your JID
    password = Your XMPP/Jabber password

You can run ``pysysbot`` from the command-line or as service with systemd.::

    sudo systemctl start pysysbot.service

Resources
---------

- `Website`_
- `git repository`_
- `Download`_

.. _Website: http://affolter-engineering.ch/pysysbot/
.. _git repository: https://github.com/fabaff/pysysbot
.. _Download: https://github.com/fabaff/pysysbot/releases

``pysysbot`` is licensed under BSD, for more details check COPYING. 
