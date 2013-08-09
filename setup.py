#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PrintUs
-------

    :copyright: (c) 2013 - Stephane Wirtel <stephane@wirtel.be>
    :license: MIT, see LICENSE for more details
"""
import os
import sys
from setuptools import setup
from setuptools import find_packages

from printus import release

HERE = os.path.dirname(__file__)

if not hasattr(sys, 'version_info') or sys.version_info < (2, 6, 0, 'final'):
    raise SystemExit("PrintUs requires Python 2.6 or later.")

with open('README.rst') as fp:
    README = fp.read()

with open('CHANGES.rst') as fp:
    CHANGES = fp.read()

with open(os.path.join(HERE, 'requirements.txt')) as fp:
    requirements = fp.read()


setup(
    name                 = release.title,
    version              = release.version,
    url                  = release.url,
    license              = 'MIT',
    description          = release.description,
    long_description     = README + '\n' + CHANGES,
    author               = release.author,
    author_email         = release.author_email,
    packages             = find_packages(),
    include_package_data = True,
    zip_safe             = False,
    platforms            = 'any',
    install_requires     = requirements,
    entry_points      = """
    [console_scripts]
    """,
    classifiers       = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
