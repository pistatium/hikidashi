# coding: utf-8

import os
import sys
from setuptools import setup, find_packages

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

setup(
    name='hikidashi',
    version='0.0.1',
    url='https://github.com/pistatium/hikidashi',
    author='pistatium',
    description='Key-Value store over http protcol.',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
    ],
    extras_require={
        'test': [
            'pytest',
        ],
        'server': [
            'uwsgi'
        ]
    },
    entry_points={
        'console_scripts': [
            'hikidashi=hikidashi.cmd:main'
        ]
    },
)
