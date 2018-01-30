#!/usr/bin/env python

import os
import re
import sys
import codecs

from setuptools import setup, find_packages

def read(*parts):
    file_path = os.path.join(os.path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()

setup(
    name='django-spurl',
    version='0.6.4',
    license='Public Domain',

    install_requires=[
        'urlobject>=2.4.0',
        'six',
    ],
    setup_requires=[
        'urlobject>=2.4.0',
        'django>=1.4,<2.0',
        'six',
    ],

    description='A Django template library for manipulating URLs.',
    long_description=read('README.md') + '\n\n' + read('CHANGES'),

    author='Jamie Matthews',
    author_email='jamie.matthews@gmail.com',

    maintainer='Basil Shubin',
    maintainer_email='basil.shubin@gmail.com',

    url='http://github.com/j4mie/django-spurl',
    download_url='https://github.com/j4mie/django-spurl/zipball/master',
    
    packages=find_packages(exclude=('example*', '*.tests*')),
    include_package_data=True,

    zip_safe=False,
)
