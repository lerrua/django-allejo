#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import re
import sys


version = '0.1.0'
name = 'django-allejo'
package = 'allejo'
description = 'Management and creation for custom tournaments and \
rankings for many sports.'
url = 'http://github.com/lerrua/django-allejo'
author = 'Igor P. Leroy'
author_email = 'ip.leroy@gmail.com'
license = 'BSD'
install_requires = []

setup(
    name=name,
    version=version,
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(),
    include_package_data=True,
    description=description,
    keywords = ['standings', 'soccer', 'football', 'ranking'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
    install_requires=install_requires
)
