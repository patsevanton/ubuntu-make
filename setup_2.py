#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2014 Canonical
#
# Authors:
#  Didier Roche
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import codecs
import os
import re
import sys
from setuptools import setup, find_packages

# Common distribution data
name = 'ubuntu-make'
version = 'devel'
description = 'setup your development environment on ubuntu easily'
url = 'https://github.com/ubuntu/ubuntu-make'

license = 'GPL v3'
classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Build Tools',
    'Topic :: System :: Software Distribution',
)

# look/set what version we have
changelog = 'debian/changelog'
if os.path.exists(changelog):
    head = codecs.open(changelog, encoding='utf-8').readline()
    match = re.compile('.*\((.*)\).*').match(head)
    if match:
        version = match.group(1)

setup(
    name=name,
    version=version,
    description=description,
    #author_email=author_email,
    url=url,
    packages=find_packages(exclude=["tests*"]),
    package_data={},
    license=license,
    classifiers=classifiers,
    # non-cx_Freeze arguments
    entry_points={
        'console_scripts': [
            'umake = umake:main',
        ],
    },
    # This is not in console_scripts because we need a clean environment
    data_files=[
        ('lib/python3/dist-packages/umake', ['umake/version']),
        ('share/zsh/vendor-completions', ['confs/completions/_umake']),
    ]
)