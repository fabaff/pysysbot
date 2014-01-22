# This file is part of pysysbot.
#
# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2014 Fabian Affolter <fabian at affolter-engineering.ch>
#
# Released under the BSD license. See COPYING file for details.
#
from setuptools import setup

if __name__ == '__main__':
    setup(
        name = 'pysysbot',
        version="0.1.3",
        description = 'Python based system jabber bot',
        long_description = """This python jabber (XMPP) bot is based on \
            the jabberbot framework (http://thpinfo.com/2007/python-jabberbot/).\
            The bot is capable to display details about the system it \
            is running on. """,
        author = 'Fabian Affolter',
        author_email = 'fabian@affolter-engineering.ch',
        maintainer = 'Fabian Affolter',
        maintainer_email = 'fabian@affolter-engineering.ch',
        url = 'http://affolter-engineering.ch/pysysbot/',
        license = 'BSD',
        platforms = 'Linux',
        packages = ['pysysbot'],
        entry_points = {
            'console_scripts': ['pysysbot = pysysbot.pysysbot:main']
        },
        include_package_data = True,
        install_requires=[
            'psutil',
            'jabberbot',
        ],
        keywords = ['Jabber','XMPP','System','python'],
        classifiers = [
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: System Administrators',
                'License :: OSI Approved :: BSD License',
                'Operating System :: POSIX',
                'Programming Language :: Python',
                'Topic :: Communications',
                'Topic :: Internet',
                'Topic :: System',
                'Topic :: System :: Monitoring',
                'Topic :: System :: Networking'
                ],
    )
