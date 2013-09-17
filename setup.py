# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009-2011 Fabian Affolter <fabian@affolter-engineering.ch>
#
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from setuptools import setup

if __name__ == '__main__':
    setup(
        name = 'pysysbot',
        version="0.1.2",
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
