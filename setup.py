#!/usr/bin/env python3
"""Set up the pySysBot."""
import os
import sys

from setuptools import setup

from pysysbot.constants import VERSION as __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as desc:
    long_description = desc.read()

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

setup(
    name='pysysbot',
    version=__version__,
    description="Python based system jabber bot",
    long_description=long_description,
    author="Fabian Affolter",
    author_email='fabian@affolter-engineering.ch',
    maintainer="Fabian Affolter",
    maintainer_email="fabian@affolter-engineering.ch",
    url='http://affolter-engineering.ch/pysysbot/',
    license='BSD',
    platforms='Linux',
    packages=['pysysbot'],
    entry_points={
        'console_scripts': ['pysysbot = pysysbot.pysysbot:main']
    },
    include_package_data=True,
    install_requires=[
        'psutil',
        'slixmpp',
    ],
    keywords=['Jabber', 'XMPP', 'System', 'python'],
    classifiers=[
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
            ],
)
