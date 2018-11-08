# !/usr/bin/env python
# encoding: utf-8

from setuptools import find_packages, setup

NAME = 'autocorrect'
DESCRIPTION = 'A CLI-based tool for making bulk changes to file text.'
URL = 'https://github.com/alycejenni/autocorrect'
EMAIL = 'alycejenni@gmail.com'
AUTHOR = 'Alice Butcher'
VERSION = '0.1.3'

REQUIRED = ['click', 'redbaron']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    package_data={
        'autocorrect': ['data/autocorrect.json']
        },
    include_package_data=True,
    entry_points='''
        [console_scripts]
        autocorrect=autocorrect.cli:cli
    ''',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
        ]
    )
